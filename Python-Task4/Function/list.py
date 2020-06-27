# Funcion to calculate square of a number

def squareNum(num):
    squarenum = num**2
    print("square of the num is :",squarenum)

# Function to calculate  max num in the lst

def maxNum(List):
    max = 0
    for i in List:
        if (max < i):
            max = i
    print("the max number in the list is :",max)

# Function to find min num in the list

def minNum(List):
    min = List[0]
    for i in List:
        if(min > i):
            min = i
    print("the min num in the list is :",min)

# Funcion to find the sum of numbers in the list

def sumofList(List):
    sum = 0
    for num in List:
        sum = sum + num
    print("sum of numbers in the list :",sum)
