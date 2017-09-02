from blinkstick import blinkstick
import time

def loop_square():
  bstick = blinkstick.find_first()
  for y in range(0,10):
    for x in range(0,8):
      if x>=1: bstick.set_color(channel=0, index=(x-1))
      if x<8:  bstick.set_color(channel=0, index=x, name="blue")
      time.sleep(0.05)
    turn_off_square()

def turn_off_square():
  bstick = blinkstick.find_first()
  for x in range(0,8):
    bstick.set_color(channel=0, index=x)



loop_square()

