# Declaring and defining the function
def check_marks():
    # Taking user input
    studentMark = int(input("Enter the marks:"))

    # Using try and catch blocl
    try:
        if (studentMark < 90):
            raise Exception

    except Exception:
        print("Not Eligible!!!")
    else:
        print("Eligible")

    # calling the function


check_marks()
