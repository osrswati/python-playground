#Parent Class
class Polygon():
  #class variable
  __width = None
  __height = None
  
  def set_value(self, width, height):
    self.__width = width
    self.__height = height
    
  def get_width(self):
    return self.__width

  def get_height(self):
    return self.__height

#Child Class
class Square(Polygon):
  
  def area(self):
    return self.get_width() * self.get_height()

class Triangle(Polygon):
  
  def area(self):
    return self.get_width() * self.get_height() * 1/2


my_square = Square()
my_square.set_value(8,7)

print(my_square.area())

my_triangle = Triangle()
my_triangle.set_value(8,10)

print(my_triangle.area())