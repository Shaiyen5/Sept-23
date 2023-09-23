import random 
name_string = "Daniel, John, Jonah, Josh, Stuart, Greg, Fatima, Aisha"
# the reason why we used the split function was assuming that names_string was gonna be an input 
names = name_string.split(", ")
print(names)
random_integer = random.randint(1,8)

if random_integer == 1:
    print(f"The waiter picked 1 {names[0]} is paying tonight's bill")
elif random_integer == 2:
    print(f"The waiter picked 2 {names[1]} is paying tonight's bill")
elif random_integer == 3:
    print(f"The waiter picked 3 {names[2]} is paying tonight's bill")
elif random_integer == 4:
    print(f"The waiter picked 4 {names[3]} is paying tonight's bill")
elif random_integer == 5:
    print(f"The waiter picked 5 {names[4]} is paying tonight's bill")
elif random_integer == 6:
    print(f"The waiter picked 6 {names[5]} is paying tonight's bill")
elif random_integer == 7:
    print(f"The waiter picked 7 {names[6]} is paying tonight's bill")
else:
    print(f"The waiter picked 8 {names[7]} is paying tonight's bill")
