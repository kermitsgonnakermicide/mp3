# Day 1
the basic idea is a retro ipod (like) mp3 player with a FTP server for uploading
i used a waveshare 240*320 display.
my first decision was what kind of gui to use. SInce i could setup the display as the Pi's, i briefly considered using something like Electron (ewww) / EGui (Rust :crab:) / cTK (Python)
However. all of these wpould prevent headless execution, lowering battery life. Additionally, keyboard support is requierd, as we plan to have physical buttons. I then thought of huhh (Golang), which could be run from a TTY, but decided against it due to image support and other stuff
So, i'm making my own custom GUI using their library (ig i have to make an audio visualizer with that :( )
i will also 5bundle it with nvlc or musikcube or ncmpcpp (pls dont hurt me)

# Day 2

Mostly just code refactors, segmenting things into functions.  I setup Image drawing for album art aswell as the down button (crazy).
The media screen template was created - im using vlc python bindings to play the media properly. The song class has to be expanded to contain more information <br>
i may just have to make the media async to ensure  that i can update the Media GUI parallely