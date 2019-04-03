# -*- coding: utf-8 -*-
"""
Cameron Reading
Data 119 Python
3/27/2019
In-Class Work/Practice To Do List
"""


#Function that will spit the options for the user to explore
def print_menu():
    print("\n1) View the items on your todo list")
    print("2) View the items you have finished")
    print("3) Add an item to the todo list")
    print("4) Mark a todo list item as completed")
    print("5) Exit the Todo List Application (your list will not be saved)")
    
    return

'''Prints out the current items in the list and prints them
out nice and neatly! It also will catch and tell the user 
if the list itself is empty too!
'''

def print_todo_list(todo_list):
    print("\nThis is your todo list:")
#Incase the list is empty. this will catch it
    if todo_list == []:
        print("\nThere is nothing to display.")
        
    else:
        for element in todo_list:
            print(todo_list.index(element) + 1, ") ", element, sep = '')
    return
    


#Same as above, but will print out the tasks the user has done!
def print_completed_tasks(completed_list):
    print("\nThis is your list of completed tasks:")
#incase the list is empty this will catch it    
    if completed_list == []:
        print("\nThere is nothing to display.")

    else:
        for element in completed_list:
            print(completed_list.index(element) + 1, ") ", element, sep = '')
    return



''' One of the bigger functins of the program, it will ask input of the user
to be added as a task to the todo list and then spit the user back to the menu

This will also check to make sure something is actually typed in and not just a blank space!
'''
def add_to_todo_list(todo_list):
    element_to_add = input("What would you like to add? ")
    good_input = False
    while good_input != True: 
        if element_to_add == '':
            good_input = False
            print("\n!! Please enter something to add !! ")
            element_to_add = input("What would you like to add? ")
        else:
            good_input = True
            todo_list.append(element_to_add)
            
    return todo_list

''' The other big function of this program which will allow the user to 
mark tasks as "complete" and do two things.
1) It will remove them from the todo list
2) It will add the removed task to the completed tasks list!

This function also checks for input errors making sure the choice is within the
range of the todo list (ie a list of two items can only have a choice between 1 or 2 no more or less)
and doubly make sure the item is actally in the list.
'''

def complete_task(todo_list, completed_list):

#Checks to make sure the todo list has something actually in it
#otherwise no reason to move forward
    if todo_list == []:
        print("\nYour todo list is already completed!")
        input("Please hit enter after reading this to confirm!")
        return
    good_input = False
    
    #This is a loop that will go on until a correct answer is supplied! 
    while good_input == False:
        
        print("\nChoose an item to mark completed.")
        
        print_todo_list(todo_list)
        
        user_task_done = int(input("Please choose one of the options above: "))        
        
        #Checks answer if it is good input from the user
        if user_task_done <= 0 or user_task_done > len(todo_list) + 1:
            print("\nError Element does not exsist!")
            good_input = False
       
        #proceeds to add and remove element from todo list and completed list
        else:
            good_input = True
            element_done = todo_list[user_task_done - 1]
            todo_list.remove(element_done)
            completed_list.append(element_done)
            
    return



#Main Function of the program, contains main loop will allow the user
#to navigate the menu and choose an option and eventually terminate itself!
def main():
    
    #creating empty lists, and a bool operator
    todo_list = []
    completed_list = []
    exit_program = False
    print("Welcome to the Todo List Application.")
    
    #Loop will terminate only when the user chooses to
    while exit_program == False:
        print_menu()
        user_menu_choice = int(input("Please choose one of the options above: "))
        
        #This determins what path the user will take given menu choices
        
        if user_menu_choice == 5:
            exit_program = True 
            
        elif user_menu_choice == 1:
            print_todo_list(todo_list)
            input("Hit enter when finished viewing")
            
        elif user_menu_choice == 2:
            print_completed_tasks(completed_list)
            input("Hit enter when finished viewing")
            
        elif user_menu_choice == 3:
            add_to_todo_list(todo_list)
        
        elif user_menu_choice == 4:
            complete_task(todo_list, completed_list)
            
        #An Error will occur if an answer supplied is not a choice in selection
        else:
            print("ERROR Menu Option does not exsist! ")
            
    print("\nThank you for using this Todo List Application!")


    
if __name__ == "__main__":
    main()