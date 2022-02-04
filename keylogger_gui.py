from tkinter import *
import sys

class MainWindow:
  def __init__(self, root, title, geometry, message):
    self.root = root
    self.root.title(title)
    self.root.geometry(geometry)
    Label(self.root, text=message, font=("Helvetica", 16)).pack(pady=20)
    button1 = Button(self.root, text="logs", command=self.logs)
    button1.pack()
    self.root.mainloop()

  def logs(self):
    self.new_win =  Toplevel(self.root)
    self.new_win = Showlogs(self.new_win, "logs", "1280x720+360+210", "Logs are here")

class Showlogs:
  def __init__(self, root, title, geometry, message):
    self.root = root
    self.root.title(title)
    self.root.geometry(geometry)
    Label(self.root, text=message, font=("Helvetica", 16)).pack(pady=2)
    self.root.mainloop()

def main():
  root = Tk()
  window = MainWindow(root, "keylogger", "400x400+573+306", "BUTTONS")

if __name__ == "__main__":
  main()