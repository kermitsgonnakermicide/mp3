import io

import PIL
import gpiozero
from PIL import Image, ImageDraw, ImageFont
import eyed3
from mutagen.id3 import ID3
import os
import vlc
from gui import song, draw_text
from LCD_2inch4 import LCD_2inch4

#this is very stupid
# 2 libraries :(((
current_sel = 0

class Music_Display:

    def __init__(self,song: song):
        self.lcd = LCD_2inch4()
        #stupid? yes. No pointers? indeed
        self.lcd.Init()
        self.lcd.clear()
        self.song = song
    def audio_dac(self):
        Image= PIL.Image.new("RGB", (640,480), color=(255,255,255))
        canvas = ImageDraw.Draw(Image)
        draw_text(25,25,self.song.title,canvas,"WHITE")
        canvas.bitmap(self.song.image)
        canvas.line([(0,30),(30,0)],"WHITE",5)
        canvas.line([(1, 30), (30, 0)], "RED", 5)
        media = vlc.MediaPlayer(song)
        media.play()
if __name__ == "__main__":

