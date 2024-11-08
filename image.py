from tkinter import font
from tkinter import filedialog as fd

class image_input:
    def __init__(self,window,tk,ttk,os) -> None:
        #general window master class input
        self.window = window
        self.os = os
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
        self.Input_TypeMasque = '' # variable to fill
        self.Input_TypeMasqueold = '' # variable to fill
        self.Input_TypeMasque_list = ['ONE','SEQ'] # variable to fill -> valid choices
        self.Input_OneNameMasque = '' # variable to fill if type one
        self.Input_SeqDirMasque = '' # variable to fill if type seq
            # SEQ
        self.Input_SEQDirname = '' # variable to fill if type seq
        self.Input_SEQDebut = 0 # variable to fill if type seq
        self.Input_SEQinterImg = 0 # variable to fill if type seq
        self.Input_SEQinterPaire = 0 # variable to fill if type seq
            # Double
        self.Input_Imgdouble = '' # variable to fill if type dbl
            # Two
        self.Input_ImgTWO1 = '' # variable to fill if type two
        self.Input_ImgTWO2 = '' # variable to fill if type two
        # Styles 
        self.text_font = font.Font(family='Consolas',size=10) # a font for general text
        self.title_font = font.Font(family='Consolas',size=20) # a font for title texts
        self.deroulant_style = ttk.Style() # Style created for every combobox created using ttk
        self.deroulant_style.theme_use('clam')
        self.deroulant_style.configure("TCombobox", listboxbackground='gray3', fieldbackground= "gray3", background= "gray3", foreground="chartreuse2",
                                        bordercolor="chartreuse2",arrowcolor="chartreuse2",
                                        lightcolor="chartreuse2",darkcolor="gray3",focusfill="gray3",
                                        selectbackground="gray3", selectforeground="chartreuse2",Listboxforeground= 'chartreuse2', ListboxselectBackground = 'gray3',
                                        ListboxselectForeground = 'chartreuse2')
        self.deroulant_style.map("TCombobox",
              fieldbackground=[('readonly', 'gray3')],
              background=[('readonly', 'gray3')])
        

        #Global interactive items
        # ------ Note by Alexandre LM --------
        # This part of the code is used solely to define tkinter objects  to be later placed on the window
        # Here are the general object used:
        # - combobox: a box to choose a value between a list of predefined choices
        # - Entry: an open writing space for user prompt 
        # - button: a simple push button that activate something 
        # - checkbutton : a checkbox that gives back a different value if checked or not 
        # - Label: a non interactive text space
        # 
        # The long calls and general cluttered look of the code is due to the fact that we change
        # a lot of visual parameters to fit the style of the program.
        #
        # NB: The Entries and button have a white outer layer on window but a green one on linux. No clue to why
        # that is the case and I don't really have the time nor the knowledge to work around it. 
        # ------------------------------------

        self.typedata = ttk.Combobox(self.img_frame,values=self.Input_typedata_list, state='readonly') 
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
                                       background="gray3",highlightcolor="chartreuse2",highlightbackground="chartreuse2",activebackground='gray3',
                                       selectcolor='gray3',highlightthickness = 2)
        self.TypeMasque = ttk.Combobox(self.img_frame,values=self.Input_TypeMasque_list, state='readonly')
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
        # non toggleable non-interactive items
        self. Name = tk.Label(self.img_frame, text='> IMAGE')
        self.typedata_label = tk.Label(self.img_frame ,text='>> data type :')
        self.image_label = tk.Label(self.img_frame ,text='>> Image selection :')
        self.mask_label = tk.Label(self.img_frame ,text='>> Add a mask :')

    def setup(self): # a function that displays all the stuff that is not supposed to be toggled during use (titles, general indications, ...)
        #----------- Global display --------------
        # Frame
        self.img_frame.config(bg='gray3',highlightbackground='chartreuse2',highlightcolor="chartreuse2",highlightthickness=1,relief='ridge')
        self.img_frame.pack(fill='x', padx = 5, pady = 2)
        # Title
        self.Name.config(bg='gray3',fg='chartreuse2',font=self.title_font)
        self.Name.grid(column = 0, row= 0)
        #-----------------------------------------

        #---------- Choose DATATYPE --------------
        # Label
        self.typedata_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)
        self.typedata_label.grid(column = 1, row = 1, sticky = 'W')
        # choice input
        self.typedata.grid(column=2, row = 1, sticky = 'W')
        #-----------------------------------------

        #-------- Image selection ----------------
        self.image_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)
        self.image_label.grid(column = 1, row = 2, sticky = 'W')
        #-----------------------------------------

        #--------- Mask selection ----------------
        self.mask_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)
        self.mask_label.grid(column = 1, row = 8, sticky = 'W')
        self.Masque.grid(column = 2, row = 8, sticky = 'W')
        self.Masque.deselect() # option is deselected by default to avoid having a none variable
        #-----------------------------------------

    def type_choice(self): # a routine that runs every tick to see if a choice-related variable has changed
        if self.Input_typedata != self.previous_typedata and self.Input_typedata != '': # we check if a different file type has been chosen
            self.hide_all() #we hide all the type-related stuff on screen
            if self.Input_typedata == 'SEQ': # then we show only what is related to the user's choice
                self.show_seq()
            elif self.Input_typedata == 'TWO':
                self.show_two()
            elif self.Input_typedata == 'DBL':
                self.show_dbl()
            elif self.Input_typedata == 'SEQDBL':
                self.show_seqdbl()
            self.previous_typedata = self.Input_typedata
        if self.Input_Masque != self.Input_Masque_old: # we check if the user wants a mask
            if self.Input_Masque == 'OK':
                self.show_mask()
            else:
                self.hide_mask()
                self.hide_mask_one()
                self.hide_mask_seq()
                self.Input_TypeMasqueold = ''
            self.Input_Masque_old = self.Input_Masque
        if self.Input_TypeMasqueold != self.Input_TypeMasque and self.Input_Masque == 'OK': # we check if the mask type chosen has changed
            self.hide_mask_one()
            self.hide_mask_seq()
            if self.Input_TypeMasque == 'ONE':
                self.show_mask_one()
            elif self.Input_TypeMasque == 'SEQ':
                self.show_mask_seq()
            self.Input_TypeMasqueold = self.Input_TypeMasque
        
    def show_mask(self): # we show the mask choice combobox
        self.Mask_type_label.grid(column = 2, row = 9, sticky = 'W')
        self.TypeMasque.grid(column = 3, row = 9, sticky = 'W')

    def hide_mask(self): # we hide it
        self.Mask_type_label.grid_forget()
        self.TypeMasque.grid_forget()

    def show_mask_one(self): # we show the mask type one related items
        self.Mask_one_label.grid(column = 3, row = 10, sticky = 'W')
        self.OneNameMasque.grid(column = 4, row = 10, sticky = 'W')
        self.get_OneNameMasque.grid(column = 5, row = 10, sticky = 'W')
    
    def hide_mask_one(self): # we hide them
        self.Mask_one_label.grid_forget()
        self.OneNameMasque.grid_forget()
        self.get_OneNameMasque.grid_forget()

    def show_mask_seq(self): # we show the mask type seq related items
        self.Mask_seq_label.grid(column = 3, row = 10, sticky = 'W')
        self.SeqDirMasque.grid(column = 4, row = 10, sticky = 'W')
        self.get_SeqDirMasque.grid(column = 5, row = 10, sticky = 'W')
    
    def hide_mask_seq(self): # we hide them
        self.Mask_seq_label.grid_forget()
        self.SeqDirMasque.grid_forget()
        self.get_SeqDirMasque.grid_forget()
    
    def path_choice(self,var,item): # generic function for path choice 
        filename = fd.askopenfilename()
        var = filename
        #self.Input_SEQDirname = filename 
        item.delete(0, 'end')
        item.insert(0,filename)
        #self.SEQDirname.insert(0,filename)

    def refresh(self): #we update the stored value for the important variables
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
        ans = {}
        #Debug part
        print(self.dict_ans())
        #######
        # we first define EVERY SINGLE ERROR POSSIBLE (necessitate use case branching scenarios)
        error = [['Choose an image type',100],['Choose a valid image type',101],['Choose a path for the first image', 102],
                  ['Choose a path for the second image', 103],['Choose a path for the double image', 104],
                  ['Choose a path for the double image sequence', 105], ['Choose a path for the image sequence', 106],
                  ['Choose a value for the image sequence start', 107], ['Choose a value for the image sequence interval', 108],
                  ['Choose a value for the image sequence interval between pairs', 109],['Choose an integer value for the image sequence start', 110],
                  ['Choose an integer value for the image sequence interval', 111], ['Choose an integer value for the image sequence interval between pairs', 112],
                  ['Choose a mask type', 113], ['Choose a valid mask type', 114], ['Choose a path for the singular mask', 115], 
                  ['Choose a path for the sequence mask', 116],['Images inputs have been validated ',0], ['Choose an existing path for the first image', 117],
                  ['Choose an existing path for the second image', 118], ['Choose an existing path for the double image', 119],
                  ['Choose an existing path for the double image sequence', 120], ['Choose an existing path for the image sequence', 121],
                  ['Choose an existing path for the singular mask', 122], ['Choose an existing path for the sequence mask', 123]
        ]
        # the we check every error, one by one, stopping at the first error
        # The error vector value call match the error code defined in the vector above
        if not self.Input_typedata:
            return error[0], False, ans
        elif not self.Input_typedata in self.Input_typedata_list:
            return error[1], False, ans
        elif self.Input_typedata == 'TWO':
            if not self.Input_ImgTWO1:
                return error[2], False, ans
            elif not self.os.path.exists(self.Input_ImgTWO1):
                return error[18], False, ans
            elif not self.Input_ImgTWO2:
                return error[3], False, ans
            elif not self.os.path.exists(self.Input_ImgTWO2):
                return error[19], False, ans
        elif self.Input_typedata == 'DBL':
            if not self.Input_Imgdouble:
                return error[4], False, ans
            elif not self.os.path.exists(self.Input_Imgdouble):
                return error[20], False, ans
        elif self.Input_typedata == 'SEQDBL':
            if not self.Input_SEQDirname:
                return error[5], False, ans
            elif not self.os.path.exists(self.Input_SEQDirname):
                return error[21], False, ans
        elif self.Input_typedata == 'SEQ':
            if not self.Input_SEQDirname:
                    return error[6], False, ans
            elif not self.os.path.exists(self.Input_SEQDirname):
                return error[22], False, ans
            elif not self.Input_SEQDebut:
                return error[7], False, ans
            elif not self.Input_SEQinterImg:
                return error[8], False, ans
            elif not self.Input_SEQinterPaire:
                return error[9], False, ans
            else:
                if not self.Input_SEQDebut.isdigit():
                    return error[10], False, ans
                elif not self.Input_SEQinterImg.isdigit():
                    return error[11], False, ans
                elif not self.Input_SEQinterPaire.isdigit():
                    return error[12], False, ans
        if self.Input_Masque == 'OK':
            if not self.Input_TypeMasque:
                return error[13], False, ans
            elif not self.Input_TypeMasque in self.Input_TypeMasque_list:
                return error[14], False, ans
            elif self.Input_TypeMasque == 'ONE':
                if not self.Input_OneNameMasque:
                    return error[15], False, ans
                elif not self.os.path.exists(self.Input_OneNameMasque):
                    return error[23], False, ans   
            elif self.Input_TypeMasque == 'DBL':
                if not self.Input_SeqDirMasque:
                    return error[16], False, ans
                elif not self.os.path.exists(self.Input_SeqDirMasque):
                    return error[24], False, ans
        # if the program hasn't stopped on any error, that means the answer given is valid, hence the validation signal
        return error[17], True, self.dict_ans()
     
    def dict_ans(self): # creation of the answer dict to be used for the input file validation
        ans = {}
        ans['Input_typedata'] = self.Input_typedata
        if self.Input_typedata == 'TWO':
            ans['Input_ImgTWO1'] = self.Input_ImgTWO1
            ans['Input_ImgTWO2'] = self.Input_ImgTWO2
        elif self.Input_typedata == 'DBL':
            ans['Input_Imgdouble'] = self.Input_Imgdouble
        elif self.Input_typedata == 'SEQDBL':
            ans['Input_SEQDirname'] = self.Input_SEQDirname
        elif self.Input_typedata == 'SEQ':
            ans['Input_SEQDirname'] = self.Input_SEQDirname
            ans['Input_SEQDebut'] = self.Input_SEQDebut
            ans['Input_SEQinterImg'] = self.Input_SEQinterImg
            ans['Input_SEQinterPaire'] = self.Input_SEQinterPaire
        ans['Input_Masque'] = self.Input_Masque
        if self.Input_Masque == 'OK':
            ans['Input_TypeMasque'] = self.Input_TypeMasque
            if self.Input_TypeMasque == 'ONE':
                ans['Input_OneNameMasque'] = self.Input_OneNameMasque
            elif self.Input_TypeMasque == 'SEQ':
                ans['Input_SeqDirMasque'] = self.Input_SeqDirMasque
        return ans
    
    def hide_all(self): # a general function used to hide everything related to the image type selection 
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

    def show_seq(self): # we show everything related to the seq image type
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

    def show_two(self): # we show everything related to the two image type
        #labels
        self.two_label_Img1.grid(column = 2, row = 3, sticky = 'W')
        self.two_label_Img2.grid(column = 2, row = 4, sticky = 'W')
        #entries
        self.ImgTWO1.grid(column = 3, row = 3, sticky = 'W')
        self.ImgTWO2.grid(column = 3, row = 4, sticky = 'W')
        #Buttons
        self.get_ImgTWO1.grid(column = 4, row = 3, sticky = 'W')
        self.get_ImgTWO2.grid(column = 4, row = 4, sticky = 'W')

    def show_dbl(self):  # we show everything related to the dbl image type
        #label 
        self.DBL_label_path.grid(column = 2, row = 3, sticky = 'W')
        #entry
        self.Imgdouble.grid(column = 3, row = 3, sticky = 'W')
        #Button
        self.get_Imgdouble.grid(column = 4, row = 3, sticky = 'W')

    def show_seqdbl(self):  # we show everything related to the seqdbl image type
        #path label
        self.seq_data_label_path.grid(column = 2, row = 3, sticky = 'W')
        #entry
        self.SEQDirname.grid(column = 3, row = 3, sticky = 'W')
        #button
        self.get_SEQdir.grid(column = 4, row = 3, sticky = 'W')