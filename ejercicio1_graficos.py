# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 09:27:58 2022

@author: lab
"""

# Canvas line 

import tkinter as tk 
root = tk.Tk()
frame = tk.Frame(root).grid()
w= tk.Canvas(frame, width = 300 , height= 300)
w.grid()
w.create_line(0,0,100,250, 400, 250)
root.mainloop()