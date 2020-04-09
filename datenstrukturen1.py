"""Abschnitt 12 des Python Bootcamps"""
"""
- Objekt was mehrere Elemente enthält (Liste, Dic)
- Set -> ungeordnete Sammlung von Elementen (Alle Elemente nur einmal)
- PriorityQueue -> autom. Sortieren von Elementen
"""

#Datenstruktur Set

"""
s = {"Hallo", "Welt"}
print(s)
s.add("Mars")   #-> Sortierung kann verloren gehen (anders als bei Listen)
print(s)        # Mars könnte nicht noch einmal hinzugefügt werden

if "Mars" in s:
    print("Ja")

text = "Hallo Welt Hallo Mars Hallo Welt"
words = set()
for word in text.split(" "):
    words.add(word)
print(words)
print(len(words))
"""

#Datenstruktur queue (Eintrag hinzufügen; Eintrag vom Anfang entfernen)

"""
import queue
q = queue.Queue()

q.put("Hallo")
q.put("Welt")
q.put("Mars")
q.put("Pluto")
print(q)
print(q.get())
print(q.get())

while not q.empty():
    element = q.get()
    print(element)
"""

#Datenstruktur PriorityQueue

"""
import queue
q = queue.PriorityQueue()

q.put((10, "Hallo Welt"))
q.put((15, "Hallo Mars"))
q.put((5, "Wichtig"))

print(q.get())
print(q.get())

text = "A A A A A A A A B B B B B C C D D D D"
d = {}
for word in text.split(" "):
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1
print(d)

pq = queue.PriorityQueue()
for word, number in d.items():
    pq.put((-number, word))     #Aufsteigend: number ABsteigend: -number

print(pq.get())
print(pq.get())
print(pq.get())
"""