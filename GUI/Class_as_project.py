# Author: Artur Stankiewicz
import shutil
import os
from as_lib import download_list
# from as_lib import download_dict

class AS_project:
######################################## init ############################################################
    def __init__(self, project_name):
        self.dir_project = r'C:\srm2\reg\%s\\' % project_name #sciezka do projektu

        self.dir_cfiles = r'C:\srm2\reg\files\{0}'
        self.dir_settings = self.dir_cfiles.format(r'settings\\')

        if os.path.exists(self.dir_project) and project_name.strip() != '': #jesli nie istnieje projekt albo nazwa jest blednie podana to nie otwiera nic
            self.existflag = True
            self.CRMfiles_names = []  # nazwy plikow ktore sa wklejane TYLKO JESLI SA CRM do katalogu projektu po eksporcie
            self.files_names = []  # nazwy plikow ktore sa wklejane ZAWSZE do katalogu projektu po eksporcie

            # CNFf ={r'SADAT.CNF':r'#define NUM_USER_PARM   ', r'VMFUNC.C':r'const codesize = ', r'AMSEC2.CNF': r':D5  ', r'XP.CNF': r'CALL("XCP.INI", "'} #nazwa pliku i linia ktora zmieniam

            download_list(self.dir_settings + 'CRMfiles_names.txt', self.CRMfiles_names)  # pobranie nazw plikow crm i wpisania do listy w celu kopiowania
            download_list(self.dir_settings + 'files_names.txt', self.files_names)  # pobranie nazw plikow i wpisania do lisy w celu kopiowania
        else:
            self.existflag=False
            print('projekt nie istnieje')

######################################## CheckFlag #######################################################
    def CheckFlag(self): #zwracac false jesli projekt nie istnieje
        Flag=self.existflag
        return Flag
######################################## XP ##############################################################
    def changeXP(self, T=2, L=0, FTO=0):
        path = self.dir_project + 'XP.CNF'
        closet=[]
        if os.path.exists(path) and self.existflag:
            try:
                # wpisanie zawartosci sadat.cnf do tablicy sadat, zamiana lini z codesize
                file = open(path)
                try:
                    for line in file:
                        try:

                            if line.find('CALL("XCP.INI", "') != -1:
                                print(line, end='')
                                line = ('CALL("XCP.INI", "T=%i, L=%i, FTO=%i");\n') % (T, L, FTO)

                            closet.append(line)#zapis doo tablicy closet


                        except:

                            closet.append(line)  # safty first :D
                            # jeśli w if coś nie zagra to linia bez zmian zostanie wpisana do closet
                finally:
                    file.close()

                # zwrocenie zawartosc tablicy closet do pliku


            except IOError:
                print('błąd IOError - otwarcia')

            try:
                file = open(path, 'w')
                try:
                    for line in closet:
                        file.write(line)

                finally:
                    file.close()
            except IOError:
                print('błąd IOError - otwarcia')
        else:
            print('Brak pliku XP.CNF w katalogu files')

######################################## XPM #############################################################
    def changeXPM(self, T=2, L=0, FTO=0):
        path = self.dir_project + 'XPM.CNF'
        closet=[]
        if os.path.exists(path) and self.existflag:
            try:
                # wpisanie zawartosci sadat.cnf do tablicy sadat, zamiana lini z codesize
                file = open(path)
                try:
                    for line in file:
                        try:

                            if line.find('CALL("XCP.INI", "') != -1:
                                print(line, end='')
                                line = ('CALL("XCP.INI", "T=%i, L=%i, FTO=%i");\n') % (T, L, FTO)

                            closet.append(line)#zapis doo tablicy closet


                        except:

                            closet.append(line)  # safty first :D
                            # jeśli w if coś nie zagra to linia bez zmian zostanie wpisana do closet
                finally:
                    file.close()

                # zwrocenie zawartosc tablicy closet do pliku


            except IOError:
                print('błąd IOError - otwarcia')

            try:
                file = open(path, 'w')
                try:
                    for line in closet:
                        file.write(line)

                finally:
                    file.close()
            except IOError:
                print('błąd IOError - otwarcia')
        else:
            print('Brak pliku XPM.CNF w katalogu files')

