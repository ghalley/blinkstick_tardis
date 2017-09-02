from blinkstick import blinkstick
import time
import pygame
from subprocess import call


def loop_square():
  call(['sudo', 'amixer', 'cset', 'numid=3', '1'])
  bstick = blinkstick.find_first()
  pygame.init()
  SONG_END = pygame.USEREVENT + 1
  
  pygame.mixer.music.set_endevent(SONG_END)
  pygame.mixer.music.load('/home/pi/Projects/b_square/TARDIS.mp3')
  
  pygame.mixer.music.play()

  print 'Playing song'
  for event in pygame.event.get():
    print 'Inside event loop'
    while event.type != SONG_END: 
      for x in range(0,8):
        if x>=1: bstick.set_color(channel=0, index=(x-1))
        if x<8:  bstick.set_color(channel=0, index=x, name="white")
        time.sleep(0.05)
    turn_off_square()
  time.sleep(16)

def turn_off_square():
  bstick = blinkstick.find_first()
  for x in range(0,8):
    bstick.set_color(channel=0, index=x)

loop_square()


