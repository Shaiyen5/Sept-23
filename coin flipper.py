import random 
random_float = random.random()
print(random_float)

# this prints for random floats within 0 to 1 

print("1 is for Heads, and 0 is for tails")
dice = random.randint(0,1)
if dice == 1:
    print(f"you got a {dice} which is Heads")
else:
    print(f"you got a {dice} which is Tails")