# INT
number = 3
print(type(number))
print('Address for number :', id(number))

number = int('3')
print('Address for int:', id(number))
print('Nr as text', type(number))

# Float
number = 3.1
print(type(number))
print('Address for int:', id(number))

number = float('3.1')
print('Nr as text', type(number))
print('Address for float:', id(number))
# bool
bool_object = True
print(type(bool_object))

print('Address for bool:', id(bool_object))

print('Convert to bool:', bool(1))
print('Convert to int: ', int(True))

print('Convert to bool:', bool(0))
print('Convert to int: ', int(False))

print(True and False)

print(5//2)  # rezultatul impartirii fara rest
print(5/2)  # impartire
print(13 % 5)  # restul impartirii

#  aria triunghiului
a = 10
b = 7
print(a * b/2)


# Input

my_value = input()
print('you entered: ', my_value)

password = 7710
passinput = int(input('enter password: '))
result = password == passinput
print(result)

number1 = int(input('Number 1 is: '))
number2 = int(input('Number 2 is: '))

print('Media numerelor: ', (number1 + number2)/2)

venit = int(input('Venit :'))
cheltuieli = 50 * venit/100
hobby = 15 * venit/100
economii = 10 * venit/100
print('Buget alocat pentru cheltuieli:', cheltuieli)
print('Buget alocat pentru hobby:', hobby)
print('Buget alocat pentru economii:', economii)


# complex numbers


my_number = 1 + 4j
print(type(my_number))


# a*(x**x) + b*x + c = 0
