import random
lowerlimit = 5
upperlimit = 20
age=random.randint(lowerlimit,upperlimit)
print("Hello i am LGS____BoT,Let me guess your age")
print("I think your age is",age)
print("Press 1 if i was correct")
print("Press 2 if you Younger")
print("Press 3 if you older")

choice=int(input("Enter your choice: "))
if choice==1:
    print("I genius")
elif choice==2:
    print("You are Young fella")
    lowerlimit=age
    age=random.randint(lowerlimit,upperlimit)
    print("Then you must be",age,"years old")
elif choice==3:
    print("You are Older fella")
