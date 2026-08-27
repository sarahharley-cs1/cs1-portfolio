#PlayPig

"""This program is the game of pig.  
A player rolls 2 die and adds their total.  You keep rolling unless you roll a sum of 2.
A player wins if they reach 100 or over.
A player loses if they roll a sum of 2."""



import random



def roll_dice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    print(f"You rolled a {die1} and a {die2}", end="")
    return die1 + die2


def display_dice(dice):
    print(f" for a sum of {dice}")
    
    
    
print("Let's play pig!")


total = 0




while total <= 100:
    player_die = roll_dice()
    
    if(player_die == 2):
        break
    
    total = player_die + total
    display_dice(player_die)
    print(f"Your total is {total}")

    
    
    
    
    
if total >= 100:
    print("You win!")
    
else:
    print("You lose.")