#while

# number = int(input('Enter you number: '))

# while number != 0:
#   print(f'Your number is {number}')
  
#   number -= 1
# else:
#   print(f"You number now is {number}")
#   print('Completed!')

num = 1
sum = 0

print('Enter number for sum, Press \'0\' to exit.')

while num != 0:
  num = int(input('Enter number: '))
  sum = sum + num
  print('Current Sum:', sum)
else:
  print('Completed!')

#for

my_data = {
  "name":'Saraswati',
  "age":24,
  "mom":'Dewi',
  1:2
}

for i in my_data:
  # print(i) #key become iterable object
  print(my_data[i]) #iterable value 

for i in my_data.keys():
  print(i)
  

for i in my_data.values():
  print(i)

for key, value in my_data.items():
  print(f'The key is {key} and the value will be {value}')