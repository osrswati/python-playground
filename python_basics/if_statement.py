age = int(input('How old are you? '))

if age >= 18 and age <= 25:
  print('You are good to go')
else:
  print("Not allowed")
  

number = int(input('Enter you number: '))

if number >= 0:
  print('Potitive')
  if number % 2 ==0:
    print('Even number')
  else:
    print('Odd number')
else:
  print('Negative')
  
class_num = input('Please enter your Class number: ')
room_class = [1,2,3,4]

if class_num == 'A':
  print(f'Your room is {room_class[0]}')
elif class_num =='B':
  print(f'Your room is {room_class[1]}')
elif class_num == 'C':
  print(f'Your room is {room_class[2]}')
elif class_num == 'D':
  print(f'Your room is {room_class[3]}')
else:
  print('Please enter valid class number!')