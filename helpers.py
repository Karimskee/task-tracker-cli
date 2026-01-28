"""
Self-implemented helper classes, variables and functions
"""

import datetime


class Task:
    """For managing tasks at the run time."""

    def __init__(self, user_id, description, status, created_at, updated_at):
        """
        Initialize a Task object with the given parameters.

        Parameters:
        id (int): ID of the task
        description (str): Description of the task
        status (str): Status of the task, either "todo", "in-progress", or "done"
        created_at (str): Timestamp when the task was created
        updated_at (str): Timestamp when the task was last updated
        """
        self.user_id = user_id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at


tasks = []


class Command:
    """For executing commands at the run time."""
    # FIXME Use a better approach
    def __init__(self, name, arg_desc):
        """
        Initialize a Command object with the given parameters.

        Parameters:
        name (str): Name of the command
        arg_desc (str): Description of the command's arguments
        """
        self.name, self.arg_desc = name, arg_desc

    def execute_command(self, command, prompt):
        """
        Execute a command with the given arguments.

        Parameters:
        command (Command): Command to be executed
        input (list): List of arguments to be passed to the command
        """
        if command.name == "add" and len(prompt) >= 3:
            tasks.append(
                Task(
                    len(tasks),
                    " ".join(prompt[2:]),
                    "todo",
                    datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S"),
                    datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S"),
                )
            )

            print(f"Task added successfully (ID: {len(tasks) - 1})")

        elif command.name == "update" and len(prompt) >= 4 and prompt[2].isnumeric():
            if int(prompt[2]) > len(tasks) - 1:  # Invalid task number
                print("Invalid task number.")
                print("No changes have been made.")

            else:  # Valid task number
                tasks[int(prompt[2])].description = " ".join(prompt[3:])
                tasks[int(prompt[2])].updated_at = datetime.datetime.now().strftime(
                    "%d-%m-%Y, %H:%M:%S"
                )

                print(f"Task updated successfully (ID: {prompt[2]})")

        elif command.name == "delete" and len(prompt) >= 3 and prompt[2].isnumeric():
            if int(prompt[2]) > len(tasks) - 1:  # Invalid task number
                print("Invalid task number.")
                print("No changes have been made.")

            else:  # Valid task number
                tasks.pop(int(prompt[2]))

                # Reassign IDs
                for i, task in enumerate(tasks):
                    task.user_id = i

                print(f"Task deleted successfully (ID: {prompt[2]})")

        elif (
            command.name == "mark-in-progress"
            and len(prompt) >= 3
            and prompt[2].isnumeric()
        ):
            if int(prompt[2]) > len(tasks) - 1:  # Invalid task number
                print("Invalid task number.")
                print("No changes have been made.")

            else:  # Valid task number
                tasks[int(prompt[2])].status = "in-progress"
                tasks[int(prompt[2])].updated_at = datetime.datetime.now().strftime(
                    "%d-%m-%Y, %H:%M:%S"
                )

                print(f"Task made in progress successfully (ID: {prompt[2]})")

        elif command.name == "mark-done" and len(prompt) >= 3 and prompt[2].isnumeric():
            if int(prompt[2]) > len(tasks) - 1:  # Invalid task number
                print("Invalid task number.")
                print("No changes have been made.")

            else:  # Valid task number
                tasks[int(prompt[2])].status = "done"
                tasks[int(prompt[2])].updated_at = datetime.datetime.now().strftime(
                    "%d-%m-%Y, %H:%M:%S"
                )

                print(f"Task made in progress successfully (ID: {prompt[2]})")
                print("Task has been marked done.")

        elif command.name == "list":
            if len(prompt) >= 3 and prompt[2] == "done":
                if len(tasks) == 0:
                    print("No tasks to display")
                else:
                    for task in tasks:
                        if task.status == "done":
                            print(
                                f"Task #{task.user_id}",
                                f"Description: {task.description}",
                                f"Status: {task.status}",
                                f"Created At: {task.created_at}",
                                f"Updated At: {task.updated_at}",
                                "",
                                sep="\n",
                            )

                    print("Finished tasks have been displayed.")

            elif len(prompt) >= 3 and prompt[2] == "todo":
                if len(tasks) == 0:
                    print("No tasks to display")
                else:
                    for task in tasks:
                        if task.status == "todo":
                            print(
                                f"Task #{task.user_id}",
                                f"Description: {task.description}",
                                f"Status: {task.status}",
                                f"Created At: {task.created_at}",
                                f"Updated At: {task.updated_at}",
                                "",
                                sep="\n",
                            )

                    print("Todo tasks have been displayed.")

            elif len(prompt) >= 3 and prompt[2] == "in-progress":
                if len(tasks) == 0:
                    print("No tasks to display")
                else:
                    for task in tasks:
                        if task.status == "in-progress":
                            print(
                                f"Task #{task.user_id}",
                                f"Description: {task.description}",
                                f"Status: {task.status}",
                                f"Created At: {task.created_at}",
                                f"Updated At: {task.updated_at}",
                                "",
                                sep="\n",
                            )

                    print("In progress tasks have been displayed.")

            else:
                if len(tasks) == 0:
                    print("No tasks to display")
                else:
                    for task in tasks:
                        print(
                            f"Task #{task.user_id}",
                            f"Description: {task.description}",
                            f"Status: {task.status}",
                            f"Created At: {task.created_at}",
                            f"Updated At: {task.updated_at}",
                            "",
                            sep="\n",
                        )
                        
                    print("All tasks have been displayed.")
        else:
            print(
                f"Invalid arguments, correct usage: {command.name} {command.arg_desc}"
            )
            print("No changes have been made.")


commands = [
    Command("add", "<Task description>"),
    Command("update", "<Task number> <Task description>"),
    Command("delete", "<Task number>"),
    Command("mark-in-progress", "<Task number>"),
    Command("mark-done", "<Task number>"),
    Command("list", "(optionaldone / todo / in-progress)"),
]


def print_commands():
    """Displays the list of program commands"""
    max_key_size = max(len(command.name) for command in commands)  # For alignment

    # Heading
    command_to_argument = f"{"command".ljust(max_key_size)}: Arguments"
    print(command_to_argument)
    print("-" * len(command_to_argument))

    # Notation explanation
    print("<> -> Required\n() -> Choose none or one\n")

    # Commands
    for command in commands:
        print(f"{command.name.ljust(max_key_size)}: {command.arg_desc}")
