import sys
from tkinter import *
#from tkinter.ttk import *
import time

#from time import strftime

"""root=TK()
rot.title("Clock")

label= labe(root,font='')"""

def tick():
    time_string =time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200,tick)

root=Tk()
clock= Label(root,font=("times",50,"italic"),bg="gray")
clock.grid(row=0,column=1)
tick()
root.mainloop()