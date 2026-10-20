#while loops the conditional loop

choice=True
while choice==True:
    print("Welcome to the LGS Gulberg")
    choice=input("Would you like to play again?(y/n) ").lower()
    print(choice)


#counting

count=0
num=0
while count!=-1:
    count+=1
    count=int(input("Enter a number:"))
    print("Loops Ran for",count,"Number of times")

#write a program that will ask for numbers and check how many numbers were even numbers till a negative number is entered
n4=int(input("Enter a number:"))
count=0
while n4>0:
    if n4%2==0:
        count+=1
        num=int(input("Enter a number:"))
        print("Even Count was",count)

#write a program that will ask for numbers till 999 is entered count how many positive and negative

n3=int(input("Enter a number:"))
countp=0
countn=0
while n3!=999:
    if n3>0:
        countp+=countp
    else:
        countn+=countn
        num=int(input("Enter a number: "))
print("Positive numbers",countp)
print("Negative numbers",countn)

while True:
    n1=int(input("enter a number 1"))
    n2=int(input("enter a number 2"))
    op=input("Enter your operator +,-,*,/")
    if op=="+":
        print(n1+n2)
    elif op=="-":
        print(n1-n2)
    elif op=="*":
        print(n1*n2)
    elif op=="/":
        print(n1/n2)
    else:
        print("Invald operation")
    choice=input("Enter your choice yes/no").lower()

