# name = input("What is your name? ")
# age = int(input("How old are you? "))
# marks= int(input('Please input your marks: '))

class InputData():
  
  def __init__(self, name, age=None, **marks): #self always be the first parameter, set default value
    self.name = name
    self.age = age
    self.marks = marks
  
  def display(self):
    print("Hi", self.name)
    print("Your age", self.age)
    print("Your marks:", self.marks)

# data1 = InputData(name, age, marks)

# data1.display()

data2 = InputData("Jasika", 18, science = 78, sports =94)

data2.display()