#Q2
# initialize list of tuples
L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# removed empty tuples
L = [i for i in L if i]
print(L)
