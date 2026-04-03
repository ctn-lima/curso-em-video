#Faça um programa em python que abra e reproduza um arquivo de audio em MP3

from pygame import mixer

mixer.init()
mixer.music.load('assets/media/sonican-thinking-time-ticking-power-223023.mp3')
mixer.music.play()