#Methods used with list

#Creating a list
Colors = [ 'red' , 'blue' , 'green' , 'yellow']
print("Colors in Rainbow",Colors)

#append() method adds a single item to the existing list.
# The item will be added to the end of list.
Colors.append('indigo')
print("Color added to rainbow",Colors)

#insert() is used to insert the element/item at given index
Colors.insert(2,'orange')
print("List after inserting the color orange",Colors)

#remove() removes a given object from the list.
Colors.remove('orange')
print("List after removing the color orange",Colors)

#pop() removes and returns the value of given index.
Colors.pop(4)
print("\n popping color indigo",Colors)

#pop() without index will remove and return last item/element of list
Colors.pop()
print("popping without index",Colors)

#extend() function adds the specified list element to the end of current list.
Rainbow = [ 'orange' , 'indigo' , 'violet' , 'yellow']
Colors.extend(Rainbow)
print("\n After Extending-",Colors)

#reverse() is used to reverse the content of list.
Colors.reverse()
print("Reversed List -\n",Colors)

#count() returns the count of given element in a list.
count = Colors.count('red')
print("Number of counts",count) #output=1
count = Colors.count('black')
print("Number of counts",count) #output=0

#copy the content of one list to another
#Here content of list colors is being copied to new list called Rainbow.
Rainbow = Colors
print("\n New List Rainbow =",Rainbow)

#sort() allows use to sort the list in ascending order.
#Here the list is arranged in asc order considering the initials.
Rainbow.sort()
print("List in sorted order", Rainbow)


