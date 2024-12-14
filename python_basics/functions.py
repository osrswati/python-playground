#Create a function
def sum_func(a,b):
  if type(a) == type(b):
      return a + b
  else:
    print('Datatypes are different, try again!')

sum_calc = sum_func(2,2)

print(sum_calc)

#Different of arguments
  #position
  #keyword
  #default
  #length arguments
  
def data_user(name, age="'Please input your age'"):
  print(f'Your name is {name} and your age is {age}')

print(
  #position
  data_user('Saraswati', 24), 
  data_user(23, 'Saraswati'),
  #keyword
  data_user(age=23, name='Saraswati'),
  #default
  data_user('Saras')
)

#lenth arguments
def data_student(name, clas, mark):
  print(f"Your Name: {name}")
  print(f"Your Class: {clas}")
  print(f"Your Marks: {mark}")

print(data_student('Saraswati', 'Science Two', 90))

#single
def data_student(name, clas, *mark):
  print(f"Your Name: {name}")
  print(f"Your Class: {clas}")
  print(f"Your Marks: {mark}")

print(data_student('Saraswati', 'Science Two', 90,100,99,85))

#doulbe *
def data_student(name, clas, **mark):
  print(f"Your Name: {name}")
  print(f"Your Class: {clas}")
  # print(f"Your Marks: {mark}")
  print("Marks:")
  for index, value in mark.items():
    print(index, value)

print(data_student('Saraswati', 'Science Two', Math=90, English=100, Chemistry=99, Physics=85))


#global variabels
def sum_func(a,b):
  global c
  if type(a) == type(b):
      c = a + b
  else:
    print('Datatypes are different, try again!')
  
sum_func(7,8)

print(c)