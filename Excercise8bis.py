##Dice simulator: Write a program that simulates the roll of two dice and calculates the sum of
##the values obtained.

import random

def roll_two_dice():
    
    die1=random.randint(1,6)
    die2=random.randint(1,6)
   
    return die1, die2


def main():
 
    die1, die2 = roll_two_dice()
    print(f"Sum total: ",die1+die2)
   




if __name__ == "__main__":
    main()