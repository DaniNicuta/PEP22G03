# value1 = '*' * 10
# print(value1)
# print("|", " " * 8, "|", end="\n", sep="")
# value2 = "*" * 10
# print(value2)
# print()
#
# for i in range(5):   # gasita pe Google
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


userWord = input('Please write a word:')
userWord = userWord.upper()

for letter in userWord:
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else :
        print(letter)