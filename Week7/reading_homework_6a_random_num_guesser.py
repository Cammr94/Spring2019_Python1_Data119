# -*- coding: utf-8 -*-
"""
Cameron Reading 
Data 119 Python 1
3/13/2019
Homework Week 6 Assignment - Random Number Generator

"""
import random

'''
Main Chunk of the Program, it contains most of the other functions
Its loop will go through until a correct answer is guessed!
Also contains a counter that counts up every time it loops through
with each guess!
'''

def play_guess_game():
    
    #Guess Counter
    total_guesses = 0 
    
    target = get_guess_target()
    
    #Sentential for loop
    right_guess = False
    
    print("I'm thinking of a number from 1 to 100...")
    print("Try and guess it!")
    
    #Loop where we check to see if that answer is correct and progesses
    while right_guess == False:
        players_guess = get_players_guess()
        right_guess = check_answer(players_guess, target)
        total_guesses += 1
    print("Congratulations! It took you", total_guesses, "tries to guess correctly!")


#Getting the target to be guessed! 
def get_guess_target():
    target = random.randint(1, 100)
    return target


'''
Where the player will input a guess and also check to see if it is valid
i.e. making sure that its between 1-100 and that its an integer!
'''

def get_players_guess():
    valid_answer = False
    while valid_answer == False:
        player_guess = int(input("Enter your guess please: "))
 
        if player_guess >= 0 and player_guess <= 100:
            valid_answer == True
            return player_guess
        else:
            valid_answer == False
            print("INVALID ANSWER! Needs to be a number 1 to 100") 
        
#Checking to see if it is the correct, and respond with proper "hints"    
def check_answer(guess, target):
    if guess == target :
        return True
    
    elif guess < target:
        print("Too low...try again!")
        return False
        
    elif guess > target:
        print("Too high! Try again!")
        return False
        
#Main Function, that holds/starts it all
def main():
    #Empty String Var for Loop check, and boolean var to keep it going
    again =''
    play_again = True
    while play_again == True:
        
        play_guess_game()
        again = input("Want to play again? ")
        if 'y' in again or 'Y' in again:
            play_again = True
            
        else:
            play_again = False



if __name__ == "__main__":
    main()