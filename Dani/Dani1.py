obiecte = ['Masa', 5, 'Scaun', 4.5, [5,6,7], 8]
print(type(obiecte[0]))
print(type(obiecte[1]))
print(type(obiecte[2]))
print(type(obiecte[3]))
print(type(obiecte[4]))
print(type(obiecte[5]))
lista_nume = []
lista_numere = []
for item in obiecte:
    if type(item) == str:
        lista_nume.append(item)
    print('Obiectele string:', lista_nume)

#    elif type(item) == int or type(item) == float:     #???
#        lista_numere.append(item)
#    print('Obiecte int, float:', lista_numere)