# Author: Artur Stankiewicz

from Class_GUI import *
from Class_as_project import *
from counters2 import *
from tkinter import *
from as_lib import *



CounterApp = App()
project= AS_project()

########################## configuration ############################
WinColour='gray23'
LefSideColour='slate gray'
ConterButColour='thistle4'
########################## ROOT #####################################
window = Tk()
LefSide=Frame(window,  bg=LefSideColour, width=300, bd=20) #text='options',
TopSide=Frame(window, bg=WinColour,width=200,  height=510) #WinColour width= 700, height=500,  //, relief=RIDGE, pady=100, padx=250


window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

window.title('Badz mechanikiem wsrod supermenow')
window.geometry("900x530")
window.config(bg=WinColour)

########################## MenuBAR #####################################
menuBar= Menu(window)
# display the menu
window.config(menu=menuBar)

menuBar.add_command(label='Counters', command= lambda : CounterApp.start()) #counter button





#################### Place for checkbuttons ########################

LefSide.grid(row=0, column=0, stick='nswe') #, stick='nswe'
TopSide.grid(row=0, column=1, stick='nswe') # TopSide.pack(side=RIGHT) # side=RIGHT, fill=BOTH

# TopSide.grid(row=0, column=1, stick='nsew')
# LefSide.rowconfigure(0, weight=1)
# LefSide.columnconfigure(0, weight=1)
# LefSide.pack(side=LEFT, fill=Y) #, fill=BOTH
# LefSide.place(relx=0, relheight=1, relwidth=0.5)
# BotSide=Frame(window, width= 700, height=500, bg=WinColour) #width= 700, height=500,
# BotSide.place(relx=0.7, rely=0.5, relwidth=1, relheight=1)
# BotSide.grid(row=1, column=1,stick='nsew')







CurProjectName=StringVar()
CurProjectName.set('')
#################### Project and entry names #########################
ProjectNameLabel= Label(TopSide, text='Project path: ', bg=WinColour, fg='white', font=15, pady=20)
ProjectNameEntry=Button(TopSide, text='search project', command= lambda : project.chooseDirectory(CurProjectName), bg='black', fg='white', width=45  )
CurProjectNameLabel= Label(TopSide, textvariable=CurProjectName, bg=WinColour, fg='red2', font=15) #current project name





#################### Checkbuttons ###################################
SADAT=GUI(LefSide, 'SADAT.CNF', '#define NUM_USER_PARM   8', '#define NUM_USER_PARM')
SADATentry=SADAT.Place(1)

VMFUNC=GUI(LefSide, 'VMFUNC.C', 'const codesize = 4096;', 'const codesize = ')
VMFUNCentry=VMFUNC.Place(2)

AMSEC2=GUI(LefSide, 'AMSEC2.CNF', ':D5  1 1000 20', ':D5')
AMSEC2.AddChangeOption(' ', ' ')
AMSEC2entry=AMSEC2.Place(3)

XP=GUI(LefSide, 'XP.CNF', 'CALL("XCP.INI", "T=2,L=0,FTO=0");', 'CALL("XCP.INI", T="')
XP.AddChangeOption(',L=', ',FTO=')
XPentry=XP.Place(4)

XPM=GUI(LefSide, 'XPM.CNF', 'CALL("XCP.INI", "T=2,L=0,FTO=0");', 'CALL("XCP.INI", T="')
XPM.AddChangeOption(',L=', ',FTO=')
XPMentry=XPM.Place(5)

PastFlag= IntVar()
PasteTrace = Checkbutton(LefSide, text='Paste Trace...', variable=PastFlag, bg=LefSideColour)
PasteTrace.grid(row=20, column=0, columnspan=3, sticky=W)

PastCRMFlag= IntVar()
PasteCRM = Checkbutton(LefSide, text='Past CRM', variable=PastCRMFlag, bg=LefSideColour)
PasteCRM.grid(row=22, column=0, columnspan=3, sticky=W)

ProjectNameLabel.pack(side=TOP)
CurProjectNameLabel.pack(side=TOP, anchor=CENTER)
ProjectNameEntry.pack(side=TOP, fill=X,  ipady=10, padx=20) #

################### OK button function ######################################
def ButFun():
    project.StartCheck()
    NameOfProject=project.CheckProDir()
    NameOfProject=NameOfProject[12:-1]

    project_exist= project.CheckFlag()
    if project_exist:
        if SADAT.Check():
            try:
                x=int(SADATentry[0].get())
                project.changeSADAT(x)
            except:
                project.changeSADAT()

        if VMFUNC.Check():
            try:
                x=int(VMFUNCentry[0].get())
                project.changeVMFUNC(x)
            except:
                project.changeVMFUNC()

        if AMSEC2.Check():
            try:
                x=int(AMSEC2entry[0].get())
                y=int(AMSEC2entry[1].get())
                z=int(AMSEC2entry[2].get())
                project.changeAMSEC2(x, y, z)
            except:
                project.changeAMSEC2()

        if XP.Check():
            try:
                x=int(XPentry[0].get())
                y=int(XPentry[1].get())
                z=int(XPentry[2].get())
                project.changeXP(x, y, z)
            except:
                project.changeXP()

        if XPM.Check():
            try:
                x=int(XPMentry[0].get())
                y=int(XPMentry[1].get())
                z=int(XPMentry[2].get())
                project.changeXPM(x, y, z)
            except:
                project.changeXPM()
        if PastFlag.get():
            try:
                project.insertFILES()
            except:
                pass
        if PastCRMFlag.get():
            try:
                project.insertCRM()
            except:
                pass
        st = ('Project: {} gotowy KAPITANIE :D').format(NameOfProject)
        maste = Tk()
        maste.title('Project name')
        maste.config(bg='SeaGreen3')
        maste.geometry("550x250+200+100")
        ms = Message(maste, text=st)
        Exit = Button(maste, text='OK', command=maste.destroy, bg='SeaGreen2', width=10, height=3)
        ms.config(bg='SeaGreen3', font=('times', 24, 'italic'))
        ms.pack(fill=BOTH)
        Exit.pack()



    else:
        str =('Project: {} nie istnieje lub podaleś niewłaściwą nazwę ').format(NameOfProject)
        master = Tk()
        master.title('Project name')
        master.config(bg='firebrick1')

        master.geometry("550x250+200+100")
        msg = Message(master, text=str)
        Exit = Button(master, text='OK', command=master.destroy, bg='firebrick3', width=10, height=3)
        msg.config(bg='firebrick1', font=('times', 24, 'italic'))
        msg.pack(fill=BOTH)
        Exit.pack()



