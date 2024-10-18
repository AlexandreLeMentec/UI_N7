import tkinter as tk
from tkinter import ttk, font
from tkinter import filedialog as fd
from image import image_input
import sys
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
        self.image = image_input(self.window,tk,ttk)
        self.calcul = calcul_input(self.window,tk,ttk)
        self.action = action_input(self.window,tk,ttk)
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

class calcul_input:
    def __init__(self,window,tk,ttk) -> None:
        #Global frame and window
        self.window = window
        self.calc_frame = tk.Frame(self.window)
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
        
        
        #Toggleable non-interactive items


        #Non-toggleable non-interactive items
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




    def setup(self):
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


    def refresh(self):
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

    def choice(self):
        if self.CalculCPIV_ROI != self.CalculCPIV_ROI_old:
            self.hide_ROI()
            if self.CalculCPIV_ROI == 'OK':
                self.show_ROI()
            self.CalculCPIV_ROI_old = self.CalculCPIV_ROI
                
    def show_ROI(self):
        self.ROI_label_xy0.grid(column = 2, row= 7, sticky = 'W')
        self.ROI_label_xy1.grid(column = 2, row= 8, sticky = 'W')
        self.inp_CalculCPIV_ROIvalx0.grid(column = 3, row= 7, sticky = 'E')
        self.inp_CalculCPIV_ROIvaly0.grid(column = 4, row= 7, sticky = 'W')
        self.inp_CalculCPIV_ROIvalx1.grid(column = 3, row= 8, sticky = 'E')
        self.inp_CalculCPIV_ROIvaly1.grid(column = 4, row= 8, sticky = 'W')

    def hide_ROI(self):
        self.ROI_label_xy0.grid_forget()
        self.ROI_label_xy1.grid_forget()
        self.inp_CalculCPIV_ROIvalx0.grid_forget()
        self.inp_CalculCPIV_ROIvaly0.grid_forget()
        self.inp_CalculCPIV_ROIvalx1.grid_forget()
        self.inp_CalculCPIV_ROIvaly1.grid_forget()



class action_input:
    def __init__(self,window,tk,ttk) -> None:
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

