"""
Task tracker is a project used to track and manage your tasks. In this task, you will build a simple
command line interface (CLI) to track what you need to do, what you have done, and what you are
currently working on. This project will help you practice your programming skills, including working
with the filesystem, handling user inputs, and building a simple CLI application.
"""
from helpers import *


def main():
    """Main program flow"""
    retrieve_tasks()

    # Print the opening user interface
    opening_ui = "\n\
        \rA great day to manage some tasks out eh?\n\
        \r========================================\n\
        "
    print(opening_ui)

    # Handle user input
    input = sys.argv
    input_size = len(input)

    if input_size <= 1: # Incorrect usage
        print("Correct usage: python .\\task-cli.py [command] [argument 1] [argument 2] etc...\n")
        print_commands()

    elif input[1] not in [command.name for command in commands]: # Incorrect command
        print("Invalid command.")
        print_commands()
    
    else: # Correct command
        command = [command for command in commands if input[1] == command.name][0]
        command.execute_command(command, input) # Validate arguments and execute command
        
    store_tasks()

    print()



# TODO: Retrieve tasks from database
def retrieve_tasks():
    file_name = "tasks.csv"
    fieldnames = ["id", "description", "status", "createdAt", "updatedAt"]
    
    with open(file_name, mode="r") as file:
        reader = csv.DictReader(file, fieldnames=fieldnames)

        for row in reader:
            if row["id"] == "id": # Skip header row
                continue

            tasks.append(Task(
                row["id"],
                row["description"],
                row["status"],
                row["createdAt"],
                row["updatedAt"]
            ))


# TODO: Store tasks to database
def store_tasks():
    file_name = "tasks.csv"
    fieldnames = ["id", "description", "status", "createdAt", "updatedAt"]
    
    with open(file_name, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for task in tasks:
            writer.writerow({
                "id": task.id,
                "description": task.description,
                "status": task.status,
                "createdAt": task.createdAt,
                "updatedAt": task.updatedAt
            })


if __name__ == "__main__":
    main()
