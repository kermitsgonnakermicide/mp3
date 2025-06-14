# PiMP3

A Pi4 based MP3 player, with a touchscreen display and a couple of mechanical keys(+ encoder!)<br>

I wanted to make a desktop mp3 player, something that I could use on my table or in the living room as a stand alone music player.

**Design**<br>
I wanted to use a pi4 because I saw [this](https://www.waveshare.com/3.5inch-rpi-lcd-g.htm) awesome display and wanted to structure my player around this.<br>
I made a wee little PCB for mounting my mechanical keys and encoder<br>
![img](Assets/PCB.png)<br>
And for attaching both of these, I made a case<br>
![img](Assets/CASE.png)<br>

**Software**
The python script(s) loads MP3 files, extracts their metadata and album art, and displays them on a 3.5" LCD. Our mechanical keys let you scroll and select songs, while a rotary encoder adjusts the volume. On selection, the music_display module handles playback using the chosen song.

**BOM**<Br>
| [S.NO](http://s.no/) | ITEM | QTY | UNIT PRICE | TOTAL | SRC |
| -------------------- | ---------------------- | --- | ---------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 | Raspberry Pi 4 | 1 | 59.37 | 59.37 | [https://www.silverlineelectronics.in/products/raspberry-pi-4-model-b-4gb-silverline-india?variant=40981686452393](https://www.silverlineelectronics.in/products/raspberry-pi-4-model-b-4gb-silverline-india?variant=40981686452393) |
| 2 | 3.5 inch LCD module | 1 | 18.54 | 18.54 | [https://hubtronics.in/3.5inch-rpi-lcd-g](https://hubtronics.in/3.5inch-rpi-lcd-g) |
| 3 | HMX Macchiato Switches | 1 | 3.48 | 3.48 | [https://neomacro.in/products/hmx-macchiato-linear-switch](https://neomacro.in/products/hmx-macchiato-linear-switch) |
| 4 | EC11 Encoder | 1 | 2.06 | 2.06 | [https://www.amazon.in/CentIoT-Encoder-Digital-Potentiometer-Control/dp/B0888RVZSN/ref=sr_1_1?dib=eyJ2IjoiMSJ9.ub-gVfIJkebgtPjQTQbP-1BNXrl39Ma9zP8YixnEs_tw0VYc10gQvY7xqzuh_vZceHd2y-6J9D-NB9MjzyDwMGJIKOrWb9IZEiOruOY8D37diZ-Mi-mWW6Ih14xuLm8STNjV2h-nbaJC9DMzZgZoX5PxpEv7ul9Q4GGyM7gzU9TtIZhDOw5A-AdJKh8g-Y8ljjHBeLH-eLWOzSZ4Ftt-ZvcS2EI1YVhMKyesSluyfP6xULgmHWb_qcBHdLBGNNxqSWQYmD_pLOQnpAjRdksGop-jiegdd_lhKNFeYlihQNs.C6u3HSLR85ezz9IoDRMTJXpV3etCnDG9RNMFscjRzxA&dib_tag=se&keywords=EC11+encoder&qid=1749897251&sr=8-1](https://www.amazon.in/CentIoT-Encoder-Digital-Potentiometer-Control/dp/B0888RVZSN/ref=sr_1_1?dib=eyJ2IjoiMSJ9.ub-gVfIJkebgtPjQTQbP-1BNXrl39Ma9zP8YixnEs_tw0VYc10gQvY7xqzuh_vZceHd2y-6J9D-NB9MjzyDwMGJIKOrWb9IZEiOruOY8D37diZ-Mi-mWW6Ih14xuLm8STNjV2h-nbaJC9DMzZgZoX5PxpEv7ul9Q4GGyM7gzU9TtIZhDOw5A-AdJKh8g-Y8ljjHBeLH-eLWOzSZ4Ftt-ZvcS2EI1YVhMKyesSluyfP6xULgmHWb_qcBHdLBGNNxqSWQYmD_pLOQnpAjRdksGop-jiegdd_lhKNFeYlihQNs.C6u3HSLR85ezz9IoDRMTJXpV3etCnDG9RNMFscjRzxA&dib_tag=se&keywords=EC11+encoder&qid=1749897251&sr=8-1) |
| 5 | M2.5 Bolt | 10 | 0.6 | 6 | [https://3fparts.com/shop/m2-5-50mm-socket-head-allen-bolt-cap-screw-din-912-stainless-steel-304-a2-70](https://3fparts.com/shop/m2-5-50mm-socket-head-allen-bolt-cap-screw-din-912-stainless-steel-304-a2-70) |
| 6 | PCB | 1 | ~20 | | what it cost for my last PCB |
