import tkinter as tk
from tkinter import ttk, font
import threading as th
from tkinter import filedialog as fd

class PIV_UI : 
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.text_font = font.Font(family='Consolas',size=10)
        self.title_font = font.Font(family='Consolas',size=20)
        self.image = image_input(self.window)
        self.calcul = calcul_input()
        self.action = action_input()
        self.side_thread = ''

    def start(self):

        self.window.title("UI Calcul PIV")
        self.window.geometry('800x1000')
        self.window.configure(bg='gray3')
        
        self.main_display()
        self.image.setup()
        self.calcul_frame_disp()
        self.action_frame_disp()

        self.main_loop()
        self.window.mainloop()

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
        self.image.refresh()
        self.image.type_choice()

    def main_loop(self):
        self.window.after(100,self.refresh_window)
        self.window.after(100,self.main_loop)
        self.window.update()

class image_input:
    def __init__(self,window) -> None:
        #general window master class input
        self.window = window
        #general frame
        self.img_frame = tk.Frame(self.window)
        #Variables
        self.Input_typedata = ''
        self.previous_typedata = ''
            # SEQ
        self.Input_SEQDirname = ''
        self.Input_SEQDebut = 0
        self.Input_SEQinterImg = 0
        self.Input_SEQinterPaire = 0
            # Double
        self.Input_Imgdouble = ''
            # Two
        self.Input_TWO1 = ''
        self.Input_TWO2 = ''
        # Styles 
        self.text_font = font.Font(family='Consolas',size=10)
        self.title_font = font.Font(family='Consolas',size=20)
        self.deroulant_style = ttk.Style()
        self.deroulant_style.theme_use('clam')
        self.deroulant_style.configure("TCombobox", fieldbackground= "gray3", background= "gray3", foreground="chartreuse2",
                                        bordercolor="chartreuse2",arrowcolor="chartreuse2",
                                        lightcolor="chartreuse2",darkcolor="gray3",focusfill="gray3",
                                        selectbackground="gray3", selectforeground="chartreuse2")

        #Global interactive items
        self.Input_typedata_list = ['TWO','DBL','SEQDBL','SEQ']
        self.typedata = ttk.Combobox(self.img_frame,values=self.Input_typedata_list)
            # SEQ
        self.SEQDirname = tk.Entry(self.img_frame,foreground="chartreuse2",background="gray3",
                                   highlightcolor="chartreuse2",highlightbackground="chartreuse2",insertbackground="chartreuse2",font=self.text_font,width=23)
        self.get_SEQdir = tk.Button(self.img_frame,text="🗎",command = self.path_choiceSEQ,
                                    foreground="chartreuse2",background="gray3",highlightcolor="chartreuse2",highlightbackground="chartreuse2")
        self.SEQDebut = tk.Entry(self.img_frame,foreground="chartreuse2",background="gray3",
                                   highlightcolor="chartreuse2",highlightbackground="chartreuse2",insertbackground="chartreuse2",font=self.text_font,width=6)
        self.SEQinterImg = tk.Entry(self.img_frame,foreground="chartreuse2",background="gray3",
                                   highlightcolor="chartreuse2",highlightbackground="chartreuse2",insertbackground="chartreuse2",font=self.text_font,width=6)
        self.SEQinterDouble = tk.Entry(self.img_frame,foreground="chartreuse2",background="gray3",
                                   highlightcolor="chartreuse2",highlightbackground="chartreuse2",insertbackground="chartreuse2",font=self.text_font,width=6)
        #DOUBLE

        #toggleable non-interactive items
            #SEQ
        self.seq_data_label_path = tk.Label(self.img_frame ,text='>>> Sequence path :')
        self.seq_data_label_path.config(bg='gray3',fg='chartreuse2',font=self.text_font)

        self.seq_data_label_seq = tk.Label(self.img_frame ,text='>>> sequence info :')
        self.seq_data_label_seq.config(bg='gray3',fg='chartreuse2',font=self.text_font)

        self.seq_data_label_deb = tk.Label(self.img_frame ,text='>>>> début :')
        self.seq_data_label_deb.config(bg='gray3',fg='chartreuse2',font=self.text_font)

        self.seq_data_label_inter = tk.Label(self.img_frame ,text='>>>> inter image :')
        self.seq_data_label_inter.config(bg='gray3',fg='chartreuse2',font=self.text_font)

        self.seq_data_label_doub = tk.Label(self.img_frame ,text='>>>> inter double :')
        self.seq_data_label_doub.config(bg='gray3',fg='chartreuse2',font=self.text_font)


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
        
        # ---------SEQ option SETUP----------
        self.show_seq()
        # -----------------------------------
        self.hide_all()

    def type_choice(self):
        if self.Input_typedata != self.previous_typedata and self.Input_typedata != '':
            self.hide_all()
            if self.Input_typedata == 'SEQ':
                self.show_seq()
            self.previous_typedata = self.Input_typedata
    
    def path_choiceSEQ(self):
        filename = fd.askopenfilename()
        self.Input_SEQDirname = filename
        self.SEQDirname.insert(0,filename)

    def refresh(self):
        # Get type
        self.Input_typedata = self.typedata.get()
        # Get SEQ related
        self.Input_SEQDirname = self.SEQDirname.get()
        self.Input_SEQDebut = self.SEQDebut.get()
        self.Input_SEQinterImg = self.SEQinterImg.get()
        self.Input_SEQinterPaire = self.SEQinterDouble.get()
    
    def entry_validation(self):
        validity = True
        error = ''
        return validity,error
    
    def hide_all(self):
        #SEQ related
        self.SEQDirname.grid_forget()
        self.get_SEQdir.grid_forget()
        self.SEQDebut.grid_forget()
        self.SEQinterImg.grid_forget()
        self.SEQinterDouble.grid_forget()
        self.seq_data_label_path.grid_forget()
        self.seq_data_label_seq.grid_forget()
        self.seq_data_label_deb.grid_forget()
        self.seq_data_label_inter.grid_forget()
        self.seq_data_label_doub.grid_forget()

    def show_seq(self):
        #path label
        self.seq_data_label_path.grid(column = 2, row = 3, sticky = 'W')
        #path selection
        self.SEQDirname.grid(column = 3, row = 3, sticky = 'W')
        self.get_SEQdir.grid(column = 4, row = 3)
        #global Label data
        self.seq_data_label_seq.grid(column = 2, row = 4, sticky = 'W')
        #local label
        self.seq_data_label_deb.grid(column = 3, row = 5, sticky = 'W')
        self.seq_data_label_inter.grid(column = 3, row = 6, sticky = 'W')
        self.seq_data_label_doub.grid(column = 3, row = 7, sticky = 'W')
        #value entry
        self.SEQDebut.grid(column = 4, row = 5, sticky = 'W')
        self.SEQinterImg.grid(column = 4, row = 6, sticky = 'W')
        self.SEQinterDouble.grid(column = 4, row = 7, sticky = 'W')


        

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

