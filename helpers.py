"""
Self-implemented helper classes, variables and functions
"""

import datetime


tasks = []
TASK_TEMPLATE = {
    "task_id": int(),
    "description": str(),
    "status": "todo",
    "created_at": str(),
    "updated_at": str(),
}

def add_task(cmd : dict, args : str):
    print("added task")


def update_task(cmd : dict, args : str):
    print("updated task")


def delete_task(cmd : dict, args : str):
    print("deleted task")


def mark_in_progress(cmd : dict, args : str):
    print("mark in progress task")


def mark_done(cmd : dict, args : str):
    print("marked done task")


def list_done(cmd : dict, args : str):
    print("listed done task")


def list_todo(cmd : dict, args : str):
    print("listed todo task")


def list_in_progress(cmd : dict, args : str):
    print("listed in progress task")


def list_all(cmd : dict, args : str):
    print("listed all task")


commands = [
    {"name": "add", "runner": add_task, "description": "<task description>"},
    {"name": "update", "runner": update_task, "description": "<task number> <task description>"},
    {"name": "delete", "runner": delete_task, "description": "<task number>"},
    {"name": "mark-in-progress", "runner": mark_in_progress, "description": "<task number>"},
    {"name": "mark-done", "runner": mark_done, "description": "<task number>"},
    {"name": "list done", "runner": list_done, "description": ""},
    {"name": "list todo", "runner": list_todo, "description": ""},
    {"name": "list in-progress", "runner": list_in_progress, "description": ""},
    {"name": "list", "runner": list_all, "description": ""},
]


def execute_command(prompt : str):
    matching_cmds = [cmd for cmd in commands if prompt.startswith(cmd["name"])]

    cmd_to_execute = matching_cmds[0]
    args = prompt.removeprefix(cmd_to_execute["name"])
    cmd_to_execute["runner"](cmd=cmd_to_execute, args=args.strip())



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
            task = TASK_TEMPLATE.copy()

            task["task_id"] = len(tasks),
            task["description"] = " ".join(prompt[2:]),
            task["status"] = "todo",
            task["created_at"] = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S"),
            task["updated_at"] = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S"),

            tasks.append(task)

            print(f"Task added successfully (ID: {task["task_id"]})")

        elif command.name == "update" and len(prompt) >= 4 and prompt[2].isnumeric():
            if int(prompt[2]) > len(tasks) - 1:  # Invalid task number
                print("Invalid task number.")
                print("No changes have been made.")

            else:  # Valid task number
                tasks[int(prompt[2])]["description"] = " ".join(prompt[3:])
                tasks[int(prompt[2])]["updated_at"] = datetime.datetime.now().strftime(
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


def print_commands():
    """Displays the list of program commands"""
    max_key_size = max(len(command["name"]) for command in commands)  # For alignment

    # Heading
    command_to_argument = f"Commands and their arguments"
    print(command_to_argument)
    print("-" * len(command_to_argument))

    # Notation explanation
    print("<> -> Required")
    # print("() -> Choose none or one")
    print()

    # Commands
    for command in commands:
        print(f"{command["name"]} {command["description"]}")
