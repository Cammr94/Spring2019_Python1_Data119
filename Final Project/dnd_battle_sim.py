# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 14:08:14 2019

@author: cammr
"""

import dice_rolls
import string
import pickle

#All Levels of players and Enemies scaled to Lvl 10

def character_selection():
    input("(Hit enter to progress through un-prompted texts!)")
    input("Welcome fellow adventureer!")
    input("I hope you are ready for glory and honor on the battlefield!")
    print("\nPlease do tell me friend, have you been here before?\nOr are you new around these parts?")
    
    print("(A) New Character")
    print("(B) Load Previous Character", end = '')
    char_choice = input("Choose: ")
    
    valid_answer = False
    
    while valid_answer != True:
        if char_choice.isalpha() == False:
            input("Uhh, pardon me? Could you repeat that? ~Invalid Choice~")
            print("(A) New Character")
            print("(B) Load Previous Character", end = '')
            char_choice = input("Choose: ")
        
        elif char_choice.upper() == 'A' or char_choice.upper() == 'B':
            valid_answer = True
        else:
            input("Uhh, pardon me? Could you repeat that? ~Invalid Choice~")
            print("(A) New Character")
            print("(B) Load Previous Character", end = '')
            char_choice = input("Choose: ")
            
    if char_choice.upper() == 'A':
        player_dic = create_chaaracter()
        
    elif char_choice.upper() == 'B':
        player_dic = load_character()
    
    return
    
def create_chaaracter():
    player_dic = {}
    input("Ahhh a newcomer!\nWelcome welcome!")
    input("Now...Tell me about your self")
    
    #Concatenate the name with a string to allow input conversations!
    
    player_name = input("Your Name: ")
    player_dic["name"] = player_name
    
    print("Choose a class!")
    print("(A) Barbarian")
    print("(B) Ranger")
    print("(C) Paladin")
    print("(D) Rogue")
    
    class_choice = input("Choice: ")
    
    valid_answer = False
    
    while valid_answer != True:
        if class_choice.isalpha() == False:
            print("~Not a valid choice!~\n")
            print("Choose a class!")
            print("(A) Barbarian")
            print("(B) Ranger")
            print("(C) Paladin")
            print("(D) Rogue")
            
            class_choice = input("Choice: ")
            
        elif class_choice.upper() < 'A' or class_choice.upper() > 'D':
            print("~Not a valid choice!~\n")
            print("Choose a class!")
            print("(A) Barbarian")
            print("(B) Ranger")
            print("(C) Paladin")
            print("(D) Rogue")
            
            class_choice = input("Choice: ")
            
        else:
            valid_answer = True
            
    if class_choice == 'A':
        print("Barbarian Choosen")
        player_dic['class'] = 'Barbarian'
        player_dic = barbarian_create(player_dic)
        
    elif class_choice == 'B':
        print("Ranger Choosen")
        player_dic['class'] = 'Ranger'
    elif class_choice == 'C':
        print("Paladin Choosen")
        player_dic['class'] = 'Paladin'
    else:
        print("Rogue Choosen")
        player_dic['class'] = 'Rogue'
        
    return player_dic
            
def barbarian_create (player_dic):    
    print("Barbarian Choosen")


def load_character():
    input("Oh its you! Welcome back...")
    input("...uh, remind me...")
    
    char_found = False
    while char_found != True:
        char_name = input("...who are you?\nYour Name: ")
        char_name_file = char_name.replace(' ', '_')
        try:
            char_file_object = open(char_name_file, 'rb')
        except IOError:
            input("Uhh, I've never heard of you stranger? ~Character Not Found~")
        else:
            char_found = True
            
    player_dic = pickle.load(char_file_object)
    return player_dic

def main():
    character_selection()
    
    
main()