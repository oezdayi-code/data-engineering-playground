# Meine erste Python-Iste
einkaufsliste = ["Brot", "Milch", "Käse", "Äpfel"]

print("Die ganze Liste:")
print(einkaufsliste)

print("Erstes Element:") 
print(einkaufsliste[0])

print("Letztes Element:")
print(einkaufsliste[-1])

print("Anzahl der Einträge:")
print(len(einkaufsliste))

# Ein neues ELement hinzufügen
einkaufsliste.append("Butter")

print("Liste nach append:")
print(einkaufsliste)

# Ein Element ändern
einkaufsliste[1] = "Hafermilch"

print("Liste nach Änderung von Index 1:")
print(einkaufsliste)

# 1) Einfache Ausgabe pro Element
print("Alle Artikel einzeln:")
for artikel in einkaufsliste:
    print(artikel)

# 2) Zählen: wie oft läuft die Schleife?
print("Zählen mit for:")
zaehler = 0
for artikel in einkaufsliste:
    zaehler = zaehler + 1
print("In der Liste sind:",  zaehler, "Artikel") # <- keine Einrückung 

# 3) Mit if/else in der Schleife kombinieren
print("Mit if in der Schleife:")
for artikel in einkaufsliste:
    if artikel == "Käse":
        print(artikel, "ist mein Favorit")
    else:
        print(artikel)
