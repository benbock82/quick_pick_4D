"""
This script is to generate a list of unique and random 4D numbers and accordingly to the numbers of bets you want.
"""

#Import random to generate random numbers
import random

# Define the quick_pick_4D function
def quick_pick_4D(bets):
    # create an empty all_4D to store all the numbers generated
    all_4D = []
    while len(all_4D) < bets :
        # create an empty one_4D to store the number generated
        one_4D = []
        for num in range(4):
            rand_4D = random.randint(1, 9)
            one_4D.append(rand_4D)
            # convert the list of 4 integers into a string of 4 numbers (i.e 8877)
            string_4D = [str(D) for D in one_4D]
            string_4D = "".join(string_4D)
        # Append one 4D number into all_4D
        all_4D.append(string_4D)
        
        # If there is duplicate, reset and regenerate all the numbers
        if len(all_4D) != len(set(all_4D)):
            all_4D =[]
    
    # print the 4D numbers on each line for easy reference
    for num_4D in all_4D:
        print(num_4D)

if __name__ == '__main__':
    bets = int(input('Please enter the number of bets (1 and above): '))
    while True:
        if bets <= 0:
            bets = int(input('Please only enter number above 1: '))
        else:
            break

    quick_pick_4D(bets)