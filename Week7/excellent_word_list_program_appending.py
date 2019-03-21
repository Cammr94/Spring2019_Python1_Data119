# -*- coding: utf-8 -*-
"""
Cameron Reading
Data 119 Python
3/20/2019
In-Class Work/Practice
"""

excellent_words = ["Dogs", 'Cats', 'Hamsters', 'Seals', 'Birbs']

for word in excellent_words:
    print(word, '',  end = '')

print('')
    
user_num_choice = int(input("Pick a number from 1 through 5: "))
print("The animal you chose was: ", excellent_words[user_num_choice - 1])
print('')

print("The first three items on this list are ", excellent_words[:3])
print("The last three items on this list are ", excellent_words[-3:])

'''
Could also print nicely these "first 3 and last 3 if we wanted to
by assigning the section we need ([:3]) and assign that to anotherlist
and use a for loop to print that new list out!
'''


excellent_words.append(input("Please enter new animal to be added to list: "))
print("~~NEW WORD ADDED~~")
for word in excellent_words:
    print(word, '', end = '')

print('')
print('')
print("!!!Sorting words!!!")
print('')

excellent_words.sort()
for word in excellent_words:
    print(word, '', end = '')

print('')

remove_word = input("Please enter word to get rid of: ")
if remove_word in excellent_words:
    excellent_words.remove(remove_word)
    
print('')

for word in excellent_words:
    print(word, '', end = '')
    
    
