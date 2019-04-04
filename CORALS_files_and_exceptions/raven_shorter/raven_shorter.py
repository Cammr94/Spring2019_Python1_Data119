# -*- coding: utf-8 -*-
"""
Cameron Reading
Data 119 Python
3/20/2019
In-Class Work/Practice
"""

raven_txt_object = open('the_raven.txt', 'r')

raven_lines = raven_txt_object.readlines()

list_lines_raven = []

for line in raven_lines:
    print(line.rstrip('\n'))
    list_lines_raven.append(line.rstrip('\n'))
    
raven_txt_object.close()   


output_file_object = open("raven_abbriviated.txt", 'w')

for index in range(len(list_lines_raven)):
#    print(index % 3)
    if index % 3 == 0:
        output_file_object.write(list_lines_raven[index] + '\n')
        #print(list_lines_raven[index])

output_file_object.close()

'''
for index in range(len(raven_text)):
    if index % 3 == 0:
        output_file_object.write(raven_text)
        
    raven_text = raven_txt_object.readline()
'''        