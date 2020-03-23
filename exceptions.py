"Abschnitt 11 des Python Bootcamps"

#einfache exception 
"""
try:
    with open("meinfile.txt", "r") as file:
        print(file)
except FileNotFoundError:
    print("Das war falsch")
"""
#exceptions die in einer Funktion auftreten
"""
def function_whatever():
    print(5/0)

try:
    function_whatever()
except ZeroDivisionError:
    print("Das hat nicht funktioniert")
"""
#eigene exception erstellen
"""
#eigene exceptiosn
class InvalidEmailError(Exception): #eigener Klassenname muss gewählt werden
    pass

def send_email(mail, subject, content):
    if not "@" in mail:
        raise InvalidEmailError("Email does not contain an @")

send_email("hallo", "betreff", "text")
"""

 #file wird bei exception immer geschlossen
"""
 with open("existiert.txt", "r") as file:
     print(file)
     print(5/0)
     #durch with open wird trotz exception die Datei geschlossen
"""