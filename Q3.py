#Q3
def string_test(string):
    UL = {"UPPER_CASE":0, "LOWER_CASE":0}
    for i in string:
        if i.isupper():
           UL["UPPER_CASE"]+= 1
        elif i.islower():
           UL["LOWER_CASE"]+= 1
        else:
           pass
    print ("Original String : ", string)
    print ("No. of Upper case characters : ", UL["UPPER_CASE"])
    print ("No. of Lower case Characters : ", UL["LOWER_CASE"])

string_test('My Name Is Jivthesh.')
