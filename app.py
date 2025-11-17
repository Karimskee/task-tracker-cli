"""
Task tracker is a project used to track and manage your tasks. In this task, you will build a simple
command line interface (CLI) to track what you need to do, what you have done, and what you are
currently working on. This project will help you practice your programming skills, including working
with the filesystem, handling user inputs, and building a simple CLI application.
"""
from helpers import *
import sys
import time


def main():
    """Main program flow"""
    ...
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

    
    else:
        command = [command for command in commands if input[1] == command.name][0]
        command.execute_command(command, input)
        
    print()


if __name__ == "__main__":
    main()
