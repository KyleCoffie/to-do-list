# Project Requirements
# User Interface (UI):
# Create a command-line interface (CLI) for the To-Do List Application.
# Display a welcoming message and a menu with the following options:
#         Welcome to the To-Do List App!

#         Menu:
#         1. Add a task
#         2. View tasks
#         3. Mark a task as complete
#         4. Delete a task
#         5. Quit
# To-Do List Features:
# Implement the following features for the To-Do List:
# Adding a task with a title (by default “Incomplete”).
# Viewing the list of tasks with their titles and statuses (e.g., "Incomplete" or "Complete").
# Marking a task as complete.
# Deleting a task.
# Quitting the application.
# User Interaction:
# Allow users to interact with the application by selecting menu options using input().
# Implement input validation to handle unexpected user input gracefully.
# Error Handling:
# Implement error handling using try, except, else, and finally blocks to handle potential issues.
# Code Organization:
# Organize your code into functions to promote modularity and readability.
# Use meaningful function names with appropriate comments and docstrings for clarity.
# Testing and Debugging:
# Thoroughly test your application to identify and fix any bugs.
# Consider edge cases, such as empty task lists or incorrect user input.
# Documentation:
# Include a README file that explains how to run the application and provides a brief overview of its features.
# Optional Features (Bonus):
# If you feel adventurous, you can add extra features like task priorities, due dates, or color-coding tasks based on their status.
# GitHub Repository:
# Create a GitHub repository for your project.
# Commit your code to the repository regularly.
# Include a link to your GitHub repository in your project documentation.

tasks = []
# [
    # {'Task': 'hello', 'completed': False}, OBJECT 1 
    # {'Task': 'value', 'completed': Boolean} OBJECT 2
# ]

def add_tasks():
            tasks.append({"Task" :task, "completed" : False})
            print(f"Task '{task}' added to the list.")
            #print(tasks)
        
        
def list_task():
    if not tasks:
        print("There are no task in you list")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
                    status = "Completed" if task["completed"] else "Not Completed"
                    print(f"Task #{index +1}. {task['Task']} = {status}")

        
def complete_task():
    list_task()
    complete_task = int(input("Enter the task # to mark as completed ")) 
    try:
        #print(tasks[complete_task -1])
        #complete_task == len(tasks)
        tasks[complete_task -1]["completed"] = True
        #print(len(tasks))
        #print(tasks[complete_task])
        print (f"Task '{tasks[complete_task -1]["Task"]}' marked completed!")
    except IndexError:
        print("Invalid task #")

            
def delete_task():
    list_task()
    try:
        tasktodelete = int(input("Enter the # to delete: " ))
        if tasktodelete -1 >=0 and tasktodelete -1 < len(tasks):
            tasks.pop(tasktodelete-1)
            print(f"Task #{tasktodelete} has been removed.")
        else:
            print(f"Task #{tasktodelete} was not found.")
    except ValueError:
        print("Invalid input")    
                
if __name__ =="__main__":
  
#To-Do List Features:
    while True:
        print("====== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice ")
    #Implement the following features for the To-Do List:
        if choice == "1":
            task = input("Please enter a task: ")

            add_tasks()
        elif choice == "2":
            list_task()
        elif choice == "3":
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Thank you for using this To-Do program")
            break
        else:
            print("please choose a valid number") 