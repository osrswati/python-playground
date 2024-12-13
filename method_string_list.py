#string
nickname = 'Saras'
full_name ='Saraswati'
another_text = 'Saraswati Dewi Lala         '

print(nickname.replace('S', 'W'))
print(nickname.lower()
      ,nickname.upper()
      ,nickname.lower()
      ,another_text.split(" ")
      ,full_name.capitalize()
      ,another_text.lstrip()
      )

#list
mom_order = ['Banana', 'Banana', 'Papaya', 'Rice', 'Sugar']
list_num = [1,24,66,3,4,12,1]

mom_order.append('Chitato')
print(mom_order)

mom_order[1] = 'Element 1'
print(mom_order.index("Banana"))

mom_order.insert(1,'Yogurt')
print(mom_order)

mom_order.pop()
print(mom_order)

mom_order.pop(0)
print(mom_order)

list_num.sort() #running in place

print(list_num)

list_num.reverse() #running in place

print(list_num)

#built it function
print(sorted(list_num), len(mom_order))
print(f'Freq value is : {list_num.count(1)}')

list_num.clear()
print(list_num)

print(mom_order)
mom_order.remove("Sugar")
print(mom_order)

# del mom_order
del mom_order[2]

print(mom_order)


