class IceCream():
  # pass
  def __init__(self):
    print('Ice Cream is created!')
    self.scoops = 3
  
  def eat(self, num_scoop_eat):
    # self.scoops = self.scoops - num_scoop_eat
    if self.scoops < num_scoop_eat:
      print('Not enough bites left!')
    else:
      self.scoops -= num_scoop_eat
    
  def add(self, num_scoop_add):
    self.scoops += num_scoop_add

my_ice_cream = IceCream()
# print(type(my_ice_cream))

print(f"Scoops of my ice cream: {my_ice_cream.scoops}")

my_ice_cream.eat(2)

print(f"Scoops of my ice cream: {my_ice_cream.scoops}")

my_ice_cream.add(4)

print(f"Scoops of my ice cream: {my_ice_cream.scoops}")

my_ice_cream.eat(6)

# my_ice_cream.eat(1)