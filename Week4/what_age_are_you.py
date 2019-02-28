# -*- coding: utf-8 -*-
"""
Cameron Reading
2/27/2019
In-Class Practice 2

Tell what stage in life someone is with input of age from User
"""
#Asking for Age to be examined. and implementing a variable
user_age = float(input("Please enter age: "))

#check/comparing entered Age to find out what age group it is in
#and outputing corresponding group tag!

if user_age >= 20:
    print("You are an adult!")
    
elif user_age >= 13 and user_age < 20: #Could potentially Rule out the <20 check 
                                        #beacuse we already know it has to be under 20
    print("You are a teenager!")
    
elif user_age > 1 and  user_age < 13:
    print("You are a child!")
    
elif user_age <= 1 and user_age > 0:
    print ("You are an infant! HOW CAN YOU TYPE??")
    
else:
    print("!!ERROR --INVALID AGE!!")