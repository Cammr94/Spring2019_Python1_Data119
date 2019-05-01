# -*- coding: utf-8 -*-
"""
Cameron Reading
Data 119 Python 1
4/24/19
In-Class Assignment
"""

import random

'''
Function that will open files that contain a list of states
and states capoitals, and return a completed dictionary
that will be used for the quiz!
'''
def states_and_capital_dictionary():
    state_name_list = []
    input_file_object = open("states_names.txt", 'r')
    state_string = input_file_object.readline()

    
    while state_string != '':
        state_name_list.append(state_string.rstrip('\n'))
        state_string = input_file_object.readline()
        
    input_file_object.close()
    
    state_caps_list = []
    input_file_object = open('state_caps.txt', 'r')
    caps_string = input_file_object.readline()
    
    while caps_string != '':
        state_caps_list.append(caps_string.rstrip('\n'))
        caps_string = input_file_object.readline()
        
    #Special line of code, that combines two lists into a dictionary    
    quiz_dictionary = dict(set(zip(state_name_list, state_caps_list)))
    
    
    
    return quiz_dictionary

'''
A sub version of the above function that makes a list
of state naems to be used to randomly pick a state
and use it in the quiz game!
'''

def state_list_create():
    state_name_list = []
    input_file_object = open("states_names.txt", 'r')
    state_string = input_file_object.readline()

    
    while state_string != '':
        state_name_list.append(state_string.rstrip('\n'))
        state_string = input_file_object.readline()
        
    input_file_object.close()
    
    return state_name_list

'''
Main function of the qwiz game, will randomly pick a state from the list of 
states and use that as key to get the value (Capital of the state) to be 
compared with the players guess.  It will keep track of right and wrong
guesses, and will keep the player up to date with the score!
'''

def quiz_game(quiz_dict, states_list):
    input("Welcome to the State Capital Quiz Game! (Hit Enter to start!)")

    question_num = 1
    correct_num = 0
    wrong_num = 0
    quit_quiz = False
    
    #Will exit loop, if player quits, or if the num of loops passes 50!
    while question_num != 51 and quit_quiz != True:
        random_state_num = random.randint(1, 50) - 1
        state = states_list[random_state_num]
        question = "What is " + state + "'s capital?  "
        
        #makes players guess a string, lower it, and then title it
        #This makes it so the answer will match the case of the capital
        guess = str(input(question))                
        guess = guess.lower()
        guess = guess.title()
        
        #Allows the player to leave the quiz in the middle of it
        if guess == 'X':
            quit_quiz = True
        
       #If answer is correct 
        elif guess == quiz_dict[state]:
            correct_num += 1
            print("Correct!")
            current_score = "Curent Score: " + str(correct_num) + " Correct " +  str(wrong_num) + " Incorrect"
            print(current_score)
       
        #If answer is wrong
        else:
            wrong_num += 1
            print("Sorry, that is incorrect...")
            current_score = "Curent Score: " + str(correct_num) + " Correct " +  str(wrong_num) + " Incorrect"
            print(current_score)
            
        question_num += 1
        
    print("Final Score: Correct Guesses ", str(correct_num), " Incorrect ", str(wrong_num))
            
            
            



def main():
    quiz_dict = states_and_capital_dictionary()
    state_list = state_list_create()
    quiz_game(quiz_dict, state_list)

        
main()