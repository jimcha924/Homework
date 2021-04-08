

myword = ['beefy', 'pools', 'breaks']

longVowelsounds = ['ee', 'oo', 'ea']

result = ''
for i in range(len(myword)):
    twoletters = myword[i:i+2]
    if twoletters in longVowelsounds:
        result += myword[i] * 4
    else:
        result += myword[i]

print(result)