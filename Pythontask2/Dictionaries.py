# Creating Dictionary
Car = { 'brand' : 'Ford', 'model' : 'Figo', 'year' : 2014}
print(Car)

# Accessing items
year = Car['year']
print("Year of car is ", year)

# Accessing items using get()
model = Car.get('model')
print("Model is ",model)

# Change value
Car['year'] = 2012
print(Car)

# Loop through Dictionary :: Print key names
for details in Car:
    print(details)

# Loop through Dictionary :: Print value names
for value in Car:
    print(Car[value])

# Same using values() method
for value in Car.values():
    print(value)

# Both keys and values
for k, v in Car.items():
    print(k, v)

# Check if key present
if 'year' in Car:
    print("Year in Car")

# length of dictionary
print(len(Car))

# Add items using new key
Car['colour'] = 'Red'
print(Car)

# POP
Car.pop('year')
print(Car)

# Delete using del
del Car['colour']
print(Car)

# Copy
new_Car = Car.copy()
new_Car['Price'] = 500000
print(new_Car)

# Using dict() to make copy
myCar = dict(new_Car)
print(myCar)

# Dictionary in Dictionary

myfamily = {
  "child1" : {
    "name" : "john",
    "year" : 2004
  },
  "child2" : {
    "name" : "peetter",
    "year" : 2007
  },
  "child3" : {
    "name" : "jithu",
    "year" : 2011
  }
}
print(myfamily)

# Using dict constructor
this_Car = dict(brand = 'Honda', year = '2009', price = 780546)
print(this_Car)

# Clear() Dictionary
Car.clear()
print(Car)
