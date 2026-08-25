# Mini-Projekt Woche 3
# Tagesumsätze einer Woche auswerten, auch wenn die Rohdaten schmutzig sind.

# --- 1) Rohdate (wie aus einer CSV-Spalte) ---
rohdaten = ["1200", "980", "n/a", "1750", "", "2100", "895"]

# --- 2) Hilfsfunnktion: einen Rohwert in eine Zahl umwandeln ---
# Gibt None zurück, wenn der Wert kein gültiger Zahlen-String ist.
def zu_zahl(wert):
    try:
        return float(wert)
    except ValueError:
        return None

# --- 3) Rohdaten durchgehen und die gültigen Werte einsammeln ---
gueltig = []
verworfen = 0
for eintrag in rohdaten:
    zahl = zu_zahl(eintrag)
    if zahl is None:
        verworfen = verworfen + 1
    else:
        gueltig.append(zahl)

# --- 4) Auswertungs-Funktionen ---
def summe(zahlen):
    gesamt = 0
    for z in zahlen:
        gesamt = gesamt + z
    return gesamt

def durchschnitt(zahlen):
    if len(zahlen) == 0:
        return 0
    return summe(zahlen) / len(zahlen)

def maximum(zahlen):
    if len(zahlen) == 0:
        return None
    groesster = zahlen[0]
    for z in zahlen:
        if z > groesster:
            groesster = z
    return groesster

# --- 5) Report ausgeben ---
print("---Umsatz-Report ---")
print("Rohdaten gesamt:", len(rohdaten))
print("Gültige Werte:  ", len(gueltig))
print("Verworfen:      ", verworfen)
print()
print("Summe:      ", summe(gueltig))
print("Durchschnitt:", durchschnitt(gueltig))
print("Maximum:    ", maximum(gueltig))
