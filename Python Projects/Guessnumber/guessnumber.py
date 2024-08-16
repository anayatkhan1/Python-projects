#guessing game project 
#first the import the function 
import random

#define function
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess!= random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print(f"Sorry! The {random_number} is too low")
        elif guess> random_number:
            print(f"Sorry! your {random_number} is too high")
    print(f"Wow, Congratulation you guess the right number is {random_number}")

    
#define function where computer guess the number

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    while feedback!='c':
        if high != low:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"the guessing {guess} too low[l], too high[h] or Correct [c]: ").lower()
        if feedback == 'h':
         high = guess-1
        elif feedback == 'l':
            low = guess+1  
    print(f"Yoah! the computer guessed the Correct number is {guess}..!!!")        
computer_guess(10)
