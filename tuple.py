#tuple
tuple_num = (1,2,3,4)
fullname = ('Hello')
fullname_2 = ('Hello',)

print(tuple_num, fullname, type(fullname), type(fullname_2))

tuple_num_2 = (4,5,6)

new_tuple =  tuple_num + tuple_num_2
print(new_tuple)

print(fullname_2*5)
print(new_tuple*2)

print(max(tuple_num), min(tuple_num))

del(tuple_num)

