# -*- coding: utf-8 -*-
"""
Cameron Reading
Data 119 Python
3/20/2019
In-Class Work/Practice
"""
import random
LOTTO_NUM_LENGTH = 7

def main():
    generate_lotto_numbers()
    
    

   
#Encases all other funcions pertaining to Lotto Generating 
def generate_lotto_numbers():
    lotto_list = gen_lotto_list()
    print_lotto_numbers(lotto_list)

#Making list of numbers of rando nums
def gen_lotto_list(): 
    lotto_list = []
    num = 1
    while num <= LOTTO_NUM_LENGTH:
        lotto_list.append(gen_lotto_num())
        num += 1
    return lotto_list
    
    
#Will return lotto number for each spot (0-9)    
def gen_lotto_num():
    ran_num = random.randint(0,9)
    return ran_num

#Prints out the newly made lotto nicely!
def print_lotto_numbers(lotto_list):  
    num = 0
    print("Today's winning numbers: ", end = '')
    while num < LOTTO_NUM_LENGTH:
        print(lotto_list[num], end = '')
        num += 1
    print('')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()
