import io

import gpiozero
from PIL import Image, ImageDraw, ImageFont
import eyed3
from mutagen.id3 import ID3
import os

from LCD_2inch4 import LCD_2inch4

#this is very stupid
# 2 libraries :(((
current_sel = 0

lcd = LCD_2inch4()
lcd.Init()
def extract_album_art_pil(mp3_file):
    try:
        audio = ID3(mp3_file)

        for tag in audio.values():
            if tag.FrameID == "APIC":
                image_data = tag.data
                image = Image.open(io.BytesIO(image_data))
                print(f"Image format: {image.format}, size: {image.size}, mode: {image.mode}")
                return image.resize((240, 320), Image.ANTIALIAS)

        print("No album art found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


test_songs = []

class song:
    def __init__(self, path):
        self.title = None
        self.artist = None
        self.album = None
        self.image = None
        data = eyed3.load(path=path)
        if data is None or data.tag is None:
            self.artist = "No Metadata"
            self.title = "No Metadata"
            self.album = "No Metadata"
        else:
            self.title = data.tag.title if data.tag.title else "Unknown Title"
            self.artist = data.tag.artist if data.tag.artist else "Unknown Artist"
            self.album = data.tag.album if data.tag.album else "Unknown Album"
            #this is even more stuoid
            #use fallback rpi image
            self.image = extract_album_art_pil(path) if extract_album_art_pil(path) else  bytearray(b"\x00\x00\x00"
                                                                                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    def return_format_data(self):
        return f"{self.title} By {self.artist}"


def setup():
    files = os.listdir("./music")
    print(files)
    for file in files:
        if file.endswith('.mp3'):
            nest = song(os.path.join('music', file))
            test_songs.append(nest)


def display_init():
    global current_sel
    lcd.clear()
    setup()
    image1 = Image.new("RGB", (lcd.width, lcd.height), "BLACK")
    draw = ImageDraw.Draw(image1)
    width = lcd.width
    height = lcd.height

    num_songs = len(test_songs)
    if num_songs == 0:
        draw.text()
        return

    padding_top = 20
    padding_bottom = 20
    available_height = height - padding_top - padding_bottom
    item_height = available_height // num_songs if num_songs > 0 else 30
    if item_height < 25:
        item_height = 25

    for i, song_obj in enumerate(test_songs):
        y_pos = padding_top + (i * item_height)

        rect_x1 = 5
        rect_y1 = y_pos
        rect_x2 = width - 5
        rect_y2 = y_pos + item_height - 2
        text_x = rect_x1 + 5
        text_y = rect_y1 + 5

        if i == current_sel:
            draw.rectangle([(rect_x1, rect_y1), (rect_x2, rect_y2)],
                           fill="WHITE", outline="BLACK")
            draw.bitmap((rect_x1, rect_y1), song_obj.image)
            text_color = "BLACK"
            print(f"Song {i + 1} (SELECTED): Rect({rect_x1},{rect_y1},{rect_x2},{rect_y2}) Text({text_x},{text_y})")
        else:
            draw.rectangle([(rect_x1, rect_y1), (rect_x2, rect_y2)],
                           fill="BLACK", outline="WHITE")
            text_color = "WHITE"
            print(f"Song {i + 1}: Rect({rect_x1},{rect_y1},{rect_x2},{rect_y2}) Text({text_x},{text_y})")
        song_text = song_obj.return_format_data()
        max_chars = 25
        if len(song_text) > max_chars:
            song_text = song_text[:max_chars - 3] + "..."
        try:
            font = ImageFont.truetype("fonts/Font00.ttf", 16)  # Smaller font to fit better
        except:
            font = ImageFont.load_default()
        draw_text((text_x, text_y), song_text, "BLACK")
        draw.text((text_x, text_y), song_text, fill=text_color, font=font)

        print(f"  Text: '{song_text}'")

    print("-" * 50)

    lcd.ShowImage(image1)

    return image1
def draw_text(x,y,text,Image, text_color, max_chars=25):
    if len(text) > max_chars:
        song_text = text[:max_chars - 3] + "..."
    try:
        font = ImageFont.truetype("fonts/Font00.ttf", 16)  # Smaller font to fit better
    except:
        font = ImageFont.load_default()

    Image.text((x, y), text, fill=text_color, font=font)
def increase_button():
    global current_sel
    button = gpiozero.Button(12)
    if button.is_held:
        current_sel+=1
        display_init()
def test_display_console():
    class TestSong:
        def __init__(self, title, artist, album):
            self.title = title
            self.artist = artist
            self.album = album

        def return_format_data(self):
            return f"{self.title} By {self.artist}"

    setup()

    width = 240
    height = 320

    num_songs = len(test_songs)
    padding_top = 20
    padding_bottom = 20
    available_height = height - padding_top - padding_bottom
    item_height = available_height // num_songs if num_songs > 0 else 30



    for i, song_obj in enumerate(test_songs):
        y_pos = padding_top + (i * item_height)

        rect_x1 = 5
        rect_y1 = y_pos
        rect_x2 = width - 5
        rect_y2 = y_pos + item_height - 2

        text_x = rect_x1 + 5
        text_y = rect_y1 + 5

        song_text = song_obj.return_format_data()
        if len(song_text) > 25:
            song_text = song_text[:22] + "..."

        status = "SELECTED" if i == current_sel else "NORMAL"
        print(f"Song {i + 1} ({status}):")
        print(f"  Rectangle: ({rect_x1}, {rect_y1}) to ({rect_x2}, {rect_y2})")
        print(f"  Text pos: ({text_x}, {text_y})")
        print(f"  Text: '{song_text}'")
        print()


if __name__ == "__main__":
    display_init()
    while True:
        increase_button()
