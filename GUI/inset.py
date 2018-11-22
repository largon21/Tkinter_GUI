from tkinter import *

class InsetGUI:
    def __init__(self, frame):
        self.frame=frame

        Label(self.frame, text='file name:', bd=3).grid(row=0, column=0, stick='w', padx=5)

        Label(self.frame, text='first line:', bd=3).grid(row=2, column= 0, stick='w', padx=5)

        Label(self.frame, text='last line:', bd=3).grid(row=2, column= 1, stick='w', padx=5)

        Label(self.frame, text='lines to change:', bd=3).grid(row=4, column= 0, stick='w', padx=5)

        self.file_list = Listbox(self.frame, width=24, bd=3, height=5)
        self.file_list.insert(END, 'SADAT.CNF')
        self.file_list.insert(END, 'VMFUNC.C')
        self.file_list.insert(END, 'AMSEC2.CNF')
        self.file_list.insert(END, 'XP.CNF')
        self.file_list.insert(END, 'XPM.CNF')
        self.file_list.grid(row=1, column=0, stick='w', padx=5)

        self.first_entry = Entry(self.frame, width=24, bd=3).grid(row=3, column=0, stick='w', padx=5)

        self.last_entry = Entry(self.frame, width=24, bd=3).grid(row=3, column=1, stick='w', padx=5)

        self.lines_text = Text(self.frame, width=50, height=15, bd=3).grid(row=5, column=0, columnspan=2, stick='w', padx=5)


    def selection(self):
        try:
            index=self.file_list.curselection()
            fileName=self.file_list.get(index)
        except:
            fileName=''
        return fileName