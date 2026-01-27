"""
Task tracker is a project used to track and manage your tasks. In this task, you will build a simple
command line interface (CLI) to track what you need to do, what you have done, and what you are
currently working on. This project will help you practice your programming skills, including working
with the filesystem, handling user inputs, and building a simple CLI application.
"""

import csv
import sys
from helpers import commands, print_commands, Task, tasks


def main():
    """Main program flow"""
    retrieve_tasks()

    # Print the opening user interface
    print(
        """
A great day to manage some tasks out eh?
========================================
"""
    )

    # Handle user input
    prompt = sys.argv
    input_size = len(prompt)

    if input_size <= 1:  # Incorrect usage

        print(
            "Correct usage: python .\\task-cli.py [command] [argument 1] [argument 2] etc...\n"
        )
        print_commands()

    elif prompt[1] not in [command.name for command in commands]:  # Incorrect command

        print("Invalid command.\n")
        print_commands()

    else:  # Correct command

        command = [command for command in commands if prompt[1] == command.name][0]
        command.execute_command(
            command, prompt
        )  # Validate arguments and execute command

    store_tasks()
    print()


def retrieve_tasks():
    """
    Retrieves tasks from a CSV file and stores them in the tasks list.

    Opens a CSV file named "tasks.csv" in read mode and reads the header and all tasks from it.
    The CSV file is then closed and the tasks are stored.
    """
    file_name = "tasks.csv"
    fieldnames = ["id", "description", "status", "created_at", "updated_at"]

    with open(file_name, mode="r", encoding="utf-8") as file:

        reader = csv.DictReader(file, fieldnames=fieldnames)

        for row in reader:

            if row["id"] == "id":  # Skip header row
                continue

            tasks.append(
                Task(
                    row["id"],
                    row["description"],
                    row["status"],
                    row["created_at"],
                    row["updated_at"],
                )
            )


def store_tasks():
    """
    Store tasks to a CSV file.

    Opens a CSV file named "tasks.csv" in write mode and writes the header and all tasks to it.
    The CSV file is then closed and the tasks are stored.
    """
    file_name = "tasks.csv"
    fieldnames = ["id", "description", "status", "created_at", "updated_at"]

    with open(file_name, mode="w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for task in tasks:
            writer.writerow(
                {
                    "id": task.user_id,
                    "description": task.description,
                    "status": task.status,
                    "created_at": task.created_at,
                    "updated_at": task.updated_at,
                }
            )


if __name__ == "__main__":
    main()
