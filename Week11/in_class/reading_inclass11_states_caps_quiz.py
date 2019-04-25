# -*- coding: utf-8 -*-
"""
Cameron Reading
Data 119 Python 1
4/24/19
In-Class Assignment
"""

import random

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
        
        
    quiz_dictionary = dict(set(zip(state_name_list, state_caps_list)))
    
    
    
    return quiz_dictionary

def state_list_create():
    state_name_list = []
    input_file_object = open("states_names.txt", 'r')
    state_string = input_file_object.readline()

    
    while state_string != '':
        state_name_list.append(state_string.rstrip('\n'))
        state_string = input_file_object.readline()
        
    input_file_object.close()
    
    return state_name_list


def quiz_game(quiz_dict, states_list):
    input("Welcome to the State Capital Quiz Game! Hit Enter to start!")

    question_num = 1
    correct_num = 0
    wrong_num = 0
    while question_num != 51:
        random_state_num = random.randint(1, 50) - 1
        state = states_list[random_state_num]
        question = "What is " + state + "'s capital?"
        guess = input(question)
        
        if guess.isaplha() != True:
            



def main():
    quiz_dict = states_and_capital_dictionary()
    state_list = state_list_create()
    quiz_game(quiz_dict, state_list)

        
main()