# number = int(input("Type a number: "))
# counter = 0
# while counter <= number:
#     if not counter % 2:
#         print(counter)
#     counter += 1

print("1. Cappuccino     ... 4 lei","2. Espresso       ... 3.5 lei",sep="\n")
Cappucino = 4
Espresso = 3.5
optiune = 0
while not optiune:
    optiune = int(input("Ce optiune alegeti? [1,2]: "))
    if optiune == 1:
        print("Ati ales optiunea 1")
    elif optiune == 2:
        print("Ati ales optiunea 2")
    else:
        print("Alegere gresita")
        optiune = 0

while True:
    bani = int(input("Introduceti o banconta [5,10]: "))
    if bani == 5:
        print("Ati introdus 5 lei")
        break
    elif bani == 10:
        print("Ati introdus 10 lei")
        break
    else:
        print("Se permit doar bancnote de 5 sau 10 lei")
        continue

if optiune == 1:
    print(f"Veti primi restul de {bani-Cappucino} lei","Produsul se livreaza...",sep="\n")
elif optiune == 2:
    print(f"Veti primi restul de {bani- Espresso} lei", "Produsul se livreaza...", sep="\n")
else:
    print("Alegere gresita")

