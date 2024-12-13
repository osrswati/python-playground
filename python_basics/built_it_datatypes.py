#numeric
a = 2
b = 2.0
c = 2 + 0j
d = bool(1)
my_biner = 0b101
my_hexa = 0x5A1C
for value in (a,b,c,d,my_biner,my_hexa):
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

#set
my_set = {1,2,3,4}
my_set_2 = set(range(4))
print(my_set, my_set_2 )

#dictionary (mapping data type)
current_year = 2024
birth_year = 2000
my_dict = {'name' : 'Saraswati', 'age' : current_year-birth_year, 62 : "ID Phone"}

print(my_dict)
print(f'All keys are {my_dict.keys()}')
print(f'All values are {my_dict.values()}')
print(my_dict.items())

for key, value in my_dict.items():
  print(f'The key is {key} and the value will be {value}')