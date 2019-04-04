# -*- coding: utf-8 -*-
"""
Cameron Reading
Data 119 Python
4/3/2019
In-Class Work/Practice Step-Month-AVG Calculator
"""

days_in_month_list = [31,28,31,30,31,30,31,31,30,31,30,31]


steps_object = open('steps.txt', 'r')

steps_num_line = steps_object.readline()

output_file_object = open('steps_per_month.txt', 'w')

month_num = 1
month = ''

for days in days_in_month_list:
    day_num = 1
    steps_total_month = 0
    average_steps_month = 0
    while day_num <= days:
        current_day_steps = int(steps_num_line.rstrip('\n'))
        steps_total_month += current_day_steps
        steps_num_line = steps_object.readline()
        day_num += 1
    if month_num == 1:
        month = "January"
    elif month_num == 2:
        month = "Febuary"
    elif month_num == 3:
        month = "March"
    elif month_num == 4:
        month =  "April"
    elif month_num == 5:
        month = "May"
    elif month_num == 6:
        month = "June"
    elif month_num == 7:
        month = "July"
    elif month_num == 8:
        month = "August"
    elif month_num == 9:
        month = "September"
    elif month_num == 10:
        month = "October"
    elif month_num == 11:
        month = "November"
    elif month_num == 12:
        month = "December"    
    
    
    average_steps_month = format(float(steps_total_month / days), '.1f')
    string_to_output = str(average_steps_month)
    output_file_object.write(string_to_output + '\n')
    
output_file_object.close()
