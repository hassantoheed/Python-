
#binary search(works on sorted arrays)
#works faster than linear search=>BIG O Notation
#in binary search in any list you will compare centre index(found by adding upper and lower bound divided by 2)
#formula center index=INT(UB+LB/2)
# with upper and lower bounds so that
# index is found searchvalue is used too
#in it three comparisons are made first search value with center index if it matches then its output if it doesnt then it is search value is compared in it so is center index>seachvalue or center index<searchvalue.if search value is lesser than center index it becomes lower bound if search value becomes greater than center index it becomes upper bound
#upperbound=len(Array)-1 to find out upper bound, lowerbound=0
#binary search algorithmn
Array=[11,12,13,14,17,91,99,101,107]
found=False
searchvalue=int(input("btayn? "))
lowerbound=0
upperbound=len(Array)-1
while found==False and lowerbound<=upperbound:
    index = int(upperbound + lowerbound / 2)
    if Array[index]==searchvalue:
            found=True
    if Array[index]>searchvalue:
            upperbound=index-1
    if Array[index]<searchvalue:
            lowerbound=index+1
if found:
    print("yes found")
else:
        print("not found")


#Insertion Sort(works backwards/sorts backwards)
#pick second index compare it backwards till it reaches lowerbound
#ub=upperbound
#lb=lowerbound
#index of present element (place=index-1)
Array=[2,3,4,3,2,4,3]
found=False
lb=0
ub=len(Array)-1
searchvalue=int(input("btayn? "))
for index in range(lb+1,ub):
    key=Array[index]
    place=index-1#index of present element
    if Array[place]>key:#for efficiency not necessary to add
        while place>=lb and Array[place]>key:
            temp=Array[place+1]
            Array[place+1]=Array[place]
            Array[place]=temp
            place = place - 1

