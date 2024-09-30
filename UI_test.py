import tkinter as tk
from tkinter import ttk, font
import threading as th

class PIV_UI : 
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.text_font = font.Font(family='Consolas',size=10)
        self.title_font = font.Font(family='Consolas',size=20)
        self.image = image_input(self.window)
        self.calcul = calcul_input()
        self.action = action_input()

    def start(self):

        self.window.title("UI Calcul PIV")
        self.window.geometry('700x1000')
        self.window.configure(bg='gray3')
        
        self.main_display()
        self.image.setup()
        self.calcul_frame_disp()
        self.action_frame_disp()

        self.main_loop()

    def main_display(self):
        # Logo Frame
        Prez_frame = tk.Frame(self.window)
        Prez_frame.config(bg='gray3',highlightbackground='chartreuse2',highlightcolor="chartreuse2",highlightthickness=3,relief='sunken')
        Prez_frame.pack(fill='x', padx = 5, pady = 2)
        # Logo/Title
        title = tk.Label(Prez_frame, text="PIV calcul \n(LOGO à mettre ici)", font=self.title_font)
        title.config(bg='gray3',fg='chartreuse2')
        title.pack(side='top', pady = 2)

    def calcul_frame_disp(self):
        calc_frame = tk.Frame(self.window)
        calc_frame.config(bg='gray3',highlightbackground='chartreuse2',highlightcolor="chartreuse2",highlightthickness=1,relief='ridge')
        calc_frame.pack(fill='x', padx = 5, pady = 2)

        Name = tk.Label(calc_frame, text='> CALCUL')
        Name.config(bg='gray3',fg='chartreuse2',font=self.title_font)
        Name.grid(column = 0, row= 0)
        self.calcul.setup()


    def action_frame_disp(self):
        act_frame = tk.Frame(self.window)
        act_frame.config(bg='gray3',highlightbackground='chartreuse2',highlightcolor="chartreuse2",highlightthickness=1,relief='ridge')
        act_frame.pack(fill='x', padx = 5, pady = 2)

        Name = tk.Label(act_frame, text='> ACTION')
        Name.config(bg='gray3',fg='chartreuse2',font=self.title_font)
        Name.grid(column = 0, row= 0)
        self.action.setup()

    def refresh_window(self):
        self.image.sequence_choice()

    def main_loop(self):
        self.window.after(1,th.Thread(target=self.refresh_window))
        self.window.mainloop()

class image_input:
    def __init__(self,window) -> None:
        #general window master class input
        self.window = window
        #general frame
        self.img_frame = tk.Frame(self.window)
        #Variables
        self.Input_typedata = ''
        self.Input_SEQDirname = ''
        self.Input_Imgdouble = ''
        self.Input_TWO1 = ''
        self.Input_TWO2 = ''
        #Global interactive items
        self.Input_typedata_list = ['TWO','DBL','SEQDBL','SEQ']
        self.typedata = ttk.Combobox(self.img_frame,values=self.Input_typedata_list,)
        self.SEQDirname = tk.Entry(self.img_frame)
        #toggleable non-interactive items

        # Styles 
        self.text_font = font.Font(family='Consolas',size=10)
        self.title_font = font.Font(family='Consolas',size=20)
        self.deroulant_style = ttk.Style()
        self.deroulant_style.theme_use('clam')
        self.deroulant_style.configure("TCombobox", fieldbackground= "gray3", background= "gray3", foreground="chartreuse2",
                                        bordercolor="chartreuse2",arrowcolor="chartreuse2",
                                        lightcolor="chartreuse2",darkcolor="gray3",focusfill="gray3",
                                        selectbackground="gray3", selectforeground="chartreuse2")
        self.entry_style = ttk.Style()

    def setup(self):
        #----------- Global display --------------
        # Frame
        self.img_frame.config(bg='gray3',highlightbackground='chartreuse2',highlightcolor="chartreuse2",highlightthickness=1,relief='ridge')
        self.img_frame.pack(fill='x', padx = 5, pady = 2)
        # Title
        Name = tk.Label(self.img_frame, text='> IMAGE')
        Name.config(bg='gray3',fg='chartreuse2',font=self.title_font)
        Name.grid(column = 0, row= 0)
        #-----------------------------------------

        #---------- Choose DATATYPE --------------
        # Label
        typedata_label = tk.Label(self.img_frame ,text='>> data type :')
        typedata_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)
        typedata_label.grid(column = 1, row = 1, sticky = 'W')
        # choice input
        self.typedata.grid(column=2, row = 1, sticky = 'W')
        #-----------------------------------------

        #-------- Image selection ----------------
        typedata_label = tk.Label(self.img_frame ,text='>> Image selection :')
        typedata_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)
        typedata_label.grid(column = 1, row = 2, sticky = 'W')
        #-------- IF SEQ -> seq properties -------
        #path label
        seq_data_label = tk.Label(self.img_frame ,text='>>> Sequence path :')
        seq_data_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)
        seq_data_label.grid(column = 2, row = 3, sticky = 'W')
        #path selection
        self.SEQDirname.bind('<1>',self.path_choice(self.SEQDirname))
        self.SEQDirname.grid(column = 3, row = 3, sticky = 'W')
        #global Label data
        seq_data_label = tk.Label(self.img_frame ,text='>>> sequence info :')
        seq_data_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)
        seq_data_label.grid(column = 2, row = 4, sticky = 'W')
        #local label
        seq_data_label = tk.Label(self.img_frame ,text='>>>> début :')
        seq_data_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)
        seq_data_label.grid(column = 3, row = 5, sticky = 'W')
        seq_data_label = tk.Label(self.img_frame ,text='>>>> inter image :')
        seq_data_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)
        seq_data_label.grid(column = 3, row = 6, sticky = 'W')

    def sequence_choice(self):
        pass
    
    def path_choice(self,item):
        print('yo le fraté')

    def refresh(self):
        self.Input_typedata = self.typedata.get()
        self

class calcul_input:
    def __init__(self) -> None:
        pass

    def setup(self):
        pass

    def refresh(self):
        pass

class action_input:
    def __init__(self) -> None:
        pass

    def setup(self):
        pass

    def refresh(self):
        pass



UI = PIV_UI()
UI.start()

