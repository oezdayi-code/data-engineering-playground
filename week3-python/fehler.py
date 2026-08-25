# --- try / except üben ---

# 1) Fehler bei falscher Eingabe abfrangen
try:
    alter = int(input(" Wie alt bist du? "))
    print("Du bist", alter, "Jahre alt.")
except ValueError:
    print("Das war keine Zahl. Bitte gib eine Zahl ein.")

# 2) Fehler beim Teilen durch 0
def teile(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Division durch Null ist nicht erlaubt.")
        return None

print("10 / 2 =", teile(10, 2))
print("10 / 0 =", teile(10, 0))

# 3) Fehler bei Listen-Index
zahlen = [1,2,3]
try:
    print(zahlen[10])
except IndexError:
    print("Index existiert nicht in der Liste.")