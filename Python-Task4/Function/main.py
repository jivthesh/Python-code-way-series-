import list
import string
import Logopertion

# LIST

print("*************Function of list***********")

List = [1, 2, 3, 4, 5]
list.squareNum(6)
list.maxNum(List)
list.minNum(List)
list.sumofList(List)
print()

# STRING
print("************Functions of string*************")

String = input("Enter the string :")
string.find_middle_character(String)
string.length_of_string(String)
string.Vowel_in_string(String)

#logical operators
print("************Functions of Logicaloperatos*************")

x = int(input("enter the first number: "))
y = int(input("enter the second number: "))
Logopertion.Andoperator(x, y)
Logopertion.Oroperator(x, y)
Logopertion.Notoperator(x, y)

