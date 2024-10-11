import tkinter as tk
from tkinter import ttk, font
from tkinter import filedialog as fd
from bin.image import image_input
import sys

class PIV_UI : 
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("UI Calcul PIV")
        self.window.geometry('900x1000')
        self.window.configure(bg='gray3') 
        self.window.protocol("WM_DELETE_WINDOW", self.closing)
        self.text_font = font.Font(family='Consolas',size=10)
        self.title_font = font.Font(family='Consolas',size=20)
        self.main_display()
        self.image = image_input(self.window,tk)
        self.calcul = calcul_input(self.window,tk)
        self.action = action_input(self.window,tk)
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
        title = tk.Label(Prez_frame, text="PIV calcul \n(LOGO à mettre ici)", font=self.title_font)
        title.config(bg='gray3',fg='chartreuse2')
        title.pack(side='top', pady = 2)

    def refresh_window(self):
        self.image.refresh()
        self.image.type_choice()

    def main_loop(self):
        self.window.after(100,self.refresh_window)
        self.window.after(100,self.main_loop)
        self.window.update()

class calcul_input:
    def __init__(self,window,tk) -> None:
        #Global frame and window
        self.window = window
        self.calc_frame = tk.Frame(self.window)
        #fonts 
        self.text_font = font.Font(family='Consolas',size=10)
        self.title_font = font.Font(family='Consolas',size=20)
        #Variables
        self.CalculCPIV_meths = '' 
        #global interactive items

        #Toggleable non-interactive items

        #Non-toggleable non-interactive items
        self.Name = tk.Label(self.calc_frame, text='> CALCUL')

    def setup(self):
        #setup the frame
        self.calc_frame.config(bg='gray3',highlightbackground='chartreuse2',highlightcolor="chartreuse2",highlightthickness=1,relief='ridge')
        self.calc_frame.pack(fill='x', padx = 5, pady = 2)
        # put the name of the frame
        self.Name.config(bg='gray3',fg='chartreuse2',font=self.title_font)
        self.Name.grid(column = 0, row= 0)

    def refresh(self):
        pass

class action_input:
    def __init__(self,window,tk) -> None:
        self.window = window
        self.text_font = font.Font(family='Consolas',size=10)
        self.title_font = font.Font(family='Consolas',size=20)
        self.act_frame = tk.Frame(self.window)
        self.Name = tk.Label(self.act_frame, text='> ACTION')

    def setup(self):
        self.act_frame.config(bg='gray3',highlightbackground='chartreuse2',highlightcolor="chartreuse2",highlightthickness=1,relief='ridge')
        self.act_frame.pack(fill='x', padx = 5, pady = 2)

        self.Name.config(bg='gray3',fg='chartreuse2',font=self.title_font)
        self.Name.grid(column = 0, row= 0)

    def refresh(self):
        pass



UI = PIV_UI()
UI.start()

