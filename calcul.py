import re

class calcul_input:
    def __init__(self,window,tk,ttk,os,font) -> None:
        #Global instaces, frame and window
        self.window = window
        self.calc_frame = tk.Frame(self.window)
        self.os = os
        #fonts
        self.text_font = font.Font(family='Consolas',size=10)
        self.title_font = font.Font(family='Consolas',size=20)
        #Styles
        self.deroulant_style = ttk.Style()
        self.deroulant_style.theme_use('clam')
        self.deroulant_style.configure("TCombobox", listboxbackground='gray3', fieldbackground= "gray3", background= "gray3", foreground="chartreuse2",
                                        bordercolor="chartreuse2",arrowcolor="chartreuse2",
                                        lightcolor="chartreuse2",darkcolor="gray3",focusfill="gray3",
                                        selectbackground="gray3", selectforeground="chartreuse2",Listboxforeground= 'chartreuse2', ListboxselectBackground = 'gray3',
                                        ListboxselectForeground = 'chartreuse2')
        self.deroulant_style.map("TCombobox",
              fieldbackground=[('readonly', 'gray3')],
              background=[('readonly', 'gray3')])

        #Variables
            #method choice
        self.CalculCPIV_meths = ''
        self.CalculCPIV_meths_list = ['IVDEFORM ','PIVDECAL ','PIVSIMPLE']
            #X and Y
        self.CalculCPIV_dimXYcell = ''
        self.CalculCPIV_dimX = ''
        self.CalculCPIV_dimY = ''
            # covered zone
        self.CalculCPIV_recouv = ''
        self.CalculCPIV_recouv1 = ''
        self.CalculCPIV_recouv2 = ''
            # ROI
        self.CalculCPIV_ROI = 'NO'
        self.CalculCPIV_ROI_old = 'NO'
        self.CalculCPIV_ROI_var = tk.StringVar()
        self.CalculCPIV_ROIval = ''
        self.CalculCPIV_ROIvalx0 = ''
        self.CalculCPIV_ROIvaly0 = ''
        self.CalculCPIV_ROIvalx1 = ''
        self.CalculCPIV_ROIvaly1 = ''
            #Conv tools
        self.CalculCPIV_ConvTools = 'NO'
        self.CalculCPIV_ConvTools_var = tk.StringVar()
            #Post processing filter
        self.CalculCPIV_FiltrePostCalcul = 'NO'
        self.CalculCPIV_FiltrePostCalcul_var = tk.StringVar()
            #Calculation tracking
        self.CalculCPIV_SuiviCalcul = 'NO'
        self.CalculCPIV_SuiviCalcul_old = 'NO'
        self.CalculCPIV_SuiviCalcul_var = tk.StringVar()
        self.CalculCPIV_VecX = ''
        self.CalculCPIV_VecY = ''

        #global interactive items
            # method choice
        self.choice_CalculCPIV_meths = ttk.Combobox(self.calc_frame,values=self.CalculCPIV_meths_list, state = "readonly",style='TCombobox')
            # X and Y
        self.inp_CalculCPIV_dimX = tk.Entry(self.calc_frame,foreground="chartreuse2",background="gray3",
                                   highlightcolor="chartreuse2",highlightbackground="chartreuse2",insertbackground="chartreuse2",font=self.text_font,width=9)
        self.inp_CalculCPIV_dimY = tk.Entry(self.calc_frame,foreground="chartreuse2",background="gray3",
                                   highlightcolor="chartreuse2",highlightbackground="chartreuse2",insertbackground="chartreuse2",font=self.text_font,width=9)
            # covered zone
        self.inp_CalculCPIV_recouv1 = tk.Entry(self.calc_frame,foreground="chartreuse2",background="gray3",
                                   highlightcolor="chartreuse2",highlightbackground="chartreuse2",insertbackground="chartreuse2",font=self.text_font,width=9)
        self.inp_CalculCPIV_recouv2 = tk.Entry(self.calc_frame,foreground="chartreuse2",background="gray3",
                                   highlightcolor="chartreuse2",highlightbackground="chartreuse2",insertbackground="chartreuse2",font=self.text_font,width=9)
            # ROI
        self.CalculCPIV_ROI_bool = tk.Checkbutton(self.calc_frame, onvalue='OK', offvalue='NO', variable=self.CalculCPIV_ROI_var,foreground="chartreuse2",
                                       background="gray3",highlightcolor="chartreuse2",highlightbackground="chartreuse2",activebackground='gray3',
                                       selectcolor='gray3')
        self.CalculCPIV_ROI_bool.deselect()
        self.inp_CalculCPIV_ROIvalx0 = tk.Entry(self.calc_frame,foreground="chartreuse2",background="gray3",
                                   highlightcolor="chartreuse2",highlightbackground="chartreuse2",insertbackground="chartreuse2",font=self.text_font,width=9)
        self.inp_CalculCPIV_ROIvaly0 = tk.Entry(self.calc_frame,foreground="chartreuse2",background="gray3",
                                   highlightcolor="chartreuse2",highlightbackground="chartreuse2",insertbackground="chartreuse2",font=self.text_font,width=9)
        self.inp_CalculCPIV_ROIvalx1 = tk.Entry(self.calc_frame,foreground="chartreuse2",background="gray3",
                                   highlightcolor="chartreuse2",highlightbackground="chartreuse2",insertbackground="chartreuse2",font=self.text_font,width=9)
        self.inp_CalculCPIV_ROIvaly1 = tk.Entry(self.calc_frame,foreground="chartreuse2",background="gray3",
                                   highlightcolor="chartreuse2",highlightbackground="chartreuse2",insertbackground="chartreuse2",font=self.text_font,width=9)
            # Conv tools
        self.CalculCPIV_ConvTools_bool = tk.Checkbutton(self.calc_frame, onvalue='OK', offvalue='NO', variable=self.CalculCPIV_ConvTools_var,foreground="chartreuse2",
                                       background="gray3",highlightcolor="chartreuse2",highlightbackground="chartreuse2",activebackground='gray3',
                                       selectcolor='gray3')
        self.CalculCPIV_ConvTools_bool.deselect()
            # Post Proc
        self.CalculCPIV_FiltrePostCalcul_bool = tk.Checkbutton(self.calc_frame, onvalue='OK', offvalue='NO', variable=self.CalculCPIV_FiltrePostCalcul_var,foreground="chartreuse2",
                                       background="gray3",highlightcolor="chartreuse2",highlightbackground="chartreuse2",activebackground='gray3',
                                       selectcolor='gray3')
        self.CalculCPIV_FiltrePostCalcul_bool.deselect()
            #Calculation Tracking
        self.CalculCPIV_SuiviCalcul_bool = tk.Checkbutton(self.calc_frame, onvalue='OK', offvalue='NO', variable=self.CalculCPIV_SuiviCalcul_var,foreground="chartreuse2",
                                       background="gray3",highlightcolor="chartreuse2",highlightbackground="chartreuse2",activebackground='gray3',
                                       selectcolor='gray3')
        self.CalculCPIV_SuiviCalcul_bool.deselect()
        self.CalculCPIV_VecX_inp = tk.Entry(self.calc_frame,foreground="chartreuse2",background="gray3",
                                   highlightcolor="chartreuse2",highlightbackground="chartreuse2",insertbackground="chartreuse2",font=self.text_font,width=9)
        self.CalculCPIV_VecY_inp = tk.Entry(self.calc_frame,foreground="chartreuse2",background="gray3",
                                   highlightcolor="chartreuse2",highlightbackground="chartreuse2",insertbackground="chartreuse2",font=self.text_font,width=9)

        #non-interactive items
            #global name
        self.Name = tk.Label(self.calc_frame, text='> CALCUL')
        self.Name.config(bg='gray3',fg='chartreuse2',font=self.title_font)
            # Method choice
        self.meth_choice_label = tk.Label(self.calc_frame, text='>> Chosen computing method')
        self.meth_choice_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)
            # X and Y
        self.XY_dim_label = tk.Label(self.calc_frame, text='>> X and Y size of the comp window')
        self.XY_dim_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)
        self.XY_dim_choice_label = tk.Label(self.calc_frame, text='>>> [X][Y]')
        self.XY_dim_choice_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)
            # covered zone
        self.covered_zone_label = tk.Label(self.calc_frame, text='>> covering zone parameters')
        self.covered_zone_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)
        self.coverd_zone_choice_label = tk.Label(self.calc_frame, text='>>> [1][2] floats in [0, 1[ ')
        self.coverd_zone_choice_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)
            # ROI
        self.ROI_label = tk.Label(self.calc_frame, text='>> Compute Region of Interest')
        self.ROI_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)
        self.ROI_label_xy0 = tk.Label(self.calc_frame, text='>>> [X0][Y0]')
        self.ROI_label_xy0.config(bg='gray3',fg='chartreuse2',font=self.text_font)
        self.ROI_label_xy1 = tk.Label(self.calc_frame, text='>>> [X1][Y1]')
        self.ROI_label_xy1.config(bg='gray3',fg='chartreuse2',font=self.text_font)
            # Conv_tools
        self.Conv_label = tk.Label(self.calc_frame, text='>> Convergence tools')
        self.Conv_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)
            # PostProc
        self.Postpro_label = tk.Label(self.calc_frame, text='>> Post processing')
        self.Postpro_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)
            # Calculation Tracking
        self.CalcTrack_label = tk.Label(self.calc_frame, text='>> Calculation tracking')
        self.CalcTrack_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)
        self.CalcTrackXY_label = tk.Label(self.calc_frame, text='>>> [X][Y]')
        self.CalcTrackXY_label.config(bg='gray3',fg='chartreuse2',font=self.text_font)

    def setup(self): #Here we setup the different items that are supposed to stay visible during the entierety of the use
        #setup the frame
        self.calc_frame.config(bg='gray3',highlightbackground='chartreuse2',highlightcolor="chartreuse2",highlightthickness=1,relief='ridge')
        self.calc_frame.pack(fill='x', padx = 5, pady = 2)
        # put the name of the frame
        self.Name.grid(column = 0, row= 0)
        # Method choice
        self.meth_choice_label.grid(column = 1, row= 1, sticky = 'W')
        self.choice_CalculCPIV_meths.grid(column = 2, row= 1, sticky = 'W')
        # XY choice
        self.XY_dim_label.grid(column = 1, row= 2, sticky = 'W')
        self.XY_dim_choice_label.grid(column = 2, row= 3, sticky = 'W')
        self.inp_CalculCPIV_dimX.grid(column = 3, row= 3, sticky = 'E')
        self.inp_CalculCPIV_dimY.grid(column = 4, row= 3, sticky = 'W')
        # covered zone
        self.covered_zone_label.grid(column = 1, row= 4, sticky = 'W')
        self.coverd_zone_choice_label.grid(column = 2, row= 5, sticky = 'W')
        self.inp_CalculCPIV_recouv1.grid(column = 3, row= 5, sticky = 'E')
        self.inp_CalculCPIV_recouv2.grid(column = 4, row= 5, sticky = 'W')
        # ROI
        self.ROI_label.grid(column = 1, row= 6, sticky = 'W')
        self.CalculCPIV_ROI_bool.grid(column = 2, row= 6, sticky = 'W')
        #Conv tools
        self.Conv_label.grid(column = 1, row= 9, sticky = 'W')
        self.CalculCPIV_ConvTools_bool.grid(column = 2, row= 9, sticky = 'W')
        #Postproc
        self.Postpro_label.grid(column = 1, row= 10, sticky = 'W')
        self.CalculCPIV_FiltrePostCalcul_bool.grid(column = 2, row= 10, sticky = 'W')
        # calc track
        self.CalcTrack_label.grid(column = 1, row = 11, sticky = 'W')
        self.CalculCPIV_SuiviCalcul_bool.grid(column = 2, row = 11, sticky = 'W')

    def refresh(self): # a pretty messy way to update everything, TODO: use focus related events instead 
        # method choice
        self.CalculCPIV_meths = self.choice_CalculCPIV_meths.get()
        # X Y
        self.CalculCPIV_dimY = self.inp_CalculCPIV_dimY.get()
        self.CalculCPIV_dimX = self.inp_CalculCPIV_dimX.get()
        self.CalculCPIV_dimXYcell = self.CalculCPIV_dimX + ' ' + self.CalculCPIV_dimY
        # covered zone
        self.CalculCPIV_recouv1 = self.inp_CalculCPIV_recouv1.get()
        self.CalculCPIV_recouv2 = self.inp_CalculCPIV_recouv2.get()
        self.CalculCPIV_recouv = self.CalculCPIV_recouv1 + ' ' + self.CalculCPIV_recouv2
        # ROI
        self.CalculCPIV_ROI = self.CalculCPIV_ROI_var.get()
        self.CalculCPIV_ROIvalx0 = self.inp_CalculCPIV_ROIvalx0.get()
        self.CalculCPIV_ROIvaly0 = self.inp_CalculCPIV_ROIvaly0.get()
        self.CalculCPIV_ROIvalx1 = self.inp_CalculCPIV_ROIvalx1.get()
        self.CalculCPIV_ROIvaly1 = self.inp_CalculCPIV_ROIvaly1.get()
        self.CalculCPIV_ROIval = self.CalculCPIV_ROIvalx0 + ' ' + self.CalculCPIV_ROIvaly0 + ' ' + self.CalculCPIV_ROIvalx1+ ' ' + self.CalculCPIV_ROIvaly1
        #Conv tools
        self.CalculCPIV_ConvTools = self.CalculCPIV_ConvTools_var.get()
        #Postproc
        self.CalculCPIV_FiltrePostCalcul = self.CalculCPIV_FiltrePostCalcul_var.get()
        #Comp track
        self.CalculCPIV_SuiviCalcul = self.CalculCPIV_SuiviCalcul_var.get()
        self.CalculCPIV_VecX = self.CalculCPIV_VecX_inp.get()
        self.CalculCPIV_VecY = self.CalculCPIV_VecY_inp.get()

    def choice(self): # a little background task that checks if an important value has been modified TODO: link it to only run when a value is edited (!= changed)
        if self.CalculCPIV_ROI != self.CalculCPIV_ROI_old:
            self.hide_ROI()
            if self.CalculCPIV_ROI == 'OK':
                self.show_ROI()
            self.CalculCPIV_ROI_old = self.CalculCPIV_ROI
        if self.CalculCPIV_SuiviCalcul != self.CalculCPIV_SuiviCalcul_old:
            self.hide_comp_track()
            if self.CalculCPIV_SuiviCalcul == 'OK':
                self.show_comp_track()
            self.CalculCPIV_SuiviCalcul_old = self.CalculCPIV_SuiviCalcul

    def show_ROI(self): #We show everything related to ROI 
        self.ROI_label_xy0.grid(column = 2, row= 7, sticky = 'W')
        self.ROI_label_xy1.grid(column = 2, row= 8, sticky = 'W')
        self.inp_CalculCPIV_ROIvalx0.grid(column = 3, row= 7, sticky = 'E')
        self.inp_CalculCPIV_ROIvaly0.grid(column = 4, row= 7, sticky = 'W')
        self.inp_CalculCPIV_ROIvalx1.grid(column = 3, row= 8, sticky = 'E')
        self.inp_CalculCPIV_ROIvaly1.grid(column = 4, row= 8, sticky = 'W')

    def hide_ROI(self): # we hide everything related to ROI
        self.ROI_label_xy0.grid_forget()
        self.ROI_label_xy1.grid_forget()
        self.inp_CalculCPIV_ROIvalx0.grid_forget()
        self.inp_CalculCPIV_ROIvaly0.grid_forget()
        self.inp_CalculCPIV_ROIvalx1.grid_forget()
        self.inp_CalculCPIV_ROIvaly1.grid_forget()

    def show_comp_track(self): #we show everything related to the computation tracking
        self.CalcTrackXY_label.grid(column = 2, row= 12, sticky = 'W')
        self.CalculCPIV_VecX_inp.grid(column = 3, row= 12, sticky = 'E')
        self.CalculCPIV_VecY_inp.grid(column = 4, row= 12, sticky = 'W')

    def hide_comp_track(self): #we hide everything related to the computation tracking
        self.CalcTrackXY_label.grid_forget()
        self.CalculCPIV_VecX_inp.grid_forget()
        self.CalculCPIV_VecY_inp.grid_forget()

    def entry_validation(self): # same thing as for the image class: we check every possible error
        # an error is organised as follow: an error message and an error code, the latter being a bit irrelevant here but 
        # which become a lot more important in bigger projects.
        error = [
            ['Choose a computing method', 200], ['choose the x size of the computing window', 201],
            ['Choose the y size of the computing window', 202], ['Choose an integer value for the x size of the computing window', 203],
            ['Choose an integer value for the y size of the computing window', 204], ['Input the first covering zone parameter', 205],
            ['Input the second covering zone parameter', 206],
            ['Choose a float value for the first covering zone parameter', 207], ['Choose a float value for the second covering zone parameter', 208],
            ['Input the ROI parameters', 209], ['Input integers for the ROI parameters', 210],
            ['Input the X and Y coordinates for the calculation tracking', 211], ['Input integer for the X and Y coordinates for the calculation tracking', 212],
            ['calculation imput have been validated', 0]
        ]
        if not self.CalculCPIV_meths:
            return error[0], False, {}
        elif not self.CalculCPIV_dimX:
            return error[1], False, {}
        elif not self.CalculCPIV_dimY:
            return error[2], False, {}
        elif not self.CalculCPIV_dimX.isdigit():
            return error[3], False, {}
        elif not self.CalculCPIV_dimY.isdigit():
            return error[4], False, {}
        elif not self.CalculCPIV_recouv1:
            return error[5], False, {}
        elif not self.CalculCPIV_recouv2:
            return error[6], False, {}
        elif not self.isfloat(self.CalculCPIV_recouv1):
            if not self.is_float_between_0_and_1(self.CalculCPIV_recouv1): 
                return error[7], False, {}
        elif not self.isfloat(self.CalculCPIV_recouv2):
            if not self.is_float_between_0_and_1(self.CalculCPIV_recouv2): 
                return error[8], False, {}
        elif self.CalculCPIV_ROI == 'OK':
            if not self.CalculCPIV_ROIvalx0 or not self.CalculCPIV_ROIvaly0 or not self.CalculCPIV_ROIvalx1 or not self.CalculCPIV_ROIvaly1:
                return error[9], False, {}
            elif not self.CalculCPIV_ROIvalx0.isdigit():
                return error[10], False, {}
            elif not self.CalculCPIV_ROIvalx1.isdigit():
                return error[10], False, {}
            elif not self.CalculCPIV_ROIvaly0.isdigit():
                return error[10], False, {}
            elif not self.CalculCPIV_ROIvaly1.isdigit():
                return error[10], False, {}
        elif self.CalculCPIV_SuiviCalcul == 'OK':
            if not self.CalculCPIV_VecX or not self.CalculCPIV_VecY:
                return error[11], False, {}
            elif not self.CalculCPIV_VecX.isdigit() or not self.CalculCPIV_VecY.isdigit():
                return error[12], False, {}
        return error[13], True, self.dict_ans()

    def dict_ans(self):
        ans = {}
        ans["CalculCPIV_meths"] = self.CalculCPIV_meths
        ans["CalculCPIV_dimXYcell"] = self.CalculCPIV_dimXYcell
        ans["CalculCPIV_recouv"] = self.CalculCPIV_recouv
        ans["CalculCPIV_ROI"] = self.CalculCPIV_ROI
        if self.CalculCPIV_ROI == 'OK':
            ans["CalculCPIV_ROIval"] = self.CalculCPIV_ROIval
        ans["CalculCPIV_ConvTools"] = self.CalculCPIV_ConvTools
        ans["CalculCPIV_FiltrePostCalcul"] = self.CalculCPIV_FiltrePostCalcul
        ans["CalculCPIV_SuiviCalcul"] = self.CalculCPIV_SuiviCalcul
        if self.CalculCPIV_SuiviCalcul == 'OK':
            ans["CalculCPIV_VecX"] = self.CalculCPIV_VecX
            ans["CalculCPIV_VecY"] = self.CalculCPIV_VecY
        return ans

    def is_float_between_0_and_1(self, s):
    # Replace comma with dot to handle cases in which the user uses a comma
        s = s.replace(',', '.')
        try:
            # Convert to float
            num = float(s)
            # Check if number is in the desired range
            return 0 <= num < 1
        except ValueError:
            # Return False if conversion to float fails
            return False

    def isfloat(self,s: str) -> bool: # A quick function to check if a string is a float (can use . or , separator)
        pattern = r"^(\d+([.,]\d+)?|\d+[.,]?)$"
        # How does it work: We use the "re" library which enable the use of patterns to recognise str inputs
        # our pattern is (\d+([.,]\d+)?|\d+[.,]?)
        # \d+: Matches one or more digits. ([123].125)
        # ([.,]\d+)?: Allows one . or , followed by more digits. (123[,125])
        # |: enables another possible expression (123.125 or 123.)
        # \d+: Again, this matches one or more digits. ([123].)
        # [.,]?: Optionally matches a decimal separator (. or ,) with nothing required after it (123[,])
        return bool(re.match(pattern, s))
