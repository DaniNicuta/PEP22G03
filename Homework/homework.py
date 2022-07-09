#  Quest  1

#  password = 'Passme1n'
#  passinput = input('Insert password: ')
#  result = password == passinput
#  print(result)

#  Quest 2
#  name1 = input('User 1: ')
#  name2 = input('User 2: ')
#  print('Numarul de caractere user 1:', len(name1))
#  print('Numarul de caractere este egal?', len(name1) == len(name2))
#  print('Numarul de caractere al primului nume este mai mare?', len(name1) > len(name2))
#  print('Initiala primului nume este: ', name1[0])
#  print('Primul nume inversat: ', name1[::-1])

#  Quest 3

#  name1 = input('User 1: ')
#  name2 = input('User 2: ')
#  print('Numarul de caractere user 1:', len(name1))
#  print('Numarul de caractere este egal?', len(name1) == len(name2))
#  print('Numarul de caractere al primului nume este mai mare?', len(name1) > len(name2))
#  print('Initiala primului nume este: ', name1[0])
#  print('Primul nume inversat: ', name1[::-1])
#  number = int(input('Introduceti un numar:'))
#  print(name1 * number)

#  Quest 4
# fruit = "Ananas"
# print('\n', fruit[0], '\n', fruit[1], '\n', fruit[3], '\n', fruit[4], '\n', fruit[5])
#
# print('Ana\nnas')
#
# print('An', ':', 'ana', ':', 's', sep='')
# print('An', '_', 'ana', '_', 's', sep='')
# print(fruit[1:3] * 4)

#  Exerctiul suplimentar
# 1
# word = input('Introduceti un cuvant: ')
# word1 = word.upper()
# reverse = word1[::-1]
# print('Cuvantul este palindrom?', word1 == reverse)
#
# #  2
# word = input('Introduceti un cuvant:')
# print('Cuvantul incepe cu majuscula?', word != word.isupper())


#  Cap 3


#  ex 6

#
# cuvant = list(input('Introduceti un cuvant:'))
# count = 0
# for i in cuvant:
#     if i == cuvant[0]:
#         count += 1
# print(count)


# cap 3
#  ex 5
# obiecte = ['Masa', 5, 'Scaun', 4.5, [5,6,7], 8]
# for i in obiecte :
#     print(f"Tipul obiectului {i} este:", type(i).__name__)

# ex 7

# lista = input('Introduceti lista de taskuri:')
# lista_taskuri = lista.split(",")
# print(lista_taskuri)
# for task in lista_taskuri:
#     if lista_taskuri.count(task) > 1:
#         lista_taskuri.remove(task)
# print(lista_taskuri)


# #  modul 3_2
# obiecte = ['abc', 123, '1', 1]
# for i in obiecte:
#     print(f"Tipul obiectului {i} este:", type(i).__name__)


# ex 2
# cuvant = input('Introduceti cuvant:')
# lista = cuvant.split()
# print(lista)
# consoane = 0
# for i in range(0, len(cuvant)):
#     if cuvant[i] not in ('a', 'e', 'i', 'o', 'u'):
#         consoane += 1
# print('Numarul consoanelor :', consoane)


# Modul 5

print('--'* 5, 'Va rugam sa introduceti un CNP valid si valorea bonului pentru a participa la tombola noastra', '--' * 5)
print('--'* 5,' ' * 10,'SUCCES!',' '*10, '--'* 5)

cnp = input('Introduceti CNP:')
anul_nasterii = int(cnp[1:3])
anul_curent = 2022
if len(cnp) != 13:
    print('CNP incorect')
    print(input('Reintroduceti CNP:'))
if int(cnp[0]) > 2:
    anul_nasterii += 2000
else:
    anul_nasterii += 1900
if anul_curent - anul_nasterii > 18:
    print(anul_curent - anul_nasterii > 18)
else:
    print('Sunteti minor')

from random import choice, sample

premiul1 = ['un suc', 'o punga de chipsuri', 'o caserola de prajituri']
premiul2 = ['un prajitor de paine', ' o consola de Gaming', 'o tastatura mecanica']
premiul3 = ['Un robot de bucatarie', ' o masina', choice(premiul1), choice(premiul2)]
bon = input('Introduceti valoarea bonului:')
if int(bon) > 0 and int(bon) < 100:
    print('Ati castigat:', choice(premiul1))
elif int(bon) >= 100 and int(bon) < 500:
    print('Ati castigat:', choice(premiul2))
else:
    print('Ati castigat:', choice(premiul3))
