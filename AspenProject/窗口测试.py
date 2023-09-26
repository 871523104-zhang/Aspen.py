import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
import ttkbootstrap as ttkb
from PIL import ImageTk, Image

root = tk.Tk()
style = ttkb.Style("morph")
root.title("Aspen设置")
root.geometry("800x500")
note = Notebook(root, width=800, height=500)

# 添加标题图片
img1 = Image.open(r"F:\AspenPlus-Python-Interface-main\AspenPlus-Python-Interface-main\AspenProject\标题.png")
photo = ImageTk.PhotoImage(img1)
imglabel = Label(root, image=photo)
imglabel.place(x=0, y=0)

fr1 = Frame()
fr2 = Frame()
fr3 = Frame()

note.place(x=0, y=70)

note.add(fr1, text='input')
note.add(fr2, text='result')
note.add(fr3, text='...')

label = tk.Label(fr2, text="Temperature：", font="等线")
label.grid(row=0, column=0)
label = tk.Label(fr2, text="-50")
label.grid(row=0, column=1)

root.mainloop()