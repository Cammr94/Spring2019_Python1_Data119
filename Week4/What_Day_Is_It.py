# -*- coding: utf-8 -*-
"""
Cameron Reading
2/27/2019
In-Class Practice
A simple program that tells you what day it is

"""

user_num = int(input("Please enter a number from 1 to 7, and I will tell you what day it is! "))

if user_num == 1:
    print("It's Monday!")
elif user_num == 2:
    print("It's Tuesday!")
elif user_num == 3:
    print("It's Wednesday!")
elif user_num == 4:
    print("It's Thursday!")
elif user_num == 5:
    print("It's Friday!")
elif user_num == 6:
    print("It's Saturday!")
elif user_num == 7:
    print("It's Sunday!")
else:
    print("Invalid Number!!")