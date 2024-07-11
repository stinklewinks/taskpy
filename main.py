import math
import random
import time
import os

tasks = {
    "0": "Wash the dishes",
    "1": "Do laundry",
    "2": "Vacuum house",
    "3": "Take out the trash",
}

random = str(math.floor(random.random() * len(tasks)))

def addTask():
    newTask = input("Enter a new task: ")
    tasks[len(tasks)] = newTask
    # Create a txt file for persistence
    with open("tasks.txt", "a") as f:
        f.write(f"{tasks}")
    print("Task added successfully!")
    time.sleep(1)
    taskChooser()

def completeTask():
    taskToComplete = input("Enter the number of the task you want to complete: ")
    if taskToComplete in tasks:
        del tasks[taskToComplete]
        print("Task completed successfully!")
    else:
        print("Invalid task number. Please try again.")
    time.sleep(1)
    taskChooser()

def editTask():
    taskToEdit = input("Enter the number of the task you want to edit: ")
    if taskToEdit in tasks:
        newTaskDescription = input("Enter the new task description: ")
        tasks[taskToEdit] = newTaskDescription
        print("Task edited successfully!")
    else:
        print("Invalid task number. Please try again.")
    time.sleep(1)
    taskChooser()

def taskChooser():
    # Decide whether to add, complete, or edit tasks
    print("What would you like to do?")
    print("1. Add a task")
    print("2. Complete a task")
    print("3. Edit a task")
    print("Back to Dashboard (d)")
    print("Quit (q)")
    choice = input(f"Enter your choice 0-{len(tasks) - 1}: ")
    if(choice != "1" and choice != "2" and choice != "3" and choice != 'd' and choice != 'q'):
        print("Invalid choice. Please try again.")
        taskChooser()
    elif(choice == "1"):
        addTask()
    elif(choice == "2"):
        completeTask()
    elif(choice == "3"):
        editTask()
    elif(choice == 'd'):
        main()
    else:
        exit()




def main():
    print("Welcome to TaskMate")
    time.sleep(1)
    print("Here are your tasks for today:")
    time.sleep(1)
    for task in tasks:
        time.sleep(.5)
        print(f"{task}: {tasks[task]}")
    taskChooser()

main()