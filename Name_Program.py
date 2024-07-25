import tkinter as tk
from tkinter import ttk
from tkinter import *
import random
class window_one:
    def __init__(self):
        Button(main_window,height=2, width=8, text="Quit",command = self.quit).grid(row=1, column =1,pady=0, padx = 5)
        Button(main_window,height=2, width=8, text="Play",command = self.Difficulty).grid(row=1, column= 2,pady=0, padx = 5)
        Difficulty_combobox = ttk.Combobox(main_window , values = ["Easy", "Medium", "Hard"],textvariable=combobox_value).grid(row = 1, column = 3, padx=5 ,columnspan = 2)
    def Difficulty(self):
        print(combobox_value.get())
        if combobox_value.get() == "Easy":
            self.EasyWindow()
        elif combobox_value.get() == "Medium":
            print("Mediump")             
        elif combobox_value.get() == "Hard":
            print("Hardp")
        else:
            print("Else")

            
    def quit(self):
        main_window.destroy()
        
    class EasyWindow(Toplevel):
        def __init__(self):
            canvas.delete('all')
            
            
        
def hangman_avatar():
    canvas.create_rectangle(300,90, 200,100, fill= '#c47a3d', outline ='black',width= 1)
    canvas.create_rectangle(300,90, 290,250, fill= '#c47a3d', outline ='black',width= 1)
    canvas.create_oval(310,110, 280,80, fill= '#c47a3d', outline ='black',width= 1)
    canvas.create_rectangle(320,250, 260,265, fill= '#c47a3d', outline ='black',width= 1)
    canvas.update()

main_window = Tk()
combobox_value=StringVar()
window = tk.Tk()
main_window.title("Main Window")
main_window.geometry("325x365")
#Making Canvas
canvas = Canvas(main_window, width = 320, height = 320, bg = 'gray94')
canvas.grid(row = 2, column = 1, rowspan = 2, columnspan = 3)
#Welcome text
canvas.create_text(170,30,fill="darkblue",font="Times 25 italic bold",text="Hangman")
hangman_avatar()
#Start of Code
window_one()
