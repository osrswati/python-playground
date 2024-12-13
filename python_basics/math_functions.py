list_of_function = dir(__builtins__)
print(f'Total built-it function is {len(list_of_function)}')

import math

print(f'Total function in math module is {len(dir(math))}')

print(dir(math))

num = 9
num_sqrt = math.sqrt(num)
print(num_sqrt)