# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:00:51 2019

@author: cread09
"""
import string
def is_punctuation (character):
    if character in string.punctuation:
        return True
    else:
        return False

users_string = input("Enter a sentence/word to see if it's a Palindrome: ")
no_space_string = users_string.replace(' ', '')
no_punctuations_string = ""
for char in no_space_string:

    is_punc = is_punctuation(char)

    if is_punc != True:
       no_punctuations_string = no_punctuations_string + char 
            
all_chars_lower = no_punctuations_string.lower()
reverse_string = all_chars_lower[::-1]
if reverse_string == all_chars_lower:
    print("It's a palindrom!")
else:
    print("This is not a palindrome!")
