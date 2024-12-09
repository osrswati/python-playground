number = list(range(11))

for i in number:
  if i == 5:
    # continue #skip number 2
    break #stop if number 5
  print(i)

print("-----------------")

num = 0
while num < 5:
  num += 1
  if num == 3:
    continue #skil number 3
  print(num)