# -*- coding: utf-8 -*-
"""
Cameron Reading
Data 119 Python 1
2/28/2019
Homework 4 Assignment

A program which determines what resturant you can go to
based on preferenmces of friends!

"""

#Find out the what the party likes to eat/can't eat
#and assign a true or false value to it

vege_text = input("Is anyone in your party a vegetarian? ")
if "y" in vege_text or "Y" in vege_text:
    vege_text = True
else:
    vege_text = False

vegan_text = input("Is anyone in your party a vegan? ")
if "y" in vegan_text or "Y" in vegan_text:
    vegan_text = True
else:
    vegan_text = False

gf_text = input("Is anyone in your party gluten-free? ")
if "y" in gf_text or "Y" in gf_text:
    gf_text = True
else:
    gf_text = False
    
#determine what resturants you can go to!   
    
print('Here are your restaurant choices:')

#Joe's Burger has no option for vegan, gluten-free, etc. Test if all False
if vege_text != True and vegan_text != True and gf_text != True:
    print("Joe's Burger")
     
if vegan_text != True:
    print('Main Street Pizza')

if vegan_text != True and gf_text != True:
    print('Mama\'s Fine Italian')

#Corner Cafe and The  Chef's Kitchen is always choice since    
print("Corner Cafe")
print("The Chef's Kitchen")  
  