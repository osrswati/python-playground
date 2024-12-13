#Input
# your_name = input("What is your name? ")
# current_year = 2024
# birth_year = int(input("In what year you were born? "))
# age = current_year - birth_year

# print('Hello,', your_name, f"Your age is {age}")

#Output
#concatenate
num = 2
print('Dua' + 'ini' + str(num))

#f.
my_name = 'Saraswati'
my_age = 24

print(f'My name is {my_name} and my age is {my_age}')

#.format()
mom = 'Dewi'
note = 'best'
print('My mom is {} and she is the {} mom ever!'.format(mom, note))
print('My mom is {1} and she is the {0} mom ever!, {2}'.format(note, mom, note+mom))

#string formatting with %
num_div = 10/3
# print(num_div.%f)
print("Hello %s" %my_name + "My mom is %s" %mom)
print("The value is %.2f" %num_div)
print("The value is %d" %num_div)