import tkinter as tk
from tkinter import ttk, font
from tkinter import filedialog as fd
from image import image_input
from calcul import calcul_input
import sys
import os
from datetime import datetime

# from ttkthemes import ThemedTk

class PIV_UI :
    def __init__(self) -> None:
        #self.window = ThemedTk(theme='radiance')
        self.window = tk.Tk()
        self.window.title("UI Calcul PIV")
        self.window.geometry('')
        self.window.pack_propagate(True)
        self.window.configure(bg='gray3')
        self.window.protocol("WM_DELETE_WINDOW", self.closing)
        self.window.option_add('*TCombobox*Listbox.background', 'gray3')
        self.window.option_add('*TCombobox*Listbox.foreground', 'chartreuse2')
        self.window.option_add('*TCombobox*Listbox.selectBackground', 'gray3')
        self.window.option_add('*TCombobox*Listbox.selectForeground', 'chartreuse2')
        self.text_font = font.Font(font='Consolas',size=10)
        self.title_font = font.Font(family='Consolas',size=20)
        self.globalframe = tk.Frame(self.window)
        self.globalframe.config(bg='gray3')
        self.globalframe.grid(column = 0, row= 0, sticky = 'W')
        self.main_display()
        self.image = image_input(self.globalframe,tk,ttk,os)
        self.calcul = calcul_input(self.globalframe,tk,ttk,os,font)
        self.error1 = ''
        self.error2 = ''
        self.validation_frame = tk.Frame(self.globalframe)
        self.validation_frame.config(bg='gray3',highlightbackground='chartreuse2',highlightcolor="chartreuse2",highlightthickness=3,relief='sunken')
        self.save_button = tk.Button(self.validation_frame,text="> SAVE <",command = self.validity_check,
                                    foreground="chartreuse2",background="gray3",highlightcolor="chartreuse2",highlightbackground="chartreuse2",
                                    font=self.title_font)

    def start(self):
        self.image.setup()
        self.calcul.setup()
        self.validation_frame.pack(padx = 1, pady = 2)
        self.validation_space_setup()
        self.main_loop()
        self.window.mainloop()

    def validation_space_setup(self):
        self.save_button.pack()

    def closing(self):
        self.window.destroy
        sys.exit()

    def main_display(self):
        # Logo Frame
        Prez_frame = tk.Frame(self.globalframe)
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

    def refresh_window(self): # a function containing all the action supposed to happen at each frame 
        self.image.refresh()
        self.image.type_choice()
        self.calcul.refresh()
        self.calcul.choice()

    def main_loop(self):
        self.window.after(100,self.refresh_window)
        self.window.after(100,self.main_loop)
        self.window.update()

    def validity_check(self):
        m1 = self.image.entry_validation()
        m2 = self.calcul.entry_validation()
        if m1[1] and m2[1]:
            timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M")
            filename = f"{timestamp}_OUTPUT.txt"
            directory = os.path.join("RESULT",filename)
            self.write_dict(m1[2], m2[2], directory)
            message = str(m1[0][1]) +'] ' + m1[0][0] + "\n" + str(m2[0][1]) +'] ' + m2[0][0] + "\n" + "Results have been saved at :"
            message += "\n" + directory
            self.show_error(message)
        else:
            self.show_error(str(m1[0][1]) +'] ' + m1[0][0] + "\n" + str(m2[0][1]) +'] ' + m2[0][0])
    
    def write_dict(self, dict1, dict2, directory):
        with open(directory, 'w') as file:
            for key, value in dict1.items():
                file.write(f"{key}   {value}\n")
            for key, value in dict2.items():
                file.write(f"{key}   {value}\n")
        

    def show_error(self, message):
    # Create a new Toplevel window for the error
        error_window = tk.Toplevel()
        error_window.title("Validity verification")
        error_window.configure(bg='gray3')
        # Set the size of the error window
        error_window.geometry("")
        # Create a label with the error message
        label = tk.Label(error_window, text=message, padx=20, pady=20, bg='gray3',fg='chartreuse2',font=self.text_font)
        label.pack()
        # Create an "OK" button to close the window
        ok_button = tk.Button(error_window, text="OK", command=error_window.destroy, 
                              foreground="chartreuse2",background="gray3",highlightcolor="chartreuse2",highlightbackground="chartreuse2",
                              font=self.title_font)
        ok_button.pack(pady=10)

if __name__ == "__main__":
    UI = PIV_UI()
    UI.start()
