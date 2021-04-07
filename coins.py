


coins = 0
print('You have 0 coins.')

answer = input('Would you like a coin?    ')

while answer.lower() == "yes":
    coins += 1
    print(f'You have {coins} coin.')
    answer = input('Do you want another coin?   ')
    answer.lower ()

while answer.lower() == "no":
    print("Bye", coins)
    break


