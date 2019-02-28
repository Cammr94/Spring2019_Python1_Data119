# -*- coding: utf-8 -*-
"""
Cameron Reading
2/20/19
Python 1 DATA 119 - Spring 2019
Homework Week 3 

Gives out what the tip should be in 10, 15, 20% tip for an entered price!

"""
#Asking for Input of Bill Price
bill_price =float(input("Please enter total bill cost: "))

#Finding Tip for Bill price and adding it with bill for a Final Total
tip_10_total = (bill_price * .10) + bill_price
tip_15_total = (bill_price * .15) + bill_price
tip_20_total = (bill_price * .20) + bill_price

#Displaying Results, and formatting to display with $ and messege to display
print("$", format(tip_10_total, '.2f'), sep = '', end = ' ')
print("For a 10% Tip")

print("$", format(tip_15_total, '.2f'), sep = '', end = ' ')
print("For a 15% Tip")

print("$", format(tip_20_total, '.2f'), sep = '', end = ' ')
print("For a 20% Tip")