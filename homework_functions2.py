
myNumbers = [52, 50, 30, 27, 29, 29, 25, 24]

print("The list is ", myNumbers)

smallestNumber = myNumbers[0]

for i in range(len(myNumbers)):
    if myNumbers[i] < smallestNumber:
        smallestNumber = myNumbers[i] 


print("The smallest number is ", smallestNumber)

largestNumber = myNumbers[0]

for i in range(len(myNumbers)):
    if myNumbers[i] > largestNumber:
        largestNumber = myNumbers[i] 

print("The largest number is ", max(myNumbers))
# ******************************************************



myString = ["Michigan", "Mexico", "Ohio", "Indiana"]

print("Here's the places I've lived :" + str(myString))

smallestString = 9999999999
for ele in myString: 
    if len(ele) < smallestString: 
        smallestString = len(ele) 
        res = ele 

print("Minimum length string is : " + res) 

print("The smallest string in the places I've lived is: " + res)

largestString = 0
for ele in myString: 
    if len(ele) > largestString: 
        largestString = len(ele) 
        res = ele 

print("The Largest string in the places I've lived is: " + res)
# # ***************************************************************
