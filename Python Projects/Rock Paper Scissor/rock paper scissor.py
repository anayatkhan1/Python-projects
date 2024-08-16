#define the function to make a game:
import random

def play():

    user = input("What's Your Choice from r for rocks, s for scissor, p for paper: \n")
    computer = random.choice(['r', 's', 'p'])

    if user == computer:
        return "It\'s a Tie"
    if is_win(user, computer):
        return "You win"
    
    return "You Lost"

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r')\
          or (player == 's' and opponent == 'p'):
          return True

print(play())