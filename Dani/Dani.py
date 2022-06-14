# value1 = '*' * 10
# print(value1)
# print("|", " " * 8, "|", end="\n", sep="")
# value2 = "*" * 10
# print(value2)
# print()
#
# for i in range(5):
#     print('*' * 10, end='\n', sep='')
#
# print(4**-1)
# print(15 - 1 * (5 * (1 + 2)))
# print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
# print((2 % -4), (2 % 4), (2 ** 3 ** 2))
# print((2 ** 4), (2 * 4.), (2 * 4), '\n')
# a = 3.0
# b = 4.0
# c = (a ** 2 + b ** 2) ** 0.5
# print("c =", c, '\n')

# x = 0
# x = float(x)
# y = 3 * x * x * x - 2 * x * x + 3 * x - 1
# print('y =', y)
#
# x = 1
# x = float(x)
# y = 3 * x * x * x - 2 * x * x + 3 * x - 1
# print('y =', y)

# x = -1
# x = float(x)
# y = 3 * x * x * x - 2 * x * x + 3 * x - 1
# print('y =', y)

# animal = input('Please choose animal:')
#
# while animal != 'chupacabra':
#     if animal == 'chupacabra':
#         break
#     else:
#         print('wrong animal, try again')
#         animal = input('Please choose again:')
# else:
#     print("You've successfully left the loop.")


# userWord = input('Please write a word:')
# userWord = userWord.upper()
#
# for letter in userWord:
#     if letter == 'A':
#         continue
#     elif letter == 'E':
#         continue
#     elif letter == 'I':
#         continue
#     elif letter == 'O':
#         continue
#     elif letter == 'U':
#         continue
#     else :
#         print(letter)


# word_without_vowels = ''
# userWord = input('Enter a word:')
# userWord = userWord.upper()
#
# for letter in userWord:
#     if letter in 'AEIOU':
#         continue
#     word_without_vowels = word_without_vowels + letter
# print(word_without_vowels)


# blocks = int(input('Enter the number of blocks:'))
# height = 0
# while blocks > height:
#     height = height + 1
#     blocks = blocks - height
# print('The height of the pyramid:', height)



# for digit in "0165031806510":
#     if digit == "0":
#         print("x", end="")
#         continue
#     print(digit, end="")
# print()
# for digit in "0165031806510":
#     if digit == "1":
#         print("x", end="")
#         continue
#     print(digit, end="")

#
# hat_list = [1, 2, 3, 4, 5]
#
#
# hat_list[2] = int(input("Enter an integer number: "))
# del hat_list[4]
# print('The length of the list:' , len(hat_list))
#
# print(hat_list)

# my_list = []  # Creating an empty list.
#
# for i in range(5):
#     my_list.append(i + 1)
#
# print(my_list)
#
#
# my_list = []  # Creating an empty list.
#
# for i in range(5):
#     my_list.insert(0, i + 1)
#
# print(my_list)

# my_list = [1, None, True, 'I am a string', 256, 0]
# print(my_list[3])  # outputs: I am a string
# print(my_list[-1])  # outputs: 0
#
# my_list[1] = '?'
# print(my_list)  # outputs: [1, '?', True, 'I am a string', 256, 0]
#
# my_list.insert(0, "first")
# my_list.append("last")
# print(my_list)  # outputs: ['first', 1, '?', True, 'I am a string', 256, 0, 'last']

# 1
# print("Astazi ma duc la \"facultate\"")
# print("/*\/*\*/*\/*\\", "Python", "\./\./\./\./", sep="\n")
# print("P\ty\tt\th\to\tn")
# var = input('Textul este:')
# print(var[::-1])


# 2
# user_name = input("introduceti nume utilizator:")
# age = input("introduceti varsta:")
# print("Cum te numesti?", user_name)
# print("Ce varsta ai?", age)
# print(f"Ceau {user_name}! Te-ai nascut in {2022 - int(age)}")

# 6
# a) Hello_Python
# text = "Hello Python"
# print(text[:5], "_", text[6:], sep="")
#
# # b) Hello Python.
# print('Hello', 'Python', end='.')
#
# # c) HelloHelloHelloHello
# text = "Hello Python"
# print(text[:6] * 4)
#
# # 7
# a = 5.
# b = 5
# c = "ana"
# print(hex(id(a)), type(a))
# print(hex(id(b)), type(b))
# print(hex(id(c)), type(c))

# my_text = "My Python3 Course"
#         #  0123456789
#
# # Slice with single value
# print(my_text)
# print(my_text[9])
#
# # Slice with start and stop value
# print(my_text[3:9])
# print('No start value: ', my_text[:9])
# print('No stop value: ', my_text[3:])
# print('With stop value: ', my_text[3:17])
#
# # Slice with start stop and step value
# print(my_text[3:9:1])
# print(my_text[3:9:2])
# print(my_text[3:9:2])
#
# print('No start value: ', my_text[:9:2])
# print('No stop value: ', my_text[3::2])
# print('No step value: ', my_text[3:9:])


# # Normal string
# normal1 = "Normal string \n"
# normal2 = 'Normal \n string'
#
# # Multiline string
# normal1 = """Normal string \n
# New line"""
# print(normal1)
# normal2 = '''Normal
#              string'''
# print(normal2)
#
# # raw string
# normal1 = r"""Normal string \n
# New line"""
#
# print(normal1)
#
# # formatted string
# var1 = "insert"
# normal1 = f"""Normal string {var1}
# New line"""
#
# # replace method
# var1 = "insert insert insert"
# var1 = var1.replace('ins', '_', 2)
# print('Replaced i: ', var1)

#
# my_text = "My Python3 Course"
# #           -5-4-3-2-1
#
#
# # # Slice with single negative value
# print(my_text)
# print(my_text[-2])
#
# # Slice with start and stop value
# print(my_text[-3:-1])
# print('No start value: ', my_text[:9])
# print('No stop value: ', my_text[3:])
# print('With stop value: ', my_text[3:17])
#
# # Slice with start stop and negative step value
# print(my_text[-1:-5:-1])
# # print(my_text[-1:-5:0])
#
# print('No start value: ', my_text[9::-1])
#
# # String methods and functions
#
# # len() function
# my_string = "Hello Python"
# print('Length is : ', len(my_string))
# print('Length is : ', my_string.__len__())
#
# my_string = ""
# print('Length is : ', len(my_string))
#
# # Format
#
# my_string = "Hello Python {}"
#
# print('Formatted text: ', my_string.format('abcd'))
#
# my_string = "Hello Python {0} {1} {2}"
#
# print('Formatted text: ', my_string.format('a', 'b', 'c'))
#
# my_string = "Hello Python {enva} {envb} {envc}"
#
# print('Formatted text: ', my_string.format(enva='a', envb='b', envc='c'))

# var1 = "insert arici masina"
# var1 = var1.replace('i', '|', 4)
# print('Replaced i: ', var1)