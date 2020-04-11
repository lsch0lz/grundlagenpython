""" Abschnitt 13 des Python-BootCampns """

#Funktionsparameter benennen 

def multi_print(number = 3, word = "Hallo"):
    for i in range(0, number):
        print(word)

multi_print()
multi_print(5, "Welt")