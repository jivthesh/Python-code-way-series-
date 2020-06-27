# A  code for matrix input from user 

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

# Initialize matrix 
matrix = []
print("Enter the entries rowwise:")

# For user input 
for i in range(R):  # A for loop for row entries
    a = []
    for j in range(C):  # A for loop for column entries
        a.append(int(input()))
    matrix.append(a)

# For printing the matrix 
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()

# Prime Numbers in the created matrix
print("\nThe prime Numbers in the matrix are: ")
for i in range(R):
    for j in range(C):

        # If given element of matrix is greater than 1
        if( matrix[i][j] > 1):

            # Iterating from 2 to no_of_Row / 2
            for p in range(2, matrix[i][j]):

                # If matrix[i][j] is divisible by any number between 2 and Row / 2, it is not prime
                if(matrix[i][j] % p) == 0:
                    break
            else:
                # Printing the element of the matrix which is a prime number
                print(matrix[i][j])


