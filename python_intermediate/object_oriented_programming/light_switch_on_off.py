class Light:
  def __init__(self):
    print("Light is created!")
    self.on = False
    
  def toggle(self):
    # if self.on:
    #   self.on = False
    # else:
    #   self.on = True
    self.on = not self.on
  
  def is_on(self):
    # if self.on:
    #   print("Light is on")
    # else:
    #   print("Light is off")
    return self.on
    
check_light = Light()

print(check_light)
print(check_light.is_on())

print("Is light on? ", check_light.on)
check_light.is_on()

check_light.toggle()

print("Is light on? ", check_light.on )

print(check_light.is_on())