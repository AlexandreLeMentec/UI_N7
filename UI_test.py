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
        self.window.geometry('900x1000')
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
        self.Input_typedata_list = ['TWO','DBL','SEQDBL','SEQ']
        #Variables
            #General Frame
        self.Input_typedata = ''
        self.previous_typedata = '' # to check if the variable changed
            #Mask 
        self.Input_Masque = 'NO'
        self.Input_Masque_old = 'NO' # to check if the variable changed
        self.varMasque = tk.StringVar() # variable buffer for the checkbox
        self.Input_TypeMasque = ''
        self.Input_TypeMasqueold = ''
        self.Input_TypeMasque_list = ['ONE','SEQ']
        self.Input_OneNameMasque = ''
        self.Input_SeqDirMasque = ''
            # SEQ
        self.Input_SEQDirname = ''
        self.Input_SEQDebut = 0
        self.Input_SEQinterImg = 0
        self.Input_SEQinterPaire = 0
            # Double
        self.Input_Imgdouble = ''
            # Two
        self.Input_ImgTWO1 = ''
        self.Input_ImgTWO2 = ''
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
        self.typedata = ttk.Combobox(self.img_frame,values=self.Input_typedata_list)
            # SEQ
        self.SEQDirname = tk.Entry(self.img_frame,foreground="chartreuse2",background="gray3",
                                   highlightcolor="chartreuse2",highlightbackground="chartreuse2",insertbackground="chartreuse2",font=self.text_font,width=23)
        self.get_SEQdir = tk.Button(self.img_frame,text="🗎",command = lambda: self.path_choice(self.Input_SEQDirname, self.SEQDirname),
                                    foreground="chartreuse2",background="gray3",highlightcolor="chartreuse2",highlightbackground="chartreuse2")
        self.SEQDebut = tk.Entry(self.img_frame,foreground="chartreuse2",background="gray3",
                                   highlightcolor="chartreuse2",highlightbackground="chartreuse2",insertbackground="chartreuse2",font=self.text_font,width=6)
        self.SEQinterImg = tk.Entry(self.img_frame,foreground="chartreuse2",background="gray3",
                                   highlightcolor="chartreuse2",highlightbackground="chartreuse2",insertbackground="chartreuse2",font=self.text_font,width=6)
        self.SEQinterDouble = tk.Entry(self.img_frame,foreground="chartreuse2",background="gray3",
                                   highlightcolor="chartreuse2",highlightbackground="chartreuse2",insertbackground="chartreuse2",font=self.text_font,width=6)
            #TWO
        self.ImgTWO1 = tk.Entry(self.img_frame,foreground="chartreuse2",background="gray3",
                                   highlightcolor="chartreuse2",highlightbackground="chartreuse2",insertbackground="chartreuse2",font=self.text_font,width=23)
        self.ImgTWO2 = tk.Entry(self.img_frame,foreground="chartreuse2",background="gray3",
                                   highlightcolor="chartreuse2",highlightbackground="chartreuse2",insertbackground="chartreuse2",font=self.text_font,width=23)
        self.get_ImgTWO1 = tk.Button(self.img_frame,text="🗎",command = lambda: self.path_choice(self.Input_ImgTWO1, self.ImgTWO1),
                                    foreground="chartreuse2",background="gray3",highlightcolor="chartreuse2",highlightbackground="chartreuse2")
        self.get_ImgTWO2 = tk.Button(self.img_frame,text="🗎",command = lambda: self.path_choice(self.Input_ImgTWO2, self.ImgTWO2),
                                    foreground="chartreuse2",background="gray3",highlightcolor="chartreuse2",highlightbackground="chartreuse2")
            #DBL
        self.Imgdouble = tk.Entry(self.img_frame,foreground="chartreuse2",background="gray3",
                                   highlightcolor="chartreuse2",highlightbackground="chartreuse2",insertbackground="chartreuse2",font=self.text_font,width=23)
        self.get_Imgdouble = tk.Button(self.img_frame,text="🗎",command = lambda: self.path_choice(self.Input_Imgdouble, self.Imgdouble),
                                    foreground="chartreuse2",background="gray3",highlightcolor="chartreuse2",highlightbackground="chartreuse2")
            #MASK
        self.Masque = tk.Checkbutton(self.img_frame, onvalue='OK', offvalue='NO', variable=self.varMasque,foreground="chartreuse2",
                                       background="gray3",highlightcolor="chartreuse2",highlightbackground="chartreuse2")
        self.TypeMasque = ttk.Combobox(self.img_frame,values=self.Input_TypeMasque_list)
            #MASK ONE
        self.OneNameMasque = tk.Entry(self.img_frame,foreground="chartreuse2",background="gray3",
                                        highlightcolor="chartreuse2",highlightbackground="chartreuse2",insertbackground="chartreuse2",font=self.text_font,width=23)
        self.get_OneNameMasque = tk.Button(self.img_frame,text="🗎",command = lambda: self.path_choice(self.Input_OneNameMasque, self.OneNameMasque),
                                    foreground="chartreuse2",background="gray3",highlightcolor="chartreuse2",highlightbackground="chartreuse2")
         #MASK ONE
        self.SeqDirMasque = tk.Entry(self.img_frame,foreground="chartreuse2",background="gray3",
                                        highlightcolor="chartreuse2",highlightbackground="chartreuse2",insertbackground="chartreuse2",font=self.text_font,width=23)
        self.get_SeqDirMasque = tk.Button(self.img_frame,text="🗎",command = lambda: self.path_choice(self.Input_SeqDirMasque, self.SeqDirMasque),
                                    foreground="chartreuse2",background="gray3",highlightcolor="chartreuse2",highlightbackground="chartreuse2")

        #toggleable non-interactive items

        #toggleable non-interactive items
            #SEQ
        self.seq_data_label_path = tk.Label(self.img_frame ,text='>>> Sequence path :')
        self.seq_data_label_path.config(bg='gray3',fg='chartreuse2',font=self.text_font)

        self.seq_data_label_seq = tk.Label(self.img_frame ,text='>>> sequence info :')
        self.seq_data_label_seq.config(bg='gray3',fg='chartreuse2',font=self.text_font)

        self.seq_data_label_deb = tk.Label(self.img_frame ,text='>>>> Start :')
        self.seq_data_label_deb.config(bg='gray3',fg='chartreuse2',font=self.text_font)

        self.seq_data_label_inter = tk.Label(self.img_frame ,text='>>>> inter image :')
        self.seq_data_label_inter.config(bg='gray3',fg='chartreuse2',font=self.text_font)

        self.seq_data_label_doub = tk.Label(self.img_frame ,text='>>>> inter pairs :')
        self.seq_data_label_doub.config(bg='gray3',fg='chartreuse2',font=self.text_font)

            #TWO
        self.two_label_Img1 = tk.Label(self.img_frame ,text='>>> Path Image 1:')
        self.two_label_Img1.config(bg='gray3',fg='chartreuse2',font=self.text_font)

        self.two_label_Img2 = tk.Label(self.img_frame ,text='>>> Path Image 2:')
        self.two_label_Img2.config(bg='gray3',fg='chartreuse2',font=self.text_font)
            #DBL
        self.DBL_label_path = tk.Label(self.img_frame ,text='>>> Path Image double:')
        self.DBL_label_path.config(bg='gray3',fg='chartreuse2',font=self.text_font)
            #MASK
        self.Mask_type_label = tk.Label(self.img_frame ,text='>>> Mask type')
        self.Mask_type_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)
            #MASK ONE
        self.Mask_one_label = tk.Label(self.img_frame ,text='>>>> Path mask :')
        self.Mask_one_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)
            #MASK SEQ
        self.Mask_seq_label = tk.Label(self.img_frame ,text='>>>> Path mask sequence :')
        self.Mask_seq_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)


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
        image_label = tk.Label(self.img_frame ,text='>> Image selection :')
        image_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)
        image_label.grid(column = 1, row = 2, sticky = 'W')
        #-----------------------------------------


        #--------- Mask selection ----------------
        mask_label = tk.Label(self.img_frame ,text='>> Add a mask :')
        mask_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)
        mask_label.grid(column = 1, row = 8, sticky = 'W')
        self.Masque.grid(column = 2, row = 8, sticky = 'W')
        self.Masque.deselect() # option is deselected by default to avoid having a none variable
        #-----------------------------------------

    def type_choice(self): # a routine that runs every tick to see if a choice-related variable has changed
        if self.Input_typedata != self.previous_typedata and self.Input_typedata != '':
            self.hide_all()
            if self.Input_typedata == 'SEQ':
                self.show_seq()
            elif self.Input_typedata == 'TWO':
                self.show_two()
            elif self.Input_typedata == 'DBL':
                self.show_dbl()
            elif self.Input_typedata == 'SEQDBL':
                self.show_seqdbl()
            self.previous_typedata = self.Input_typedata
        if self.Input_Masque != self.Input_Masque_old:
            if self.Input_Masque == 'OK':
                self.show_mask()
            else:
                self.hide_mask()
                self.hide_mask_one()
                self.hide_mask_seq()
                self.Input_TypeMasqueold = ''
            self.Input_Masque_old = self.Input_Masque
        if self.Input_TypeMasqueold != self.Input_TypeMasque and self.Input_Masque == 'OK':
            self.hide_mask_one()
            self.hide_mask_seq()
            if self.Input_TypeMasque == 'ONE':
                self.show_mask_one()
            elif self.Input_TypeMasque == 'SEQ':
                self.show_mask_seq()
            self.Input_TypeMasqueold = self.Input_TypeMasque
        
    def show_mask(self):
        self.Mask_type_label.grid(column = 2, row = 9, sticky = 'W')
        self.TypeMasque.grid(column = 3, row = 9, sticky = 'W')

    def hide_mask(self):
        self.Mask_type_label.grid_forget()
        self.TypeMasque.grid_forget()

    def show_mask_one(self):
        self.Mask_one_label.grid(column = 3, row = 10, sticky = 'W')
        self.OneNameMasque.grid(column = 4, row = 10, sticky = 'W')
        self.get_OneNameMasque.grid(column = 5, row = 10, sticky = 'W')
    
    def hide_mask_one(self):
        self.Mask_one_label.grid_forget()
        self.OneNameMasque.grid_forget()
        self.get_OneNameMasque.grid_forget()

    def show_mask_seq(self):
        self.Mask_seq_label.grid(column = 3, row = 10, sticky = 'W')
        self.SeqDirMasque.grid(column = 4, row = 10, sticky = 'W')
        self.get_SeqDirMasque.grid(column = 5, row = 10, sticky = 'W')
    
    def hide_mask_seq(self):
        pass
    
    def path_choice(self,var,item): # generic function for path choice 
        filename = fd.askopenfilename()
        var = filename
        #self.Input_SEQDirname = filename 
        item.insert(0,filename)
        #self.SEQDirname.insert(0,filename)

    def refresh(self):
        # Get type
        self.Input_typedata = self.typedata.get()
        # Get SEQ related
        self.Input_SEQDirname = self.SEQDirname.get()
        self.Input_SEQDebut = self.SEQDebut.get()
        self.Input_SEQinterImg = self.SEQinterImg.get()
        self.Input_SEQinterPaire = self.SEQinterDouble.get()
        # Get TWO related
        self.Input_ImgTWO1 = self.ImgTWO1.get()
        self.Input_ImgTWO2 = self.ImgTWO2.get()
        # Get DBL related
        self.Input_Imgdouble = self.Imgdouble.get()
        # Get SEQDBL related
            # using the same first variable as SEQ
        # Get Mask related
        self.Input_Masque = self.varMasque.get()
        self.Input_TypeMasque = self.TypeMasque.get()
        self.Input_OneNameMasque = self.OneNameMasque.get()
        self.Input_SeqDirMasque = self.SeqDirMasque.get()


    def entry_validation(self): #pretty ugly method to inherit a completion state and an error message, can be improved
        errors = [['Choose an image type',100],['Choose a valid image type',101],['Choose a path for the first image', 102],
                  ['Choose a path for the second image', 103],['Choose a path for the double image', 104],
                  ['Choose a path for the double image sequence', 105], ['Choose a path for the image sequence', 106],
                  ['Choose a value for the image sequence start', 107], ['Choose a value for the image sequence interval', 108],
                  ['Choose a value for the image sequence interval between pairs', 109],['Choose an integer value for the image sequence start', 110],
                  ['Choose an integer value for the image sequence interval', 111], ['Choose an integer value for the image sequence interval between pairs', 112],
                  ['Choose a mask type', 113], ['Choose a valid mask type', 114], ['Choose a path for the singular mask', 115], 
                  ['Choose a path for the sequence mask', 116],['Images inputs have been validated ',0]
        ]
        if not self.Input_typedata:
            error = errors[1]
            return error, False
        elif not self.Input_typedata in self.Input_typedata_list:
            error = errors[2]
            return error, False
        elif self.Input_typedata == 'TWO':
            if not self.Input_ImgTWO1:
                error = errors[3]
                return error, False
            elif not self.Input_ImgTWO2:
                error = errors[4]
                return error, False
        elif self.Input_typedata == 'DBL':
            if not self.Input_Imgdouble:
                error = errors[5]
                return error, False
        elif self.Input_typedata == 'SEQDBL':
            if not self.Input_SEQDirname:
                error = errors[6]
                return error, False
        elif self.Input_typedata == 'SEQ':
            if not self.Input_SEQDirname:
                    error = errors[7]
                    return error, False
            elif not self.Input_SEQDebut:
                error = errors[8]
                return error, False
            elif not self.Input_SEQinterImg:
                error = errors[9]
                return error, False
            elif not self.Input_SEQinterPaire:
                error = errors[10]
                return error, False
            else:
                try:
                    self.Input_SEQDebut = int(self.Input_SEQDebut)
                except:
                    error = errors[11]
                    return error, False
                try:
                    self.Input_SEQinterImg = int(self.Input_SEQinterImg)
                except:
                    error = errors[12]
                    return error, False
                try:
                    self.Input_SEQinterPaire = int(self.Input_SEQinterPaire)
                except:
                    error = errors[13]
                    return error, False
        if self.Input_Masque == 'OK':
            if not self.Input_TypeMasque:
                error = error[14]
                return error, False
            elif not self.Input_TypeMasque in self.Input_TypeMasque_list:
                error = error[15]
                return error, False
            elif self.Input_TypeMasque == 'ONE':
                if not self.Input_OneNameMasque:
                    error = error[16]
                    return error, False
            elif self.Input_TypeMasque == 'DBL':
                if not self.Input_SeqDirMasque:
                    error = error[17]
                    return error, False
        return errors[18], True
    
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
        #TWO related
        self.two_label_Img1.grid_forget()
        self.two_label_Img2.grid_forget()
        self.ImgTWO1.grid_forget()
        self.ImgTWO2.grid_forget()
        self.get_ImgTWO1.grid_forget()
        self.get_ImgTWO2.grid_forget()
        #DBL related
        self.DBL_label_path.grid_forget()
        self.Imgdouble.grid_forget()
        self.get_Imgdouble.grid_forget()
        #SEQDBL related
        self.SEQDirname.grid_forget()
        self.get_SEQdir.grid_forget()
        self.seq_data_label_path.grid_forget()

    def show_seq(self):
        #path label
        self.seq_data_label_path.grid(column = 2, row = 3, sticky = 'W')
        #path selection
        self.SEQDirname.grid(column = 3, row = 3, sticky = 'W')
        self.get_SEQdir.grid(column = 4, row = 3, sticky = 'W')
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

    def show_two(self):
        #labels
        self.two_label_Img1.grid(column = 2, row = 3, sticky = 'W')
        self.two_label_Img2.grid(column = 2, row = 4, sticky = 'W')
        #entries
        self.ImgTWO1.grid(column = 3, row = 3, sticky = 'W')
        self.ImgTWO2.grid(column = 3, row = 4, sticky = 'W')
        #Buttons
        self.get_ImgTWO1.grid(column = 4, row = 3, sticky = 'W')
        self.get_ImgTWO2.grid(column = 4, row = 4, sticky = 'W')

    def show_dbl(self):
        #label 
        self.DBL_label_path.grid(column = 2, row = 3, sticky = 'W')
        #entry
        self.Imgdouble.grid(column = 3, row = 3, sticky = 'W')
        #Button
        self.get_Imgdouble.grid(column = 4, row = 3, sticky = 'W')

    def show_seqdbl(self):
        #path label
        self.seq_data_label_path.grid(column = 2, row = 3, sticky = 'W')
        #entry
        self.SEQDirname.grid(column = 3, row = 3, sticky = 'W')
        #button
        self.get_SEQdir.grid(column = 4, row = 3, sticky = 'W')

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

