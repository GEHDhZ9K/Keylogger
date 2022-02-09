#!/usr/bin/env python3

from pynput import keyboard
import time

def time_now():
  c_time = time.ctime().split(" ")[1:6]
  del c_time[1]
  return c_time

def on_press(key):
  try:
    print("this func is working, on_press", key.char)
  except AttributeError:
    print("Special key char", key)

def on_release(key):
  print("this func is working, on_release", key)
  if key == keyboard.Key.esc:
    return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
  listener.join()