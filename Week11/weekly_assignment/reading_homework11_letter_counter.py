# -*- coding: utf-8 -*-
"""
Cameron Reading
Data 119 Python 1
4/24/19
Weekly Assignment Week 11 - Alphabet Counter!
"""

#Funtion thats the main core of the program, it will create a dictionary
#of all the letters of the alphabet and then will then will check each char
#and if it is a alphabetic letter then it will find that letter in the
#Dictionary and add 1 to the current value associated to that Key/Pair
def counting_letters ():
    alphabet_dictionary = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0,
                           'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0,
                           'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 
                           'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
    
    user_string = input("Give me a sentence, and I'll count the letters: ")
    
    for char in user_string:
        char = char.upper()
        
        if char.isalpha() == True:
            count = alphabet_dictionary.get(char, False)
            count += 1
            alphabet_dictionary[char] = count
    print_results(alphabet_dictionary)
    
    


#Will pretty print out the entire dictionary and its  
def print_results(dictionary_to_print):

#Hindsight being I could have kept it as a tuple, I think     
     list_of_keys = dictionary_to_print.keys()
     list_of_keys = list(list_of_keys)
     
#Sorts the key in alphabetical order to be printed correctly.
     list_of_keys.sort()
          
     for key in list_of_keys:
         

#This allows the two columns to exist, I check the index of the current letter
#And see if its odd or even and depending on the answer determines
#the side that the letter ill appear on including its value!         
         if (list_of_keys.index(key) + 1) % 2 != 0: 
             print(key, ': ', dictionary_to_print[key], "\t\t", end  = '')
         
         else:
             print(key, ': ', dictionary_to_print[key])
             
     return
 
    
    
def main():
    
    counting_letters()
    
    
    
main()