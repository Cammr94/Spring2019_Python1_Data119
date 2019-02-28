# -*- coding: utf-8 -*-
"""
Cameron Reading
Data 119
2/27/2019
In-Class Assignment

We are figuring out if a year is a leap year or not
and output how many days are in February
"""
#Asking User for a year, and assigning it to a variable
entered_year = int(input("Please enter a year to find out how many days February has: "))

#Running modular division (specifically to see if it is a 0) and assigning the result to a variable
divide_by_4 = entered_year % 4
divide_by_100 = entered_year % 100
divide_by_400 = entered_year % 400

#Checking the results of the modular division, and determining output phrase
if divide_by_4 == 0 and divide_by_100 == 0 and divide_by_400 ==0:
    print("February has 29 Days in", entered_year)
    
else:
    print("February has 28 Days in", entered_year)
