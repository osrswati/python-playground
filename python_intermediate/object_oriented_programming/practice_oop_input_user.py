# name = input("What is your name? ")
# age = int(input("How old are you? "))
# marks= int(input('Please input your marks: '))

class InputData():
  #class variabels
  total_student = 0
  
  def __init__(self, name, age=None, **marks): #self always be the first parameter, set default value
    self.name = name
    self.age = age
    self.marks = marks
    InputData.total_student += 1
  
  def display(self):
    print("Hi", self.name)
    print("Your age", self.age)
    print("Your marks:", self.marks)

data1 = InputData("Saras", 24, science=80)

# data1.display()

data2 = InputData("Jasika", 18, science = 78, sports =94)

print(InputData.__dict__)