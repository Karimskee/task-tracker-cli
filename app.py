"""
Task tracker is a project used to track and manage your tasks. In this task, you will build a
simple command line interface (CLI) to track what you need to do, what you have done, and what you
are currently working on. This project will help you practice your programming skills, including
working with the filesystem, handling user inputs, and building a simple CLI application.
"""

import json
import sys
from helpers import commands, print_commands, tasks, execute_command


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
            "Correct usage: python app.py [command] [argument 1] [argument 2] etc...\n"
        )
        print_commands()

    elif prompt[1] not in [
        command["name"] for command in commands
    ]:  # Incorrect command

        print("Invalid command.\n")
        print_commands()

    else:  # Correct command

        execute_command(" ".join(prompt[1:]))  # Validate arguments and execute command

    store_tasks()
    print()


def store_tasks():
    """
    Stores the tasks list in a JSON file named "tasks.json".

    The file is opened in write mode and the tasks list is written to it in JSON format.
    The tasks list is converted to a list of dictionaries using the __dict__ method of each Task
    object.
    The indent parameter of json.dump is set to 4 to format the JSON output with indentation.
    """
    file_name = "tasks.json"

    with open(file_name, mode="w", encoding="utf-8") as file:
        json.dump(tasks, fp=file, indent=4)
        file.write("\n")


def retrieve_tasks():
    """
    Retrieves the tasks from a JSON file named "tasks.json" and stores them in the tasks list.

    The file is opened in read mode and the tasks list is read from it in JSON format.
    The tasks list is converted from a list of dictionaries to a list of Task objects using the **
    operator.
    If the file does not exist or is empty, the tasks list is not modified.
    If the file contains invalid JSON, a JSONDecodeError is caught and the tasks list is not
    modified.
    """
    global tasks
    file_name = "tasks.json"

    with open(file_name, mode="r", encoding="utf-8") as file:
        try:
            task = json.load(file)
        except json.JSONDecodeError:
            pass
        else:
            tasks += task


if __name__ == "__main__":
    main()
