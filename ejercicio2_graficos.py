# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 09:54:08 2022

@author: lab
"""

import tkinter as tk 
root = tk.Tk()

w= tk.Canvas(root, width = 200 , height= 100)
w.pack()

w.create_rectangle(50,20,150,80 ,fill = "green")
w.create_rectangle(65,35,135,65 ,fill = "yellow")
w.create_line(0,0,50,20 ,fill = "red", width=3)
w.create_line(0,100,50,80 ,fill = "blue", width=3)
w.create_line(150,20,200,0 ,fill = "black", width=3)
w.create_line(150,80,200,100 ,fill = "light blue", width=3)
root.mainloop()