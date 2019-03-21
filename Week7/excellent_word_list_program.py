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
    
user_num_choice = int(input("Pick a number from 1 through 5: "))
print(excellent_words[user_num_choice - 1])

print("The first three items on this list are ", excellent_words[:3])
print("The last three items on this list are ", excellent_words[-3:])