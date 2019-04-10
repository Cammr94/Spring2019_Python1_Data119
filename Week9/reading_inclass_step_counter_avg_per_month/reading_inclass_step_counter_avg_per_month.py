# -*- coding: utf-8 -*-
"""
Cameron Reading
Data 119 Python
4/3/2019
In-Class Work/Practice Step-Month-AVG Calculator
"""
#Number of days for each month and in order from Jan to Dec
days_in_month_list = [31,28,31,30,31,30,31,31,30,31,30,31]

#Open Steps.txt and output file txt and reads first line
steps_object = open('steps.txt', 'r')

steps_num_line = steps_object.readline()

output_file_object = open('steps_averages.txt', 'w')

#Some month counter and empty month string
month_num = 1
month = ''


#Begining messege for output file
output_file_object.write("Month               Average Steps Per Month\n")
output_file_object.write("---------------------------------------------\n")


#major loop of program, it will travel thoough the days_month_list till end
for days in days_in_month_list:
    #Counter for day number set, and accumulator set
    day_num = 1
    steps_total_month = 0
    average_steps_month = 0
    
    #This loop will cycle through depending on how many days are in the current month
    #And will use the number from the list to work and grab number from
    #Steps.txt each time it runs throgh, adding to sum and then eventully
    #dividing by the month's days and getting an average.
    
    while day_num <= days:
        current_day_steps = int(steps_num_line.rstrip('\n'))
        steps_total_month += current_day_steps
        steps_num_line = steps_object.readline()
        day_num += 1
    
    #Section where it determines what month it is within the loop that just ended
    #And assign the month variable the correct string
    
    
    if month_num == 1:
        month = "January  "
    elif month_num == 2:
        month = "Febuary  "
    elif month_num == 3:
        month = "March    "
    elif month_num == 4:
        month =  "April   "
    elif month_num == 5:
        month = "May      "
    elif month_num == 6:
        month = "June     "
    elif month_num == 7:
        month = "July     "
    elif month_num == 8:
        month = "August   "
    elif month_num == 9:
        month = "September"
    elif month_num == 10:
        month = "October  "
    elif month_num == 11:
        month = "November "
    elif month_num == 12:
        month = "December "  
    month_num += 1
    
    #Averaging of the total steps for the month are done here after loop
    #Also making the float casted to string and catenating the 
    #month, tabs, and average into one string to be written out to file
    
    average_steps_month = format(float(steps_total_month / days), '.1f')
    avg_to_string= str(average_steps_month)
    string_to_output = month + "\t\t\t" + avg_to_string
    output_file_object.write(string_to_output + "\n")
    
output_file_object.close()
steps_object.close()
