alphabet = 'abcdefghijklmnopqrstuvwxyz'

text_input = input("Enter your message here: ")
my_key = int(input("Enter your key here: "))

n = len(text_input)

text_output = ""

for i in range(n):
    char = text_input[i]
    # print(char)
    location = alphabet.find(char)
    new_location = (location + my_key) % 26
    text_output += alphabet[new_location]

print(text_output)

#my_key = 13
#solution: you must learn what you have learned