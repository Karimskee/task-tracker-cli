"""
Self-implemented helper classes, variables and functions
"""

import datetime


TIME_FORMAT = "%d-%m-%Y, %H:%M:%S"


tasks = []
TASK_TEMPLATE = {
    "task_id": int(),
    "description": str(),
    "status": "todo",
    "created_at": str(),
    "updated_at": str(),
}


def improper_usage(cmd : dict):
    print("Improper usage.")
    print(f"Correct usage: python app.py {cmd["name"]} {cmd["args"]}")


def print_task(task : dict):
    print(f"Task ID: {task['task_id']}")
    print(f"Task description: {task['description']}")
    print(f"Task status: {task['status']}")
    print(f"Task created at: {task['created_at']}")
    print(f"Task updated at: {task['updated_at']}")


def add_task(cmd : dict, args : str):
    """Adds a task to the tasks list"""
    # Incorrect command usage
    if not args:
        improper_usage(cmd)

        return False
    
    # Correct command usage
    ## Create task
    task = TASK_TEMPLATE.copy()

    task["task_id"] = len(tasks)
    task["description"] = args
    task["status"] = "todo"
    task["created_at"] = datetime.datetime.now().strftime(TIME_FORMAT)
    task["updated_at"] = datetime.datetime.now().strftime(TIME_FORMAT)

    tasks.append(task)

    # Print task details
    print(f"Task added successfully.")
    print_task(task)

    return True


def update_task(cmd : dict, args : str):
    """Updates an existing task in the tasks list"""
    # Validate arguments
    ## Convert args to a list
    
    
    args_list = args.split()
    
    if (not args_list or len(args) < 2 or not args_list[0].isnumeric()):
        improper_usage(cmd)

        return False
    
    ## Validate task number
    if int(args_list[0]) >= len(tasks):
        print("Invalid task number.")

        return False

    # Update task details
    task = tasks[int(args_list[0])]

    task["description"] = " ".join(args_list[1:])
    task["updated_at"] = datetime.datetime.now().strftime(TIME_FORMAT)

    # Print task details
    print(f"Task updated successfully.")
    print_task(task)

    return True

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
    {"name": "add", "runner": add_task, "args": "<task description>"},
    {"name": "update", "runner": update_task, "args": "<task number> <task description>"},
    {"name": "delete", "runner": delete_task, "args": "<task number>"},
    {"name": "mark-in-progress", "runner": mark_in_progress, "args": "<task number>"},
    {"name": "mark-done", "runner": mark_done, "args": "<task number>"},
    {"name": "list done", "runner": list_done, "args": ""},
    {"name": "list todo", "runner": list_todo, "args": ""},
    {"name": "list in-progress", "runner": list_in_progress, "args": ""},
    {"name": "list", "runner": list_all, "args": ""},
]


def execute_command(prompt : str):
    matching_cmds = [cmd for cmd in commands if prompt.startswith(cmd["name"])]

    cmd_to_execute = matching_cmds[0]
    args = prompt.removeprefix(cmd_to_execute["name"])
    cmd_to_execute["runner"](cmd=cmd_to_execute, args=args.strip())



class Command:
    """For executing commands at the run time."""
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
        if command.name == "update" and len(prompt) >= 4 and prompt[2].isnumeric():
            if int(prompt[2]) > len(tasks) - 1:  # Invalid task number
                print("Invalid task number.")
                print("No changes have been made.")

            else:  # Valid task number
                tasks[int(prompt[2])]["description"] = " ".join(prompt[3:])
                tasks[int(prompt[2])]["updated_at"] = datetime.datetime.now().strftime(
                    TIME_FORMAT
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
                    TIME_FORMAT
                )

                print(f"Task made in progress successfully (ID: {prompt[2]})")

        elif command.name == "mark-done" and len(prompt) >= 3 and prompt[2].isnumeric():
            if int(prompt[2]) > len(tasks) - 1:  # Invalid task number
                print("Invalid task number.")
                print("No changes have been made.")

            else:  # Valid task number
                tasks[int(prompt[2])].status = "done"
                tasks[int(prompt[2])].updated_at = datetime.datetime.now().strftime(
                    TIME_FORMAT
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
        print(f"{command["name"]} {command["args"]}")
