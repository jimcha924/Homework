




import pickle
phonebook_dict = {}

with open('phonebook.pickle', 'rb') as fh:
    phonebook_dict = pickle.load(fh)

def look_up_entry():
    newName = input("Enter name: ")
    print(phonebook_dict[newName])

def add_entry():
    newName = input("Enter name: ")
    new_phone = input("Enter phone number: ")
    phonebook_dict[newName] = new_phone

    with open('phonebook.pickle', 'wb') as fh:
        pickle.dump(phonebook_dict, fh)
    print(phonebook_dict)

def delete_entry():
    query = str(input("Which of these entries would you like to delete?   "))
    temp = 0
    for i in range(len(phonebook_dict)):
        if query == phonebook_dict[i][0]:
            temp += 1
            print(phonebook_dict.pop(i))
            print("This entry has been deleted.")

    with open('phonebook.pickle', 'wb') as fh:
        pickle.dump(phonebook_dict.pickle, fh)


def display_all():
    print("You can find all the entries currently in the phone book below")
    print(phonebook_dict)
    with open('phonebook.pickle', 'rb') as fh:
        pickle.dump(phonebook_dict.pickle, fh)

def menu():
    print("****************************")
    print("\t\t\tYour E-Phonebook")
    print("****************************")
    print("1. Look up an entry")
    print("2. Set an entry")
    print("3. Delete an entry")
    print("4. List all entries")
    print("5. Quit")
    print("What do you want to do (1-5)?")
    choice = int(input("Please enter your choice: "))
    return choice
