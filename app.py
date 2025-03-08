import tkinter
from tkinter import *

root = Tk()

root.geometry("400x600")
root.title("Face Recognition")
root.resizable(width=0, height=0)
root.iconphoto(True, PhotoImage(file="Media/icon.png"))

mainLabel = tkinter.Label(root, text = "Attendance System")


root.mainloop()