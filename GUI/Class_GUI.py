# Author: Artur Stankiewicz
from tkinter import *

class GUI:
    def __init__(self , frame, but_name ,defText , chanText, colour='slate gray' ):
        self.colour= colour
        self.frame = frame  # ramka na ktorej rozmiescimy checkbuttons
        # self.func = func    #funkcja do wykonania gdy zaznaczymy check box i wcisniemy ok

        #############################zmienne########################################
        self.IntVar=IntVar() #zmienna int sprawdza czy checkbutton jest TRUE czy FALSE
        self.defaultText=defText
        self.defaultTextStrVar = StringVar()  # wartość sting

        self.changeText=[]
        self.changeText.append(chanText)
        self.changeTextStrVar=[]
        self.changeTextStrVar.append(StringVar())  #wartość sting

        #############################przypisanie do zmiennych teksu#####################
        self.defaultTextStrVar.set('') #ustawiam wartość stringu, zdanie jakim defaultowo zamieniamy linie
        self.changeTextStrVar[0].set('')   #czesc zdania po ktorym mozemy wpisac niestandardowe parametry

        ##############################tworzenie obiektow##############################
        self.CheckBut = Checkbutton(frame, text=but_name, variable=self.IntVar, command=self.Checkbutfun, bg=self.colour)

        self.defaultLabel = Label(self.frame, textvariable= self.defaultTextStrVar, bg=self.colour)
        self.changeLabel = Label(self.frame, textvariable=self.changeTextStrVar[0], bg=self.colour)

        self.changeEntry = Entry(self.frame, width=10)
        self.changeEntry.config(state=DISABLED)

        self.AddOptionsLabel = []
        self.AddOptionsEntry = [] #dodane wejscia
        self.AddOptionsEntry.append(self.changeEntry)

    # def Buttonfun(self, prebutcheck): #funkcja do do uycia w przycisku funkcja wykona się jeśli checkbutton jest zaznaczony i wcisniemy np. ok pressbut check to wartosc innego przycisku
    #     if  self.IntVar:
    #         # self.func()

    def AddChangeOption(self, *options): #Dodawanie dodatkowych parametrow do zmiany
        for option in options:
            self.changeText.append(option)
            self.changeTextStrVar.append(StringVar()) #.set('')
        for option in self.changeTextStrVar[1:]:
            self.AddOptionsLabel.append(Label(self.frame, textvariable=option, bg=self.colour))
            self.AddOptionsEntry.append(Entry(self.frame, width=10, state=DISABLED))

    def Check(self): #zwraca IntVar czyli stan Checkbutton'u
        StateOfCheckButton = self.IntVar.get()
        return StateOfCheckButton


    def Checkbutfun(self):
        if  self.IntVar.get():
            self.defaultTextStrVar.set(self.defaultText)  # ustawiam wartość stringu, zdanie jakim defaultowo zamieniamy linie
            for FunVar in zip(self.changeTextStrVar, self.changeText):
                Fun, Var   = FunVar
                # Var = FunVar[1]
                Fun.set(Var)
                #self.changeTextStrVar[0].set(self.changeText[0])  # czesc zdania po ktorym mozemy wpisac niestandardowe parametry
            for entry in self.AddOptionsEntry:
                entry.config(state=NORMAL)
        else:
            self.defaultTextStrVar.set('')  # ustawiam wartość stringu, zdanie jakim defaultowo zamieniamy linie
            #self.changeTextStrVar[0].set('')  # czesc zdania po ktorym mozemy wpisac niestandardowe parametry
            for StrVar in self.changeTextStrVar:
                # Var = FunVar[1]
                StrVar.set('')
            for entry in self.AddOptionsEntry:
                entry.config(state=DISABLED)
            #self.changeEntry.config(state=DISABLED)
        #print(self.changeText)

    def Place(self, nr): #zwraca liste (referencje) objektow Entry waszystkich wejsc



        ########## ROW 0 ###################
        row0=4*(nr-1)
        self.CheckBut.grid(row=row0, column=0, columnspan=3, sticky=W) #checkbutton

        ########### ROW 1 ##################
        row1 =1 + 4 * (nr - 1)
        Label(self.frame, text='Default: ', bg=self.colour).grid(row=row1, column=0, sticky=W) #description 'Default: '
        self.defaultLabel.grid(row=row1, column=1, columnspan=3, sticky=W) #linia 'Defaultowa', napis po opisie 'Default: '

        ########## ROW 2 ##################
        row2 = 2 + 4 * (nr - 1)
        Label(self.frame, text='Change: ', bg=self.colour).grid(row=row2, column=0, sticky=W)  # description 'Change: '
        self.changeLabel.grid(row=row2, column=1, sticky=E) #linia 'Change', napis po opisie 'Change: '
        self.changeEntry.grid(row=row2, column=2, sticky=W) #line for entry the change if emoty then don't do anything

        ############### DODAWANIE DODATKOWYCH PARAMETROW DO ZMIANY JESLI SA DODANE#####################################
        colLabel = 3 #column for next Label to chenge

        for AddLabel in self.AddOptionsLabel:
            AddLabel.grid(row=row2, column=colLabel, sticky=E)
            colLabel+=2

        colEntry = 4  # column for next Entry to chenge
        for AddEntry in self.AddOptionsEntry[1:]:
            AddEntry.grid(row=row2, column=colEntry, sticky=E)
            colEntry+=2
        ########## ROW 3 ##################
        row3 = 3 + 4 * (nr - 1)
        Label(self.frame, bg=self.colour).grid(row=row3, column=0, sticky=W)
        return self.AddOptionsEntry



