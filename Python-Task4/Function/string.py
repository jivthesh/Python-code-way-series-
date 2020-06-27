#declaring a functionto find middle character of string

def  find_middle_character(String):
    input1 = String[(len(String) - 1) // 2:(len(String) + 2) // 2]
    print("Middle character in a string :", input1)

#declaring a function to find length of a string

def length_of_string(String):
    length = 0
    for s in String:
        length = length + 1
    print("Length of the input string is:\n ", length)

#declaring a function to find number of vowels in a string

def Vowel_in_string(String):
    # string = input("Enter a string to print no of vowels :")
    vowels = 0
    for i in String:

        if (
                i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            vowels = vowels + 1
    print("Number of vowels are:\n",vowels)

