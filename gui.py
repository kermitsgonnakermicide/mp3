
from PIL import Image, ImageDraw, ImageFont
import eyed3
import os

test_songs = []


class song:
    def __init__(self, path):
        self.title = None
        self.artist = None
        self.album = None

        data = eyed3.load(path=path)
        if data is None or data.tag is None:
            self.artist = "No Metadata"
            self.title = "No Metadata"
            self.album = "No Metadata"
        else:
            self.title = data.tag.title if data.tag.title else "Unknown Title"
            self.artist = data.tag.artist if data.tag.artist else "Unknown Artist"
            self.album = data.tag.album if data.tag.album else "Unknown Album"

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
    lcd = LCD_2inch4.LCD_2inch4()
    lcd.Init()
    lcd.clear()
    setup()
    image1 = Image.new("RGB", (lcd.width, lcd.height), "BLACK")
    draw = ImageDraw.Draw(image1)
    width = lcd.width
    height = lcd.height

    num_songs = len(test_songs)
    if num_songs == 0:
        print("No songs found!")
        return

    padding_top = 20
    padding_bottom = 20
    available_height = height - padding_top - padding_bottom
    item_height = available_height // num_songs if num_songs > 0 else 30
    if item_height < 25:
        item_height = 25

    current_sel = 0
    print(f"\nres {width}x{height}):")
    print(f"dimensions: {lcd.width}x{lcd.height}")
    print(f"songs: {num_songs}")
    print(f"height calc: {item_height}")
    print("-" * 50)


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

        draw.text((text_x, text_y), song_text, fill=text_color, font=font)

        print(f"  Text: '{song_text}'")

    print("-" * 50)

    lcd.ShowImage(image1)

    return image1

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

    current_sel = 0

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
    test_display_console()