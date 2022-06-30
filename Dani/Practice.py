# functii

# def my_function():  # incepe intodeauna cu def urmat de numele functiei si doua puncte
# exemplu1 functie def
# def message():
#     print("Enter a value: ")
#
# print("We start here.")
# message()
# print("We end here.")

#  eroare 2, functia trebuie definita inainte de a fi invocata, altfel va da o eroare
# print("We start here.")
# message()
# print("We end here.")
#
#
# def message():
#     print("Enter a value: ")

# eroare 2, nu trebuie sa fie o functie si o variabila cu ascelasi nume

# def message():
#     print("Enter a value: ")
#
# message = 1

# exemplu 2 functie def
# def message():
#     print("Enter a value: ")
#
# message()
# a = int(input())
# message()
# b = int(input())
# message()
# c = int(input())

#  functie care nu are nici un argumet
# def message():    # defining a function
#     print("Hello")    # body of the function
#
# message()    # calling the function


#  functie care ia argumente(un parametru)
# def hello(name):    # defineste functia
#     print("Hello,", name)    # body of the function
#
#
# name = input("Enter your name: ")
#
# hello(name)    # calling the function

#  eroare
# def hi():
#     print("hi")
#
# hi(5)
#  rezolvare
#
# def hi(number):
#     print("hi", number)
#
# hi(5)

# Functii
#
# def putere_doi(x):
#     print(x * x)
#     # return None  # implicit
#
# def putere_n(x, n):
#     return x ** n
#
# print(putere_doi(3))
#
# putere_doi(3)
#
# result = putere_n(4, 5)
# print(result)
#
# print(putere_n(3, 3))

# Argumente

# def putere_n(n, x, add=100, sub=0):
#     print('Valoare1 argument cheie', add)
#     print('Valoare2 argument cheie', sub)
#     print('Variabilele sunt: ', x, n)
#     return x ** n + add + sub
#
# putere_n(3, 4, add=201)
# putere_n(3, 4, 200)
# putere_n(3, 4, 200, 150)
# # putere_n(3, 4, add=200, 150)
# # print('Variabilele sunt: ', x, n) - local scope only

# # Variabile
#
#
# add1 = 200
# sub1 = 100
# div1 = 3
# def putere_n(n, x, add1=100, sub1=0):
#     print('Valoare1 argument cheie', add1)
#     print('Valoare2 argument cheie', sub1)
#     print('Variabilele sunt: ', x, n)
#     return (x ** n + add1 + sub1) / div1
#
# print(putere_n(3,3, 25, -25))
#
#
# add = 400
# sub = 200
# div = 2
# def putere_n1(n, x, add=100, sub=0):
#     print('Valoare1 argument cheie', add)
#     print('Valoare2 argument cheie', sub)
#     print('Variabilele sunt: ', x, n)
#     return (x ** n + add + sub) / div
#
# print(putere_n1(2,4, 30, -10))

# these vars are global
# add = 200
# sub = 100
# div = 3
#
# def putere_n(n, x, add=100, sub=0):
#     global div
#     print('Valoare1 argument cheie', add)
#     print('Valoare2 argument cheie', sub)
#     print('Variabilele sunt: ', x, n)
#     div = 5
#     return (x ** n + add + sub) / div
#
#
# print(putere_n(3, 3, 25, -25))
# print('Div result: ', div)

# Nested functions
# arg1 = 2
# def level1(arg1):
#     print('inainte de modificare', arg1)
#     def level2(arg2):
#         nonlocal arg1
#         arg1 = 10
#         print(arg2 + arg1)
#     level2(3)
#     print('dupa modificare', arg1)
#
# level1(1)
# print('variabila globala', arg1)

# tuples

# my_tuple = ("a", 1, None, 'a')
# print(type(my_tuple))
#
# # tuple methods
#
# result = my_tuple.count('a')
# print(f'Numarul de obiecte in tuple: {result}')
# print(len(my_tuple))
# # tuple slice
#
# result = my_tuple[1:3]
# print('slice:',result)
#
# # tuple slice
#
# result = my_tuple[0:2]
# print('slice:',result)
# result = my_tuple[0:3]
# print('slice:',result)
# result = my_tuple[1:3]
# print('slice:',result)
#
# # unpacking tuple
# var1, var2, var3, var4 = my_tuple
#
# print(var1, var2, var3, var4)
#
# # packing tuple
# var1, *var2, var3 = my_tuple
#
# print(var1, var2, var3)
#
# *var1, var2, var3 = my_tuple
#
# print(var1, var2, var3)
#
# # args as tuple
# def my_print(args, *args2):
#     print(type(args))
#     print(args)
#
#     print(type(args2))
#     print(args2)
#
#
# my_print('value1', 'value2', '123', 'abcd')  # dynamic number of arguments

# dictionary

# my_dict = {'key1': None, 123: 'abcd', True: (1, 2, 3)}

# print(my_dict)
# print(type(my_dict))

# # dict methods
# print(my_dict.keys())
# for key in my_dict.keys():
#     print(key)
#
# print(my_dict.values())
# for value in my_dict.values():
#     print(value)

# print(my_dict.items())
# for item in my_dict.items():
#     print(item)
#
# for key, value in my_dict.items():
#     print(key, value)
#
# result = my_dict.items()
# itered = result.__iter__()
# key, value = next(itered)
# print(key, value)
# key, value = next(itered)
# print(key, value)
# key, value = next(itered)
# print(key, value)

#
# def is_year_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True
#
#
# test_data = [1900, 2001, 2016, 1987]
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
#     yr = test_data[i]
#     print(yr, "-> ", end="")
#     result = is_year_leap(yr)
#     if result == test_results[i]:
#         print("leap year")
#     else:
#         print("not a leap year")

# def is_year_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True
#
#
# def days_in_month(year, month):
#     if year < 1582 or month < 1 or month > 12:
#         return None
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     res = days[month - 1]
#     if month == 2 and is_year_leap(year):
#         res = 29
#     return res
#
#
# def day_of_year(year, month, day):
#     days = 0
#     for m in range(1, month):
#         md = days_in_month(year, m)
#         if md == None:
#             return None
#         days += md
#     md = days_in_month(year, month)
#     if day >= 1 and day <= md:
#         return days + day
#     else:
#         return None
#
#
# print(day_of_year(2000, 12, 31))
# print(day_of_year(2001, 12, 31))


# def is_prime(num):
#     for i in range(2, int(1 + num ** 0.5)):
#         if num % i == 0:
#             return False
#     return True
#
# for i in range(1, 100):
#     if is_prime(i + 1):
#         print(i + 1, end=",")
# print()
