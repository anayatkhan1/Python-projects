import random
#import the all the data from words file
from words import words
import string
def get_valid_words(words):
    word = random.choice(words) #randomly generate the words from the data
    while "-" in word or " " in word:
        word = random.choice(words)

    return word

#now we create hangman algorithm so let's get started:

def hangman():
    
    word = get_valid_words(words)
    word_letters = set(word) # letter in words
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what user guessed
    
    #getting user input
    user_letter = input("Guess a letter: ").upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letter:
            word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print("You have already use that character. Please try again")
    else:
        print("Invalid character. Please try again")


user_input = input("Type something: ")
print(user_input)

#Hangman game is stop 
