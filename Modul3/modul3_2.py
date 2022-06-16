#  for loop
# hello = 'Hello x Python'

# for letter in hello:
#     if 'x' == letter:
#         break
#     print(letter)
# else:
#     print('x is not present')

# for letter in hello:
#     if 'x' == letter:
#         continue
#     print(letter)
# else:
#     print('x was removed from string')

# my_number = 123
#
# for number in my_number:
#     if 'x' == number:
#         continue
#     print(number)
# else:
#     print('1 was removed from number')

#  how does for work
# hello = 'abc'
# iterated_object = hello.__iter__()
# print(iterated_object)
# print(next(iterated_object))
# print(next(iterated_object))
# print(next(iterated_object))
# #print(next(iterated_object))  # <- end of loop  (StopIteration)

# hello = 123
# iterated_object = hello.__iter__()
# print(iterated_object)
# print(next(iterated_object))
# print(next(iterated_object))
# print(next(iterated_object))
# print(next(iterated_object))  # <- end of loop  (StopIteration)


# hello = range(1, 11, 2)
# print(dir(hello))
# iterated_object = hello.__iter__()
# print(iterated_object)
# print(next(iterated_object))
# print(next(iterated_object))
# print(next(iterated_object))
# print(next(iterated_object))
# print(next(iterated_object))
# print(next(iterated_object))


# operatii pe biti
# Object type int
# -3 in bits = 11111101
# -2 in bits = 11111110
# -1 in bits = 11111111
# 0 in bits = 00000000
# 1 in bits = 00000001
# 2 in bits = 00000010
# 3 in bits = 00000011

#  and bits
# print(1 and 2)
# print(1 & 2) #  00000001 &
# #               00000010
# #    result     00000000 = 0
#
# # or bits
# print(-2 or 2)
# print(-2 | 2)#  11111110
# #               00000010
# #     result    11111110
#
# #  xor bits
# print(-3 ^ 3) #11111101
# #              00000011
# #              11111110 = -2
#
# print(-2 ^ 3)#11111110
# #             00000011
# #             11111110 = -3
#
# print((154 ^ 10) ^ 10)
# print((154 ^ 21) ^ 21)
# print((184 ^ 21) ^ 21)
#
# print(chr((ord('a') ^ ord('b')) ^ ord('b')))
#
# print(ord('d'))
# print(chr(100))


#  liste
my_var = 'abc'
# # my_list = ['a', 123, True,  my_var]
# #
# # for object_ in my_list:
# #     print(object_)
#
# #  print('#' * 100)
#
# my_list = ['a', 123, True,  my_var]
# # index    0      1    2     3
# #  index  -4     -3   -2    -1
# my_string = 'Hello Python'
# list_copy = my_list.copy()
# print('copied ID: ', [id(list_copy)])
# for object_ in list_copy:
#     print(id(my_list))
#     my_list.append(object_)  # list is mutable - do not do this
# print(my_list)


# for object_ in my_string:
#     print(id(my_string))
#     my_string += object_  # string is immutable - it can be changed while iterated
# print(my_string)

# x = [1, 2, 3, 4, 5, 6]
# for i in x:
#     print(x.pop(0))

my_list = ['a', 123, True,  my_var,'a']
print(my_list.count('a'))
print(my_list.append('b'), f'modified list: {my_list}')
print(my_list.remove('a'), f'modified list: {my_list}')
print(my_list.pop(3), f'modified list: {my_list}')
