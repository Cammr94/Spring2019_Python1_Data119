# -*- coding: utf-8 -*-
"""
Cameron Reading
Data 119 Python 1
4/10/2019
In-Class Assignment

"""

def load_string(file_name):
    file_object = open(file_name, 'r')
    full_text= file_object.read()
    no_endlines_text = full_text.replace('\n', '')
    no_spaces_text = no_endlines_text.replace(' ', '')
    return no_spaces_text
def count_char(text_being_looked_through, char_to_count):
    char_counter = 0
    for char in text_being_looked_through:
        char = char.lower()
        if char == char_to_count:
            char_counter += 1
            
    return char_counter
    
    
    



def main():
    
    file_name = "prejudice.txt"
    full_text_string = load_string(file_name)
    print('The vowel "A" shows up: ', count_char(full_text_string, "a"))
    print('The vowel "E" shows up: ', count_char(full_text_string, "e"))
    print('The vowel "I" shows up: ', count_char(full_text_string, "i"))
    print('The vowel "O" shows up: ', count_char(full_text_string, "o"))
    print('The vowel "U" shows up: ', count_char(full_text_string, "u"))

main()