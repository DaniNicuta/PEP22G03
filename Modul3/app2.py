# my_test = 'Hello Python'
# key = 'A'
# encrypted_text = ''
# for letter in my_test:
#     letter_code = ord(letter)
#     encrypted_letter = chr(letter_code ^ ord(key))
#     encrypted_text += encrypted_letter
# print(encrypted_text)
# decrypted_text = ''
# for letter in encrypted_text:
#     letter_code = ord(letter)
#     encrypted_letter = chr(letter_code ^ ord(key))
#     decrypted_text += encrypted_letter
# print(decrypted_text)

# cuvant = list(input('Introduceti un cuvant:'))
# count = 0
# for letter in cuvant:
#     if letter == cuvant[0]:
#         count += 1
# print('Prima litera apare de',count, 'ori')

# obiecte = ['Masa', 5, 'Scaun', 4.5, [5,6,7], 8]
# for i in obiecte :
#     print(f"Tipul obiectului {i} este:", type(i).__name__)


lista = input('Introduceti lista de taskuri:')
lista_taskuri = lista.split(",")
print(lista_taskuri)
# for task in lista_taskuri:
#     if lista_taskuri.count(task) > 1:
#         lista_taskuri.remove(task)
# print(f'Lista de taskuri: {lista_taskuri}')
for task in lista_taskuri.copy():
    lista_taskuri.count(task)
    print(f'Taskul: {task} se regaseste de {lista_taskuri.count(task)}')
    if lista_taskuri.count(task) > 1:
        lista_taskuri.remove(task)
print(lista_taskuri)