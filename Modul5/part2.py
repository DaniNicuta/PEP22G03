import pachet1


print((pachet1.my_var))

from pachet1 import my_var, my_function
print(my_var)
my_function

from pachet1.modul1 import my_function
my_function()

from pachet1 import *

from Modul5.part1 import my_math
print(my_math.pi)