######################################## AMSEC2 ##########################################################
    def changeAMSEC2(self, L1=1, L2=1000, L3=20):
        path = self.dir_project + 'AMSEC2.CNF'
        closet=[]
        if os.path.exists(path) and self.existflag:
            try:
                # wpisanie zawartosci sadat.cnf do tablicy sadat, zamiana lini z codesize
                file = open(path)
                try:
                    for line in file:
                        try:

                            if line.find(':D5') != -1:
                                print(line, end='')
                                line = (':D5  %i %i %i             ; EC2; current option, range (mA), threshold (mA)\n') % ( L1, L2, L3)

                            closet.append(line)#zapis doo tablicy closet

                        except:

                            closet.append(line)  # safty first :D
                            # jeśli w if coś nie zagra to linia bez zmian zostanie wpisana do closet
                finally:
                    file.close()

                # zwrocenie zawartosc tablicy closet do pliku

            except IOError:
                print('błąd IOError - otwarcia')

            try:
                file = open(path, 'w')
                try:
                    for line in closet:
                        file.write(line)

                finally:
                    file.close()
            except IOError:
                print('błąd IOError - otwarcia')
        else:
            print('Brak pliku XP.CNF w katalogu files')

######################################## VMFUNC ##########################################################
    def changeVMFUNC(self, codesize=4096):
        path = self.dir_project + 'VMFUNC.C'
        closet=[]
        if os.path.exists(path) and self.existflag:
            try:
                # wpisanie zawartosci sadat.cnf do tablicy sadat, zamiana lini z codesize
                file = open(path)
                try:
                    for line in file:
                        try:

                            if line.find('const codesize =') != -1:
                                print(line, end='')
                                line = ('const codesize = %i;\n') % codesize

                            closet.append(line)#zapis doo tablicy closet

                        except:

                            closet.append(line)  # safty first :D
                            # jeśli w if coś nie zagra to linia bez zmian zostanie wpisana do closet
                finally:
                    file.close()

                # zwrocenie zawartosc tablicy closet do pliku

            except IOError:
                print('błąd IOError - otwarcia')

            try:
                file = open(path, 'w')
                try:
                    for line in closet:
                        file.write(line)

                finally:
                    file.close()
            except IOError:
                print('błąd IOError - otwarcia')
        else:
            print('Brak pliku XP.CNF w katalogu files')

######################################## SADAT ###########################################################
    def changeSADAT(self, NUM_USER_PARM=8):
        path = self.dir_project + 'SADAT.CNF'
        closet=[]
        if os.path.exists(path) and self.existflag:
            try:
                # wpisanie zawartosci sadat.cnf do tablicy sadat, zamiana lini z codesize
                file = open(path)
                try:
                    for line in file:
                        try:

                            if line.find('#define NUM_USER_PARM') != -1:
                                print(line, end='')
                                line = ('#define NUM_USER_PARM   %i\n') % NUM_USER_PARM

                            closet.append(line)#zapis doo tablicy closet

                        except:

                            closet.append(line)  # safty first :D
                            # jeśli w if coś nie zagra to linia bez zmian zostanie wpisana do closet
                finally:
                    file.close()

                # zwrocenie zawartosc tablicy closet do pliku

            except IOError:
                print('błąd IOError - otwarcia')

            try:
                file = open(path, 'w')
                try:
                    for line in closet:
                        file.write(line)

                finally:
                    file.close()
            except IOError:
                print('błąd IOError - otwarcia')
        else:
            print('Brak pliku XP.CNF w katalogu files')

######################################## insertFILES #####################################################
    def insertFILES(self):
        if self.existflag:
            try:
                for name in self.files_names:
                    shutil.copy(self.dir_cfiles.format(name), self.dir_project)
            except:
                print('\nBlad kopiowania pliku {0}'.format(name))

######################################## insertCRM #####################################################
    def insertCRM(self):
        if self.existflag:
            try:
                for name in self.CRMfiles_names:
                    shutil.copy(self.dir_cfiles.format(name), self.dir_project)
            except:
                print('\nBlad kopiowania pliku {0}'.format(name))