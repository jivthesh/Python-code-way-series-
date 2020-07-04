# Q4

def countOccurences(str):
    for i in str:
        str = str.lower()
    print("number of occurences:", (str.count("at")))


str = input("String:")
countOccurences(str)
