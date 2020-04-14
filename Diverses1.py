""" Abschnitt 13 des Python-BootCampns """

#Funktionsparameter benennen 

"""
def multi_print(number = 3, word = "Hallo"):
    for i in range(0, number):
        print(word)

multi_print()
multi_print(5, "Welt")
"""

#Wie werden Funktionsparameter übergeben

a = 5
l = ["Hallo", "Welt"]

def f(x):
    #x.append("111")     #Kopie von der Liste l wird angelegt und darin wird der Inhalt verändert
    print(x)

f(l)
print(l)    #da in der Funktion die Kopie verändert worden ist wird hier auch die veränderte Kopie ausgegeben

def j(p):
    p = ["Hallo", "Welt", "!!!"]    #Es wird eine neue Kopie erstellt und die andere wird ebenfalls erhalten
    print(p)

j(l)        #Die neue Kopie wird ausgegeben
print(l)    #Die alter Version wird ausgegeben