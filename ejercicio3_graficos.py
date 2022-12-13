# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 10:05:00 2022

@author: lab
"""

import tkinter as tk 

root = tk.Tk()
frame = tk.Frame(root).grid()
w= tk.Canvas(frame, width = 300 , height= 300)
w.grid()

w.create_rectangle(50,20,150,80 ,fill = "green")
w.create_line(50,20,150,80,fill = "red", width=3)
w.create_oval(50,20,150,80 ,fill = "blue")
w.create_arc(50,20,150,80 ,fill = "yellow")

w.create_text(150,80, text = "UPS")

w.create_polygon(200,10,
                     280, 280,
                     10,100,
                     5,5,
                     fill="",
                     outline="green",
                     dash=255)
root.mainloop()