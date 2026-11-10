#all this is using procedures
#print subroutine
def Display(Output):
    print(Output)
#array
Array=[56,12,45,98,77,10]
#bubble sort
def bubblesort():
    top=len(Array)-1 #Numberofswaps
    Swap=True
    Display(Array)
    while Swap==True and top>0:
        Swap=False
        for index in range(top):
            if Array[index]>Array[index+1]:
                temp=Array[index]
                Array[index]=Array[index+1]
                Array[index+1]=temp
                Swap=True
        top=top-1
    Display(Array)

#linear search
def linearsearch():
    index=0
    found=False
    searchvalue=int(input("enter a number "))
    while found==False and index<len(Array):
        for index in range(len(Array)):
            if searchvalue==Array[index]:
                    found=True
          
       
                 
                    Display((index,Array[index]))
choice=int(input("enter your choice,1 for bubble sort,2 for linear search,3 for exit "))
if choice==1:
     bubblesort()
elif choice==2:
     linearsearch()
elif choice==3:
     print("------EXIT------")
#now using only functions
def Display(Output):
    print(Output)
#array
Array=[56,12,45,98,77,10]
#bubble sort
def bubblesort():
    top=len(Array)-1 #Numberofswaps
    Swap=True
    Display(Array)
    while Swap==True and top>0:
        Swap=False
        for index in range(top):
            if Array[index]>Array[index+1]:
                temp=Array[index]
                Array[index]=Array[index+1]
                Array[index+1]=temp
                Swap=True
        top=top-1
    return Array

#linear search
def linearsearch():
    index=0
    found=False
    searchvalue=int(input("enter a number "))
    while found==False and index<len(Array):
        for index in range(len(Array)):
            if searchvalue==Array[index]:
                    found=True
                    return((index,Array[index]))
        if found==False:
                            return("number not found")
    
          
                              
       
                 
                    
choice=int(input("enter your choice,1 for bubble sort,2 for linear search,3 for exit "))
if choice==1:
     Display(bubblesort())
elif choice==2:
     Display(linearsearch())
elif choice==3:
     print("------EXIT------")     
     


     



 
            


  
