from tkinter import *
import tkinter.ttk as ttk
import csv, os

global_font = ("Arial", 16, "bold")

class MainWindow:
  def __init__(self, root, title, geometry):
    self.root = root
    self.root.title(title)
    self.root.geometry(geometry)
    button1 = Button(self.root, text="Show Logs", font=global_font, command=self.logs, height=3, width=15).pack(pady=10)
    button2 = Button(self.root, text="Delete Logs", font=global_font, command=self.delete_logs, height=3, width=15).pack(pady=10)
    button3 = Button(self.root, text="Close Application", font=global_font, command=self.root.destroy, height=3).pack(pady=10)
    
    self.root.mainloop()

  def logs(self):
    self.new_win =  Toplevel(self.root)
    self.new_win = Log_table(self.new_win, "Log Table", "900x222+510+425")

  def delete_logs(self):
    self.remove = os.remove("./logs/logs.csv")

class Log_table:
  def __init__(self, root, title, geometry):
    self.root = root
    self.root.title(title)
    self.root.geometry(geometry)
    self.root.resizable(0, 1)

    self.TableMargin = Frame(self.root, width=500)
    self.TableMargin.pack(side=TOP)
    self.scrollbary = Scrollbar(self.TableMargin, orient=VERTICAL)
    self.tree = ttk.Treeview(self.TableMargin, columns=("key", "pressed" ,"released", "time"))
    
    self.style = ttk.Style(self.TableMargin)
    self.style.configure("Log.Treeview", rowheight=70)
    
    self.scrollbary.config(command=self.tree.yview)
    self.scrollbary.pack(side=RIGHT, fill=Y)

    self.tree.heading("pressed", text="pressed", anchor=W)
    self.tree.heading("released", text="released", anchor=W)
    self.tree.heading("key", text="key", anchor=W)
    self.tree.heading("time", text="time", anchor=W)
    self.tree.column("#0", stretch=NO, minwidth=0, width=0)
    self.tree.column("#1", stretch=NO, minwidth=0, width=200)
    self.tree.column("#2", stretch=NO, minwidth=0, width=200)
    self.tree.column("#3", stretch=NO, minwidth=0, width=300)
    self.tree.column("#4", stretch=NO, minwidth=0, width=300)
    self.tree.pack()

    with open("./logs/logs.csv") as f:
      reader = csv.DictReader(f, delimiter=",")
      for row in reader:
        pressed = row['pressed']
        released = row['released']
        key = row['key']
        time = row['time']
        self.tree.insert("", 1, values=(key, pressed, released, time))

    self.root.mainloop()

def main():
  root = Tk()
  window = MainWindow(root, "Keylogger", "400x400+573+306")

if __name__ == "__main__":
  main()