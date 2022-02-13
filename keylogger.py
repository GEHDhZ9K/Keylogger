#!/usr/bin/env python3

from pynput import keyboard
import time, sys, os, csv

def read_lines(file="./logs/logs.csv"):
  with open(file, "r") as f:
    return f.readlines()

def create_csv(file="./logs/logs.csv"):
  anchor_values = ["pressed", "released", "key", "time"]
  with open(file, "w") as f:
    csv.writer(f).writerow(anchor_values)

def check():
  path = os.path.abspath(__file__).split("/")[0:-1]
  if os.getcwd() != "/".join(path):
    os.chdir(os.path.dirname(sys.argv[0]))

  if "logs" not in os.listdir():
    os.mkdir("logs")
    create_csv()
  elif "logs.csv" not in os.listdir("logs") or len(read_lines()) == 0:
    create_csv()

def write_on_file(keys, file="./logs/logs.csv"):
  with open(file, "a") as f:
    csv.writer(f).writerow(keys)

def time_now():
  c_time = time.ctime().split(" ")[1:6]
  return " ".join(c_time)

def on_press(key):
  keys = []
  keys.extend(("True", " "))
  try:
    keys.append(key.char)
  except AttributeError:
    keys.append(str(key).split(".")[1])

  keys.append(time_now())
  write_on_file(keys)

def on_release(key):
  keys = []
  keys.extend((" ", "True"))
  try:
    keys.append(key.char)
  except AttributeError:
    keys.append(str(key).split(".")[1])
  
  if key == keyboard.Key.end:
    return False

  keys.append(time_now())
  write_on_file(keys)

def kb_listener():
  with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

def main():
  check()
  kb_listener()

if __name__ == "__main__":
  main()