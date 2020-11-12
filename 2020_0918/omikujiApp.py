import tkinter as tk
import random

def displabel():
    kuji = ['大吉', '中吉', '小吉', '凶']
    lbl.configure(text=random.choice(kuji))

root = tk.Tk()
root.geometry('200x100')

lbl = tk.Label(text='LABEL')
btn = tk.Button(text='PUSH', command = displabel)

lbl.pack()
btn.pack()
tk.mainloop()

