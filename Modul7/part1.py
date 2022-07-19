# # # objects
# #
# # class Keyboard:
# #     typed = ''
# #     shift_pressed = False
# #
# #     def press_shift(self):
# #         self.shift_pressed = True
# #         pass
# #
# #     def release_shift(self):
# #         self.shift_pressed = False
# #         pass
# #
# #     def press_a(self):
# #         if self.shift_pressed:
# #             self.typed +='A'
# #         else:
# #             self.typed += 'a'  # <- learn self
# #
# #     def how_is_self(self):
# #         print(id(self))
# #
# #
# # keyboard = Keyboard()
# #
# # print(type(keyboard))
# # print(f'valoarea este: {keyboard.typed}')
# # keyboard.press_a()
# # print(f'noua valoarea este: {keyboard.typed}')
# # keyboard.press_a()
# # print(f'noua noua valoarea este: {keyboard.typed}')
# # keyboard.how_is_self()
# # print(id(keyboard))
# #
# # # new keyboard
# # keyboard1 = Keyboard()
# # print(f'new keyboard - valoarea este: {keyboard1.typed}')
# # keyboard1.press_shift()
# # keyboard1.press_a()
# # keyboard1.release_shift()
# # print(f'new keyboard - noua valoare este: {keyboard1.typed}')
# #
# # #  class for store
# #
# # # - open shop with some products
# # # - add products
# # # - remove products
# #
# # class Shop:
# #
# #     def __init__(self, products):
# #         self.products = products
# #
# #     def add_products(self, name, quantity):
# #         try:
# #             self.products[name]
# #         except: KeyError
# #             self.products[name] = quantity
# #         else:
# #             self.products[name] = self.products[name] + quantity
# #     def remove_products(self, name):
# #         del self.products[name]
# #
# #
# # my_shop = Shop({'camera': 5, 'mouse': 2})
# # print(my_shop.products)
# # my_shop.add_products('keyboard', 3)
# # print(my_shop.products)
# # my_shop.remove_products('mouse')
# # print(my_shop.products)
# # my_shop.add_products('keyboard', 3)
# # print(my_shop.products)
# class Shop:
#     def __init__(self, products):
#         self.products = products
#
#     def add_product(self, name, quantity):
#         try:
#             self.products[name]
#         except KeyError:
#             self.products[name] = quantity
#         else:
#             self.products[name] = self.products[name] + quantity
#
#     def remove_product(self, name):
#         del self.products[name]
#
#
# my_shop = Shop({'camera': 5, 'mouse': 2})
# print(my_shop.products)
# my_shop.add_product('keyboard', 3)
# print(my_shop.products)
# my_shop.remove_product('mouse')
# print(my_shop.products)
# my_shop.add_product('keyboard', 2)
# print(my_shop.products)
#
#
# class RemoteControl:
#     press_on = True
#     press_plus = ''
#     press_minus = ''
#
#     def tv_on(self):
#         self.press_on = True
#
#     def tv_off(self):
#         self.press_on = False
#
#     def volume_up(self):
#         if self.press_plus:
#             self.press_plus += 1
#             if self.press_plus == 100:
#                 print('Volume maxim')
#
#     def volume_down(self):
#         if self.press_minus:
#             self.press_minus -= 1
#             if self.press_minus == 0:
#                 print('Mute')
#
#
# tv_remote = RemoteControl()
#
# print(f'Volume is:{tv_remote.volume_up()}')
# tv_remote.volume_up()
# print(f'Volume is:{tv_remote.volume_down()}')
# tv_remote.volume_down()
# print(f'Volume is:{tv_remote.volume_down()}')
