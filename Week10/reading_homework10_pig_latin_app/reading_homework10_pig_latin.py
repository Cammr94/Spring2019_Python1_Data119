# -*- coding: utf-8 -*-
"""
Cameron Reading
Data 119 Python 1
4/15/2019
Homework 10 Assignment - 
"""
import string
#List of Vowels to look for at the character level
VOWELS = ['a', 'e', 'i', 'o', 'u']


#A quick function that returns true or false that a character is a punctuations
def is_punctuation(character):
    # punctuation is a constant belonging to string
    if character in string.punctuation:
        return True
    else:
        return False
    #SOURCE Corals Jupyter Notebook Week 10 "Is Punction Function Excersise 





"""
Will open a file based on the name from the main function
it will open the file and load in the whole text file to an object
and will then return that object to the main function as one whole string
"""
def open_text_load_list(file_name):
    
    
    try:
        file_object = open(file_name ,'r')
    except OSError as f:
        print(f)
        print("File ", file_name, 'was not found!, please locate! ')

    else:
        file_text_string = file_object.read()
        file_object.close()
        return file_text_string
'''
function that will pipiglatin each in line of the text file
First it will 
'''
def pig_latin_list(text_line_list):
    #empty list that will contain each new line made
    pig_latin_result = []
    for line in text_line_list:
        line_list = []
        new_line = ''
        
        #this if statement will check to see for a empty space, and add it
        if line == '':
            pig_latin_result.append('')
        
        #will make a list out of the individual words from the incoming line
        else:
            word_list = line.split()
            
            
            for word in word_list:
                changed_word = pig_latin_word(word)
                line_list.append(changed_word)
            #Will make a new string out of the changed words! 
            new_line = ' '.join(line_list)
            
            #Will add new line to the result!
            pig_latin_result.append(new_line)   
    
    return pig_latin_result



'''
Big function of the whole program.  This will look at each word
from the above list and do a bunch of checks to see if it qualifies for 
certain conditions of the piglatin change!
'''
def pig_latin_word(word):
    #empty string for the whole new word
    pig_latin_word = ''
    
    #two variables that will capture any ending punctuations to be added later
    begining_punc = ''
    ending_punc = ''
    
    #flag for capitlization
    is_capital = False
    
    #Checks to see if the word is capitalized
    if word.istitle() == True:
        is_capital = True
    
    
    #Checking for punctuation and making strings for it
    if word[0] in string.punctuation or word[-1] in string.punctuation:

        #Checking the begining portion of the word for its puncutation
        if word[0] in string.punctuation:
            is_char_punc = True
            char_index = 0
            
            #will keep checking to it encounters no punctuation!
            while is_char_punc == True:
                if word[char_index] not in string.punctuation:
                    is_char_punc = False
                else:
                    begining_punc = begining_punc + word[char_index]
                    char_index += 1
                    
            #Once we know the punctuations, we chop it off the word for now!        
            word = word.replace(begining_punc, '')
            
            
        if word[-1] in string.punctuation:
            is_char_punc = True
            char_index = -1
            
            #Will keep checking to it encounters no punctuation!
            while is_char_punc == True:
                if word[char_index] not in string.punctuation:
                    is_char_punc = False
                else:
                    ending_punc = word[char_index] + ending_punc
                    char_index -= 1
                    
            #Once we know the punctuations, we chop it off the word for now!        
            word = word.replace(ending_punc, '')
                    
        
    #Forces all aplha chars to be lowered! This will help if a word is cap
    #so it will wont be placed at the end capitalized!                
    word = word.lower()    
        
    #Checks to the word is less than 2 chars length, cause all it needs is "ay"
    if len(word) <= 2:
        pig_latin_word = word + 'ay'
        
    #if the first char is a vowel, we just add "ay" at the end
    elif word[0] in VOWELS:
        pig_latin_word = word + 'ay'
        
    #We check to see if the next char is a consanant, if so, we move both
    #and then add an 'ay' at the end after move!    
    elif word[1] not in VOWELS:
        pig_latin_word = word[2:] + word[0:2] + 'ay'
        
    #Since we know that the first char is not a vowel, and the second char is, 
    #we just move the one character and add an 'ay' after the move    
    else:
        pig_latin_word = word[1:] + word[0] + 'ay'
    
   #Now we add in both the punctuations (If there are any!) to the new word
    pig_latin_word = begining_punc + pig_latin_word + ending_punc
    
    #and now we see if the word needs capitalized, and do so if true!
    if is_capital == True:
        pig_latin_word = pig_latin_word.title()
    
    return pig_latin_word


#Will output the newly made string to the output file!
def write_out_file(string_to_write):
    out_file_name = 'prejudice_latin.txt'
    
    try:
        out_file_object = open(out_file_name, 'w')
    except IOError:
        print('File is not avaible')
    else:
        out_file_object.write(string_to_write)
        
    return

    









def main():
    #Name of file that will be piglatin-ed!
    text_file_name = "prejudice.txt"
    prejudice_string = open_text_load_list(text_file_name)
    
    '''
    It will take the whole string and split the string into one
    giant list containing all the lines, since it will be split up
    by '\n' character!
    '''
    full_file_text_list = prejudice_string.split('\n')
    
    #Will transform list into piglatin words!
    transformed_list = pig_latin_list(full_file_text_list)
    
    '''
    will take transformed list and join the list into a string joined by
    the escape character "\n"
    '''
    new_string = '\n'.join(transformed_list)
    
    #Outputting the new string to the new output file!
    write_out_file(new_string)






if __name__ == "__main__":
	main()