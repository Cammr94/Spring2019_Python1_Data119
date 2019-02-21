# -*- coding: utf-8 -*-
"""
Cameron Reading 
2/20/19
Python 1 DATA 119 - Spring 2019
In-class Activity 
Take input of Seconds and Convert it into hours, minutes
Output Hours, Minutes, Seconds

@author: cread09
"""
#Asking For Seconds to be Converted
input_second = int(input("Please input seconds to be converted: "))

#Converting Inputed Seconds and assigned minute and hour variable 

secs_to_mins = input_second / 60

sec_to_hours = (secs_to_mins / 60)

#Printing Out Results of Conversion and Formating accurately!

print(format(input_second, ',d'), "seconds Equals...")
print(format(sec_to_hours, '.2f'), "hours")
print(format(secs_to_mins, '.2f'), "mins")
print(format(input_second, ',d'), "seconds")

#Yay Converted Seconds!