OKbut=Button(TopSide, text='OK', command=ButFun, width=8, height=3, bd=4) #, command=print_but




OKbut.pack(side=TOP)
Label(TopSide, bg=WinColour).pack()



window.mainloop()

# CheckVar1 = IntVar()
# CheckVar2 = IntVar()
# CheckVar3 = IntVar()
# tekst1= StringVar()
# tekst2= StringVar()
# tekst3= StringVar()
# opis1=Label(LefSide, textvariable=tekst1)
# opis2=Label(LefSide, textvariable=tekst2)
# opis3=Label(LefSide, textvariable=tekst3)
#
#
# def print_box1():
#         print(CheckVar1.get(), ' ', CheckVar2.get(), ' ', CheckVar3.get())
#         tekst1.set('{} {} {}'.format(CheckVar1.get(), CheckVar2.get(), CheckVar3.get()))
#         entchan1.config(state=NORMAL)
#         if not CheckVar1.get():
#             tekst1.set('')
#             entchan1.config(state=DISABLED)
# def print_box2():
#         print(CheckVar1.get(), ' ', CheckVar2.get(), ' ', CheckVar3.get())
#         tekst2.set('{} {} {}'.format(CheckVar1.get(), CheckVar2.get(), CheckVar3.get()))
#         entchan2.config(state=NORMAL)
#         if not CheckVar2.get():
#             tekst2.set('')
#             entchan2.config(state=DISABLED)
# def print_box3():
#         print(CheckVar1.get(), ' ', CheckVar2.get(), ' ', CheckVar3.get())
#         tekst3.set('{} {} {}'.format(CheckVar1.get(), CheckVar2.get(), CheckVar3.get()))
#         entchan3.config(state=NORMAL)
#         if not CheckVar3.get():
#             tekst3.set('')
#             entchan3.config(state=DISABLED)
#
# def print_but():
#     str=ProjectNameEntry.get()
#     if not str:
#         str='podaj nazwe projektu'
#     master=Tk()
#     master.title('Project name')
#     master.geometry("200x200+200+100")
#     whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
#     msg = Message(master, text=str)
#     msg.config(bg='lightgreen', font=('times', 24, 'italic'))
#     msg.pack()
#
#
#
#
# c=Checkbutton(LefSide, text='Xprio', variable=CheckVar1, command=print_box1 )
# b=Checkbutton(LefSide, text='CRM' , variable=CheckVar2,command=print_box2 )
# d=Checkbutton(LefSide, text='Modemreset', variable=CheckVar3, command=print_box3  )
#
#
#
#
# defaultLab1=Label(LefSide, text='Default: ')
# defaultLab2=Label(LefSide, text='Default: ')
# defaultLab3=Label(LefSide, text='Default: ')
#
# changeLab1=Label(LefSide, text='Change')
# changeLab2=Label(LefSide, text='Change')
# changeLab3=Label(LefSide, text='Change')
#
# entchan1=Entry(LefSide, width=10)
# entchan1.config(state= DISABLED)
# entchan2=Entry(LefSide, width=10)
# entchan2.config(state= DISABLED)
# entchan3=Entry(LefSide, width=10)
# entchan3.config(state= DISABLED)
#
#
#
# opis3.grid(row=9, column=1, sticky=W)
#
# c.grid(row=0, column=0,columnspan=3,  sticky=W)
# defaultLab1.grid(row=1, column=0, sticky=W)
# opis1.grid(row=1, column=1, sticky=W)
# changeLab1.grid(row=2, column=0, sticky=W)
# entchan1.grid(row=2, column=2, padx=10, sticky=W)
# Label(LefSide).grid(row=3, column=0, sticky=W)
#
# b.grid(row=4, column=0,columnspan=3,  sticky=W)
# defaultLab2.grid(row=5, column=0, sticky=W)
# opis2.grid(row=5, column=1, sticky=W)
# changeLab2.grid(row=6, column=0, sticky=W)
# entchan2.grid(row=6, column=2, padx=10, sticky=W)
# Label(LefSide).grid(row=7, column=0, sticky=W)
#
# d.grid(row=8, column=0,columnspan=3,  sticky=W)
# defaultLab3.grid(row=9, column=0, sticky=W)
# changeLab3.grid(row=10, column=0, sticky=W)
# entchan3.grid(row=10, column=2, padx=10, sticky=W)
# Label(LefSide).grid(row=11, column=0, sticky=W)



