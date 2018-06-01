# Author: Artur Stankiewicz

def download_list(dir, where): #funkcja pobierajaca linie z pliku tekstowego o sciezce dir i wpisuje linie do listy podanej w drugim argumencie
    w=[]
    w=where
    try:
        file = open(dir)
        try:
            for line in file:
                w.append(line.strip())

        finally:
            file.close()
    except IOError:
        print('Błąd IOError: '+ dir)


def download_dict(dir, where): #funkcja pobierajaca linie z pliku tekstowego o sciezce dir i wpisuje linie do listy podanej w drugim argumencie
    w={}
    w=where
    i=1
    key=''
    value=['','']
    try:
        file = open(dir)
        try:
            for line in file:
                if i==1:
                    key=line.strip()

                elif i==2:
                    value[0]=line.strip()

                elif i==3:
                    value[1]=line.strip()
                    w[key] = value[:]
                    i = -1

                i += 1

        finally:
            file.close()
    except IOError:
        print('Błąd IOError: '+ dir)