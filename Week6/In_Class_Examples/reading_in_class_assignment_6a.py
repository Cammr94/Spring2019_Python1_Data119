# -*- coding: utf-8 -*-
"""
Cameron Reading
Data 119 Python 1 
3/13/2019
In-Class Assignment Week 6 - Rock Paper Scissors Battle Royale!

"""
import random

def play_rock_paper_scissors ():
    
    result =''
    
    comps_choice = determine_computers_choice()
    players_weapon = get_players_choice()
    
    printing_comps_choice(comps_choice)
    
    result = compare_choices(comps_choice, players_weapon)
    
    no_winner = duel_results(result)
    
    return no_winner
    

def determine_computers_choice ():
    computers_choice = random.randrange(0,3)
    return computers_choice

def printing_comps_choice (comps_choice):
    if comps_choice == 0:
        print("Computer Chose Rock")
    elif comps_choice == 1:
        print("Computer Chose Paper")
    else:
        print("Computer Chose Scissors")
        


def get_players_choice ():
    players_choice = 2
    players_input = input("Choose your weapon! (Rock, Paper, or Scissors): ")
   
    if players_input == "Rock" or players_input == "rock":
        players_choice = 0
    elif players_input == "Paper" or players_input == "paper":
        players_choice = 1
        
    return players_choice

def compare_choices (comps_weapon, players_weapon):
    
    if comps_weapon == players_weapon:
        result = "Draw"
        return result
    elif comps_weapon == 0 and players_weapon == 2:
        result = "Computer Wins"
    elif comps_weapon == 1 and players_weapon == 0:
        result = "Computer Wins"
    elif comps_weapon == 2 and players_weapon == 1:
        result = "Computer Wins"
        
    else:
        result = "Player Wins"
        
    return result
        
def duel_results (results):
    if results == "Computer Wins":
        no_winner = False    
        print(results)
    elif results == "Player Wins":
        no_winner = False
        print(results)
    else:
        no_winner = True
        print(results)
    return no_winner
        

def main():
    no_winner = True
    while no_winner == True:
        no_winner = play_rock_paper_scissors()
        no_winner == False



if __name__ == "__main__":
    main()
