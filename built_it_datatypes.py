#numeric

a = 2
b = 2.0
c = 2 + 0j
d = bool(1)

for value in (a,b,c,d):
  print(f"Data type of {value} is {type(value)}")