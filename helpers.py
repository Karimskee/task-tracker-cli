"""
Self-implemented helper classes, variables and functions
"""
import csv
import datetime
import sys
import time


class Task:
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    # @property
    # def id(self):
    #      return self._id
    
    # @property
    # def description(self):
    #      return self._description

    # @property
    # def status(self):
    #      return self._status
    
    # @property
    # def createdAt(self):
    #      return self._createdAt
    
    # @property
    # def updatedAt(self):
    #      return self._updatedAt
    

    def add(self):
        print("add command executed.")

    def update(self):
        print("update command executed.")

    def delete(self):
        print("delete command executed.")

    def mark_in_progress(self):
        print("mark_in_progress command executed.")

    def mark_done(self):
        print("mark_done command executed.")

    def list(self):
        print("list command executed.")

    def list_done(self):
        print("list_done command executed.")

    def list_todo(self):
        print("list_todo command executed.")

    def list_in_progress(self):
        print("list_in_progress command executed.")


tasks = [
     
]


class Command:
    def __init__(self, name, arg_desc, arg_count):
        self.name = name
        self.arg_desc = arg_desc
        self.arg_count = arg_count

    
    def execute_command(self, command, input):
        if  command.name == "add" and \
            len(input) >= 3:
                tasks.append(Task(
                                    len(tasks),
                                    ' '.join(input[2:]),
                                    "todo",
                                    datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S"),
                                    datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
                                ))
                
                # print(tasks[0]._id,
                #       tasks[0]._description,
                #       tasks[0]._status,
                #       tasks[0]._createdAt,
                #       tasks[0]._updatedAt,
                #       sep="\n"
                #       )
                print(f"Task added successfully (ID: {len(tasks) - 1})")

        elif command.name == "update" and \
             len(input) >= 4 and \
             input[2].isnumeric():
                if int(input[2]) > len(tasks) - 1: # Invalid task number
                    print("Invalid task number.")
                    print("No changes have been made.")

                else: # Valid task number
                    tasks[int(input[2])].description = ' '.join(input[3:])
                    tasks[int(input[2])].updatedAt = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")

                    print(f"Task updated successfully (ID: {input[2]})")

        elif command.name == "delete" and \
             len(input) >= 3 and \
             input[2].isnumeric():
                if int(input[2]) > len(tasks) - 1: # Invalid task number
                    print("Invalid task number.")
                    print("No changes have been made.")

                else: # Valid task number
                    tasks.pop(int(input[2]))
                    
                    # Reassign IDs
                    for i in range(len(tasks)):
                         tasks[i].id = i
                         
                    print(f"Task deleted successfully (ID: {input[2]})")

        elif command.name == "mark-in-progress" and \
             len(input) >= 3 and \
             input[2].isnumeric():
                if int(input[2]) > len(tasks) - 1: # Invalid task number
                    print("Invalid task number.")
                    print("No changes have been made.")

                else: # Valid task number
                    tasks[int(input[2])].status = "in-progress"
                    tasks[int(input[2])].updatedAt = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
                         
                    print(f"Task made in progress successfully (ID: {input[2]})")

        elif command.name == "mark-done" and \
             len(input) >= 3 and \
             input[2].isnumeric():
                if int(input[2]) > len(tasks) - 1: # Invalid task number
                    print("Invalid task number.")
                    print("No changes have been made.")

                else: # Valid task number
                    tasks[int(input[2])].status = "done"
                    tasks[int(input[2])].updatedAt = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
                         
                    print(f"Task made in progress successfully (ID: {input[2]})")
                print("Task has been marked done.")

        elif command.name == "list":
                if len(input) >= 3 and input[2] == "done":
                    if len(tasks) == 0:
                         print("No tasks to display")
                    else:
                         for task in tasks:
                            if task.status == "done":
                                print(
                                     f"Task #{task.id}",
                                     f"Description: {task.description}",
                                     f"Status: {task.status}",
                                     f"Created At: {task.createdAt}",
                                     f"Updated At: {task.updatedAt}",
                                     "",
                                     sep="\n"
                                )
                    print("Finished tasks have been displayed.")
                    
                elif len(input) >= 3 and input[2] == "todo":
                    if len(tasks) == 0:
                         print("No tasks to display")
                    else:
                         for task in tasks:
                            if task.status == "todo":
                                print(
                                     f"Task #{task.id}",
                                     f"Description: {task.description}",
                                     f"Status: {task.status}",
                                     f"Created At: {task.createdAt}",
                                     f"Updated At: {task.updatedAt}",
                                     "",
                                     sep="\n"
                                )
                    print("Todo tasks have been displayed.")

                elif len(input) >= 3 and input[2] == "in-progress":
                    if len(tasks) == 0:
                         print("No tasks to display")
                    else:
                         for task in tasks:
                            if task.status == "in-progress":
                                print(
                                     f"Task #{task.id}",
                                     f"Description: {task.description}",
                                     f"Status: {task.status}",
                                     f"Created At: {task.createdAt}",
                                     f"Updated At: {task.updatedAt}",
                                     "",
                                     sep="\n"
                                )
                    print("In progress tasks have been displayed.")

                else:
                    if len(tasks) == 0:
                         print("No tasks to display")
                    else:
                         for task in tasks:
                              print(
                                   f"Task #{task.id}",
                                   f"Description: {task.description}",
                                   f"Status: {task.status}",
                                   f"Created At: {task.createdAt}",
                                   f"Updated At: {task.updatedAt}",
                                   "",
                                   sep="\n"
                              )
                    print("All tasks have been displayed.")
        else:
            print(f"Invalid arguments, correct usage: {command.name} {command.arg_desc}")
            print("No changes have been made.")


commands = [
    Command("add", "[Task description]", 1),
    Command("update", "[Task number] [Task description]", 2),
    Command("delete", "[Task number]", 1),
    Command("mark-in-progress", "[Task number]", 1),
    Command("mark-done", "[Task number]", 1),
    Command("list", "[done / todo / in-progress] or leave blank to show all tasks", 0),
]


def print_commands():
    """Displays the list of program commands"""
    max_key_size = max([len(command.name) for command in commands]) # For alignment
    
    # Heading
    command_to_argument = f"{"command".ljust(max_key_size)}: Arguments"
    print(command_to_argument)
    print("-" * len(command_to_argument))

    # Commands
    for command in commands:
        print(f"{command.name.ljust(max_key_size)}: {command.arg_desc}")


def helper():
    """Shows file documentation"""
    ...


if __name__ == "__main__":
    helper()
