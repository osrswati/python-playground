#numeric
a = 2
b = 2.0
c = 2 + 0j
d = bool(1)

for value in (a,b,c,d):
  print(f"Data type of {value} is {type(value)}")

#sequence
#string
full_name = 'Saraswati'

for index in range((9)):
  print(f'Char no-{index} is {full_name[index]}')

#list
my_list = [1, "satu", True, [1,2,3]]
print(my_list, list("saras"))

#tuple
my_tuple = (2, "dua", True)
print(my_tuple, tuple([1,2,3]), tuple('saras'))

#range()
my_range = list(range(10))
range_step_two = list(range(1,10,2)) #start, stop, step
print(my_range,range_step_two )