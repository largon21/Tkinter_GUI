# Author: Artur Stankiewicz
from Class_GUI import *
from Class_as_project import *
from counters2 import *


CounterApp = App()


########################## configuration ############################
WinColour='tomato3'
LefSideColour='thistle2'
ConterButColour='RosyBrown3'
########################## ROOT #####################################
window = Tk()
window.title('Ale masz pythona')
window.geometry("900x650+200+50")
window.config(bg=WinColour)

#################### Nazwa projektu i entry #########################
ProjectNameLabel= Label(window, text='Project name ', bg=WinColour)
ProjectNameEntry=Entry(window)



#################### Miejsce na checkbuttons ########################
LefSide=LabelFrame(window, text='options', width= 900 , height=300, bg=LefSideColour)
LefSide.pack(side=TOP, fill=BOTH) #, fill=BOTH

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

Counter = Button(window, text='Counters', command= lambda : CounterApp.start(), bg=ConterButColour)
Label(window, bg=WinColour).pack()
Counter.pack()



ProjectNameLabel.pack()
ProjectNameEntry.pack()

################### OK button ######################################
def ButFun():
    project= AS_project(ProjectNameEntry.get())
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



    else:
        str =('Project: {} nie istnieje lub podaleś niewłaściwą nazwę ').format(ProjectNameEntry.get())
        master = Tk()
        master.title('Project name')
        master.geometry("400x150+200+100")
        msg = Message(master, text=str)
        msg.config(bg='deep pink', font=('times', 24, 'italic'))
        msg.pack(fill=BOTH)




OKbut=Button(window, text='OK', command=ButFun) #, command=print_but
OKbut.pack()

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



