# --- Funktionen üben ---

# 1) Funktionen ohne Rückgabewert
def gruesse(name):
    print("Hallo", name)

gruesse("Timuçin")
gruesse("Hayriye")

# 2) Funktionen mit Rückgabewert
def addiere(a, b):
    return a + b

ergebnis = addiere(3, 5)
print("3 + 5 =", ergebnis)
print("10 + 20 =", addiere(10, 20))

# 3) Funktione, die eine LIste bekommt und die Summe zurückgibt
def summiere_liste(zahlen):
    gesamt = 0
    for z in zahlen:
        gesamt = gesamt + z
    return gesamt

preise = [1.99, 2.50, 0.89, 3.20]
print("Summe der Preise:", summiere_liste(preise))

umsatz = [1000, 1500, 800, 2200, 1750]
print("Wochenumsatz:", summiere_liste(umsatz))
