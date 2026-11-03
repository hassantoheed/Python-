# exception handling:when you expect an error in your code and you want to deal with this error in simpler words error detection and handling

try:
    num1 = int(input("enter your 1st number "))
    num2 = int(input("enter your 2nd number "))
    print(num1 / num2)
except ZeroDivisionError:
    print("You have entered zero as number 2")
    print("This is not possible")
    print("division by zero is not possible")
except ValueError:
    print("You have entered an invalid number")
    print("This is not possible")

#1D array
student=[]
for i in range(0,5):
    name=input("enter your name")
student.append(name)

