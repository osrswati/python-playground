class TestInit():
  
  def __init__(self): #self for consistency (standard keyword for instance), you can use any words
    print('This is first init')
    
  def __init__(self, name):
    self.name = name
    print(f'Hi {self.name}, This is our second init') #python only use one constructor and the last will be running
  
first_test = TestInit("Saras")
