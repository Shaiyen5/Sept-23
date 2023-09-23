# year checker 
year = int(input("what year are you checking for?\n "))
even1 = year % 4
even2 = year % 100
even3 = year % 400
if even1 == 0:
    print("This year is a leap year")
elif even2 == 0:
    print("This year is not a leap year")
elif even3 == 0:
    print("This year is a leap year")
else:
    print("This year is not a leap year")