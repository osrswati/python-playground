class SarasData():
  
  def __init__(self):
    self.name = 'Saraswati'
    self._birth_year = 2000
    self.__mom = 'Dewi' #private attributes
    self.__get_dad()
  
  def get_mom(self): #access private attributes
    return self.__mom
    
  def __get_dad(self):
    print("This is private method")
  
  def get_dad(self):
    self.__get_dad()

my_data = SarasData()

print(my_data.name)
print(my_data._birth_year)
# print(my_data.__moms) #private attributes

print(my_data.get_mom())

# print(my_data.__get_dad()) #private method

print(my_data.get_dad())