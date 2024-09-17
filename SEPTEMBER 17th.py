#Today we will be creating a for loop to count How many times did the loop run

numberOfTime=0

data=[10,20,30,49,67,87,89]

for index in data:
    numberOfTime+=1
    print(numberOfTime,index)
    
print("Total Number of times the loop Executed",numberOfTime)


#Now we will be learning about calculating the total of all the data in the array and also calculating the average

studentMarks=[99,22,34,87,89,94,90,10]

total=0
length=0
average=0
for marks in studentMarks:
    length+=1
    total+=marks
    average=total/length
    
print("The Average of all the grades is ",average)




#Now we will be learning about the finding the smallest number in the array without knowing all the elements in the array

studentRollNumber=[10,20,3,2,4,10,56,78]

smallestNumber=None

for index in studentRollNumber:
    if smallestNumber is None:
        smallestNumber=index
    elif index<smallestNumber:
        smallestNumber=index
                
print("The smallest Number in the array is ",smallestNumber)



    