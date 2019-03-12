# -*- coding: utf-8 -*-
"""
Cameron Reading
Data 119 Python 1
3/7/2019
Homework 5 A Outputing String and Reverse from user

"""
#Getting String from User, and store it and find its length
user_string = input("Please type a sentence out and I'll reverse it!: ")
string_length = len(user_string)

#Setting word "Accumaltor" to a blank string
reversed_string = ''

#Repeats till it gets to the begining of the string, using determined length
for letter_num in range(string_length, 0, -1):
    
    #Adds character to empty string useing letter_num from for loop
    #as the position to what letter to take from the user, and assign it
    #onto the end of the empty reverse string.
    #And repeats, until all of the string's character are added tp new string
    reversed_string = reversed_string + user_string[letter_num - 1]
    
#Prints out the new reversed string and outputs the character length of string
print(reversed_string)
print("Character Length of String:", string_length)   

    