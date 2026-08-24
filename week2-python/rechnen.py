a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

zahl = int(input("Gib eine ganze Zahl ein: "))
print(f"{zahl} geteilt durch 2 hat den Rest {zahl % 2}")

if zahl % 2 == 0:
    print(f"{zahl} ist gerade")
else:
    print(f"{zahl} ist ungerade")   

if zahl > 0:
    print(f"{zahl} ist positiv")
elif zahl < 0:
    print(f"{zahl} ist negativ")
else:
    print(f"{zahl} ist null")

