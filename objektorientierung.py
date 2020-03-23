"""Abschnitt 8 des Python Bootcamps"""

#Klasse erstellen
"""
class Students():
    pass

def get_name(student):
    print(student.firstname + " " + student.lastname)

erik = Students()
erik.firstname = "Erik"
erik.lastname = "Mustermann"

get_name(erik)


monika = Students()
monika.firstname = "Monika"
monika.lastname = "Müller"

get_name(monika)
"""

#Funktion in Klasse -> Dadurch kannnn die .name() Funktion auch später aufgerufen werden
"""
class Students():
    def name(self):
        print(self.firstname + " " + self.lastname)

erik = Students()
erik.firstname = "Erik"
erik.lastname = "Mustermann"

erik.name()


monika = Students()
monika.firstname = "Monika"
monika.lastname = "Müller"

monika.name()
"""

#Constructor

"""
class Student():
    def __init__(self, firtsnname, lastname):   #self Parameter bezieht sich auf Student
        self.firstname = firtsnname
        self.lastname = lastname
        self.term = 1
    
    def increase_term(self):
        self.term = self.term + 1
    
    def name(self):
        print(self.firstname + " " + self.lastname + " Semester: " + str(self.term))

erik = Student("Erik", "Mustermannn")   #Parameter landenn inn der __init__ Funnktion
print(erik.firstname)
print(erik.lastname)

erik.increase_term()
erik.name()
"""

#Private Eigenschaften und Methoden

"""
class Student():
    def __init__(self, firtsnname, lastname, age):   #self Parameter bezieht sich auf Student
        self.firstname = firtsnname
        self.lastname = lastname
        self.age = age
        self.__term = 1 # __ macht es zu einer private 
    # _ -> ist eine Konvention für Variablen auf die nicht publich Zugefriffen werden sollte
    def increase_term(self):
        if self.__term >= 9:
            return
        self.__term = self.__term + 1
    
    def name(self):
        print(self.firstname + " " + self.lastname + " Semester: " + str(self.__term) + " " + self.age)

erik = Student("Erik", "Mustermannn", "20")   #Parameter landenn inn der __init__ Funnktion

erik.__term = 100 #kann gemacht werden, da public (Obwohl nicht vorgesehen)
erik.increase_term()
erik.name()
"""
#Daten Kapseln, damit Sie im späteren verlauf nicht verändert werden können
"""
class PhoneBook():

    def __init__(self):
        self.__entries = {}

    def add(self, name, phone_number):
        self.__entries(name) = phone_number

    def __str__(self): #gute Methode zum debuggen
        return "PhoneBook(" + str(self.__entries")

    def __repr__(self):
        return "PhoneBook(" + str(self.__entries")
    
    def __len__(self):
        return len(self.__entries)


book = PhoneBook()
book.add("Mustermann", "01797274043")
book.add("Müller", "01795674563")

print(book.__entries)

print(book) #um __str__ Methode aufzurufen
book        #um __repr__ Methode aufzurufen

print(len(book))    #um länge des Dic herauszufinden
"""

#Vererbung

class Student():
    def __init__(self, firstname, lastname):
        self.firtsnname = firstname
        self.lastname = lastname
    
    def name(self):
        return self.firtsnname + " " + self.lastname

class WorkingStudent(Student):  #(Student) vererbt alle Eigenschaften der Studenten Klasse
    def __init__(self, firstname, lastname, company):
        super().__init__(firstname, lastname)   #__init__ aus der vererbten Klasse (Student) aufgerufen
        self.company = company
    
    def name(self):
        return super().name()+ " " + self.company   #name wird aus vererbter Klasse aufgerufen


student = Student("Max", "Müller")
student2 = WorkingStudent("Tom", "Mustermann", "facebook")

students = [
    Student("Tom", "Müller"),
    WorkingStudent("Lukas", "Scholz", "DB"),
    Student("Lisa", "Neumann"),
    WorkingStudent("Monika", "Mustermann", "Deutsche Bank")
]

for student in students:
    print(students.name())

    
print(student.name())
print(student2.name())



