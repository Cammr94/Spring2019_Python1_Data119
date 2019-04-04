# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:09:42 2019

@author: cread09
"""

raven_text_object = open("the_raven.txt", "r")

for line in raven_text_object:
    print(line.rstrip('\n'))