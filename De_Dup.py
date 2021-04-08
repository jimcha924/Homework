myList = [2, 4, 9, 1, 4, 16, 9, 2, 10, 24, 9, 1, 3, 5, 9, 7]
print ("My original list of my kiddos birthday numbers is : " +  str(myList))

result = []
for i in myList:
    if i not in result:
        result.append(i)

print ("The list after removing duplicates : " + str(result))