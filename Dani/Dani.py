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