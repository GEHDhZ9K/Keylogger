from tkinter import *

class MainWindow:
  def __init__(self, root, title, geometry, message):
    self.root = root
    self.root.title(title)
    self.root.geometry(geometry)
    Label(self.root, text=message, font=("Helvetica", 16)).pack(pady=20)
    self.root.mainloop()

def main():
  root = Tk()
  window = MainWindow(root, "keylogger", "400x400+573+306", "BUTTONS")

if __name__ == "__main__":
  main()