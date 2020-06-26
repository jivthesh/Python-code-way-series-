# function name

def fullName():
    Name = input("Enter your name :")
    print("your name is", Name)


# function marks
def totalMarks():
    subject1 = float(input("Enter marks of DSA: "))
    subject2 = float(input("Enter marks of operating system: "))
    subject3 = float(input("Enter marks of Computer Networks: "))
    subject4 = float(input("Enter marks of Compiler Design: "))
    subject5 = float(input("Enter marks of Pervasive computing: "))
    global totalMarks
    totalMarks = subject1 + subject2 + subject3 + subject4 + subject5
    print("TotalMarks = ", totalMarks)


# function percentage
def findPercentage():
    global findPercentage
    findPercentage = (totalMarks) / 5
    print("percentage = ", findPercentage)


# function grade
def findGrade():
    if (findPercentage >= 95):
        print("Grade  A")
    elif (findPercentage >= 85 and findPercentage <= 95):
        print("Grade B")
    elif (findPercentage >= 75 and findPercentage <= 85):
        print("Grade C")
    elif (findPercentage >= 65 and findPercentage <= 75):
        print("Grade D")
    else:
        print("Failed")


# Funtion calling other function:

def studentDetails():
    fullName()
    totalMarks()
    findPercentage()
    findGrade()

studentDetails()

