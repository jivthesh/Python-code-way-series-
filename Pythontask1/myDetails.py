# Q2] Program to display my details

#Taking information from the user

#Input for name

firstname = input('Enter your First name :')
lastname = input ('Enter your Last name :')

#Input collage name with address

collegename = input('Enter your College Name :')
collegeaddress = input('Enter your College Address :')

#Input for marks of 5 subject

subject1 = float( input("Enter marks of DSA: "))
subject2 = float( input("Enter marks of operating system: "))
subject3 = float( input("Enter marks of Computer Networks: "))
subject4 = float( input("Enter marks of Compiler Design: "))
subject5 = float( input("Enter marks of Pervasive computing: "))


#String concatenation for full name

FullName = firstname + " " + lastname

#String concatenation for college
College = collegename + "," +collegeaddress

#Calculating total marks and percentage

TotalMarks = subject1 + subject2 + subject3 + subject4 + subject5
Percentage = ( TotalMarks / 5)

#Displaying the information

print("Name : ",FullName)
print("College: ",College)
print("Total marks obtained: ",TotalMarks)
print("Percentage: ",Percentage)


