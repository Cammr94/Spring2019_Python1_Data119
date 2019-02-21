# -*- coding: utf-8 -*-
"""
Cameron Reading 
2/20/19
Python 1 DATA 119 - Spring 2019
Homework Week 3 

Asks user for 3 grades and then averages them!

@author: cread09
"""
#Asking for the 3 Grades to be Submitted
grade1 = int(input("Please enter 1st Grades: "))
grade2 = int(input("Please enter 2nd Grades: "))
grade3 = int(input("Please enter 3rd Grades: "))

averaged_grade = (grade1 + grade2 + grade3) / 3

print("The averaged grade is ", format(averaged_grade, '.2f'), '%', sep='')