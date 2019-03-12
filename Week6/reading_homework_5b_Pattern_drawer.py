# -*- coding: utf-8 -*-
"""
Cameron Reading
Data 119 Python 1
3/7/2019
Homework Week 5 B - Pattern Drawer! *******

"""

#Intializing Blank string for StarLine
star_string = ''

#First loop is for the number of lines of starts
for line_num in range(7, 0, -1):
    
    #Second loop is for the printing of stars for current line
    #Depending on the line_num that will determin how many times 
    #The loop will loop through and add a new "*" to the string 
    #that contains the strings 
    for star_num in range (line_num):
        star_string += "*"
    
    print(star_string)
    star_string = ''
