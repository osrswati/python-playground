class Light():
  
  def __init__(self):
    self.on = False

#instantiate the light class
a = Light()
b = Light()

print(a.on)

a.on = True

print(a.on)