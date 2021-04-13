# 1. Letter Summary
# Write a letter_histogram program that asks the user for input, and prints a dictionary containing the tally of how many times each letter in the alphabet was used in the word. For example:

# def letter_histogram(word):
#     my_letters = {}
#     for letter in word:
#         if letter in my_letters:
#             my_letters[letter] += 1
#         else:
#             my_letters[letter] = 1

#     return my_letters

# print(letter_histogram("Wolverine"))



# 2. Word Summary
# Write a word_histogram program that asks the user for a sentence as its input, 
# and prints a dictionary containing the tally of how many times each word in the alphabet was used in the text. 

def word_histogram(paragraph):    
    dict_of_letters = {}
    paragraph = input("What is your sentence? :  ")
    paragraph = paragraph.lower().split()
    for word in paragraph:
        if word in dict_of_letters:
            dict_of_letters[word] += 1
        else:
            dict_of_letters[word] = 1
    return dict_of_letters

print(word_histogram("To be or not to be."))



def most_common(word_histogram):
    c = []
    for key, value in word_histogram.items():
        c.append((value, key))

    c.sort(reverse=True)
    return c

c = most_common(word_histogram)
print('The most common words are:')
for freq, word in c[:3]:
    print(word, freq, sep='\t')

    # This kind of works, but I keep getting errors so...