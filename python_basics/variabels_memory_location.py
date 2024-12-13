x = 10000
y = 10000
p = "Saraswati"
q = "Saraswati"
a = [1,2,3]
b = [1,2,3]

var =[("x", x), ("y", y), ("p", p), ("q", q), ("a", a), ("b", b)]

for name, value in var:
  print(f"Variable {name} with value {value} and the memory location is {id(value)}")

# print(id(x), id(y), id(z), id(p))
# range(4)