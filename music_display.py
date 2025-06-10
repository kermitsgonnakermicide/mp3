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
        self.media=None
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
    async def play_music(self):
        self.media = vlc.MediaPlayer(song.path)
        self.media.play()
    def pause_music(self):
        self.media.pause()
    async def set_volume(self,volume: int):
        self.media.audio_set_volume(i_volume=volume)
if __name__ == "__main__":

