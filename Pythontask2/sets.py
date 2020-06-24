# working with sets

# creating a set
myset = {1,2,3,4,5,6,7,8,9}


# maximum element in the set
setmaximum = max(myset)					
print(setmaximum)


# minimum element in the set
setminimum = min(myset)
print(setminimum)


# looping in sets
for x in myset:
    print(x)

# length of the set
setlength = len(myset)
print(setlength)

					
# adding element in the list 
myset.add(5)
print(myset)


# adding multiple elements in the list
firstupdate = myset.update([34,67,65,87])
print(myset)


# copying the set
nextset = myset.copy()
print(nextset)



nextset = {5,6,7,8,9}
nextset_1 = {2,3,4,5,6}

# intersection of the elements in the set
mysetintersection = myset.intersection(nextset , nextset_1)
print(mysetintersection)


#difference of the elements in the set
mysetdifference = myset.difference(nextset)	
print(mysetdifference)


# resulting the whole set
unionSet = myset.union(nextset,nextset_1)
print(unionSet)
