import tkinter as tk
from tkinter import ttk, font
from tkinter import filedialog as fd
from image import image_input
from calcul import calcul_input
import sys
import os
import re

# from ttkthemes import ThemedTk

class PIV_UI :
    def __init__(self) -> None:
        #self.window = ThemedTk(theme='radiance')
        self.window = tk.Tk()
        self.window.title("UI Calcul PIV")
        self.window.geometry('900x1000')
        self.window.configure(bg='gray3')
        self.window.protocol("WM_DELETE_WINDOW", self.closing)
        self.window.option_add('*TCombobox*Listbox.background', 'gray3')
        self.window.option_add('*TCombobox*Listbox.foreground', 'chartreuse2')
        self.window.option_add('*TCombobox*Listbox.selectBackground', 'gray3')
        self.window.option_add('*TCombobox*Listbox.selectForeground', 'chartreuse2')
        self.text_font = font.Font(font='Consolas',size=10)
        self.title_font = font.Font(family='Consolas',size=20)
        self.main_display()
        self.image = image_input(self.window,tk,ttk,os)
        self.calcul = calcul_input(self.window,tk,ttk,os,font)
        self.action = action_input(self.window,tk,ttk,os)
        self.side_thread = ''
        self.start()


    def start(self):
        self.image.setup()
        self.calcul.setup()
        self.action.setup()
        self.main_loop()
        self.window.mainloop()

    def closing(self):
        self.window.destroy
        sys.exit()

    def main_display(self):
        # Logo Frame
        Prez_frame = tk.Frame(self.window)
        Prez_frame.config(bg='gray3',highlightbackground='chartreuse2',highlightcolor="chartreuse2",highlightthickness=3,relief='sunken')
        Prez_frame.pack(fill='x', padx = 5, pady = 2)
        # Logo/Title
        ascii_art = """

        ██████╗ ██╗██╗   ██╗     ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗     
        ██╔══██╗██║██║   ██║    ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     
        ██████╔╝██║██║   ██║    ██║     ███████║██║     ██║     ██║   ██║██║     
        ██╔═══╝ ██║╚██╗ ██╔╝    ██║     ██╔══██║██║     ██║     ██║   ██║██║     
        ██║     ██║ ╚████╔╝     ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗
        ╚═╝     ╚═╝  ╚═══╝       ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝
                                                                                

        """
        title = tk.Label(Prez_frame, text=ascii_art, font=("Courier", 7), bg='gray3', fg='chartreuse2', justify='left')
        title.config(bg='gray3',fg='chartreuse2')
        title.pack()

    def refresh_window(self):
        self.image.refresh()
        self.image.type_choice()
        self.calcul.refresh()
        self.calcul.choice()

    def main_loop(self):
        self.window.after(100,self.refresh_window)
        self.window.after(100,self.main_loop)
        self.window.update()


class action_input:
    def __init__(self,window,tk,ttk,os) -> None:
        self.window = window
        self.os = os
        self.text_font = font.Font(family='Consolas',size=10)
        self.title_font = font.Font(family='Consolas',size=20)
        self.act_frame = tk.Frame(self.window)
        self.Name = tk.Label(self.act_frame, text='> ACTION')

    def setup(self):
        self.act_frame.config(bg='gray3',highlightbackground='chartreuse2',highlightcolor="chartreuse2",highlightthickness=1,relief='ridge')
        self.act_frame.pack(fill='x', padx = 5, pady = 2)

        self.Name.config(bg='gray3',fg='chartreuse2',font=self.title_font)
        self.Name.grid(column = 0, row= 0)

UI = PIV_UI()
UI.start()
