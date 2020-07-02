#Import math Library

import math

#returns the squareroot of number

num=int(input("Enter a number:"))
print(math.sqrt(num))

#return the ceil value

Num=float(input("Enter a float number:"))
print(math.ceil(Num))

#return the floor value

print(math.floor(Num))


#sorting the list

print("\nSorting of List:")
Sort_List=[9, 4, 2, 6, 1]
print("Original List:", Sort_List)
Sort_List.sort()
print("List after sorting:", Sort_List)

#sorting the tuples

print("\nSorting of Tuples:")
Sort_Tuple = (8, 9, 6, 7, 4)
print("Original Tuple list:", Sort_Tuple)
new_tuple = sorted(Sort_Tuple)
print("Sorted tuple:", new_tuple)


#sorting of set

print("\nSorting of Set:")
sortSet = {'science', 'History', 'English', 'Reading'}
print("Original set:", sortSet)
print("Sorted List from Set = ", sorted(sortSet))


#sorting of Tuple :

print("\nSorting of Tuple:")
sortTuple = {'science', 'History', 'English', 'Reading'}
print("Original set:",sortTuple )
print("Sorted List from Set = ", sorted(sortTuple))

