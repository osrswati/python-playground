class Student():
  def __init__(self):
    self.name = 'Saraswati'
    self.age = 24
    self.marks = 85
    
  def talk(self):
    print(f'Hello my name is {self.name} and I"m {self.age} years old')
    
student_1 = Student()
print(student_1.name)
print(student_1.talk())

student_2 = Student()
student_2.name = 'Jasika'
student_2.age = 12
print(student_2.name)
print(student_2.talk())