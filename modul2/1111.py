# complex numbers
my_number = 1 + 4j
print(type(my_number))

my_number = 0 + 3j
print(type(my_number))
print(my_number)

print(2/3)  # 0.(6)

my_number = (-1)**(1/2)
print(my_number)
my_number = (-4)**(1/2)
print(my_number)


#  a*(x**x) + b*x + c = 0 # 3,4,5

a = 3
b = 4
c = 5
x = (-b + ((b ** 2 - 4 * a * c) ** (1 / 2))) / (2 * a)
print(x)


bool_object = True
print(type(bool_object))
print('Adress for bool:', id(bool_object))

print('Convert to bool:', bool(1))
print('Convert to int: ', int(True))

print('Convert to bool:', bool(0))
print('Convert to int: ', int(False))

print(True and False)
print(True or False)
print(1 or False)
print('False or 1 is:', False or 1)
print('False or 0 is:', False or 0)
print('True or 1 is:', True or 1)
print('a or 1 is:', 'a' or 1)
print('1 or a is:', 1 or 'a')
print(bool('a'))
print(bool(0), bool(0.0), bool(0+0j), bool(False), bool(''))
print(bool(' '), bool(True), bool(-100), bool(0.1), bool(0+2j))
print('True xor 1 is:', True.__xor__(1))
print('True xor True is:', True.__xor__(True))
print('True xor False is:', True.__xor__(False))
print('True xor 0 is:', True.__xor__(0))
print(not (True and True))
print(not (False and True))
print(not True and True)
print(not True and False)
print(not True or True)

# print('a'.__add__('b'))
