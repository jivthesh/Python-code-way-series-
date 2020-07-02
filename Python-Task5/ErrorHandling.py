try:

    # taking inputs from user
    num1 = int(input("Enter any number:"))
    num2 = int(input("enter any number:"))

    Result = num1 + num2
    print(Result)

    # created raise just to check working
    raise Exception("Error:try is executed succesfully")

# if above code failed exception will be printed
except Exception as e:
    print(e)
finally:
    print("program is finally executed")
