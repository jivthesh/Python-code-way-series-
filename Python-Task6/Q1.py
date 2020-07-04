driverSpeed = int(input("Enter your Speed:"))
def check_speed(driverSpeed):
    if(driverSpeed <= 70):
        return "OK"

    else:
        speed1=(driverSpeed-70)//5

        if(speed1<=12):
            return print(f"Point:{speed1}")

        else:
            return print("License Suspended")
# Calling the function
check_speed(driverSpeed)



