my_biodata = {
  'name' : 'Saraswati',
  'age' : 24,
  'hobby' : 'Reading',
  123 : 456
}

print(my_biodata)

my_biodata['age'] = 25
my_biodata.update({'name' : 'Saraswati Dewi'})

print(my_biodata)
print(f'All the keys is {my_biodata.keys()} and the value will be {my_biodata.values()}')

# index, value = my_biodata.items() => error harus looping
# print(my_biodata.items())

print(my_biodata.get('name'))

my_biodata.pop(123)
print(my_biodata)

my_biodata.popitem()
print(my_biodata)