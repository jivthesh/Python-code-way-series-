# creating a set:

fruits = {'apple', 'banana', 'grapes', 'cherry'}
print("The set of fruits : ", fruits)

# using add() method
fruits.add("avacado")  # using add() method
print("fruits set after adding", fruits)

# using update() method
fruits.update(["berries", "Mango"])  # using update() method
print("set after updation: ", fruits)

# using length() method
length = len(fruits)
print("The length of the fruits set is: ", length)

# using remove() method
fruits.remove("avacado")
print("The fruits set after removing ", fruits)

# remove the specific item/element
# discard/remove both can be used to remove item
# if the item which is to be remove is not present then remove will raise an error ,discard will not.
fruits.discard("cherry")
print("The fruits set after discarding ", fruits)

# using pop() method
fruits.pop()
print("The fruits set after performing a pop opearation: ", fruits)

# using clear() method
fruits.clear()
print("The set languages after using clear method: ", fruits)

