"""
Self-implemented helper classes, variables and functions
"""

import datetime


TIME_FORMAT = "%d-%m-%Y, %H:%M:%S"  # For tasks created_at and updated_at attribute

tasks = []  # A list of tasks (dict)
TASK_TEMPLATE = {
    "task_id": int(),
    "description": str(),
    "status": "todo",
    "created_at": str(),
    "updated_at": str(),
}


def improper_usage(cmd: dict):
    """Prints an improper usage message to the console."""
    print("Improper usage.")
    print(f"Correct usage: python app.py {cmd["name"]} {cmd["args"]}")


def print_task(task: dict, cmd: dict):
    """Prints a task to the console."""
    print(f"Task {cmd["name"]}ed successfully.")
    print(f"Task ID: {task['task_id']}")
    print(f"Task description: {task['description']}")
    print(f"Task status: {task['status']}")
    print(f"Task created at: {task['created_at']}")
    print(f"Task updated at: {task['updated_at']}")


def is_valid_arguments(cmd: dict, args: list, required_args_types: list) -> int:
    """Validates the arguments of a command."""
    required_args_num = len(required_args_types)  # Number of required arguments

    # Incorrect number of arguments
    if len(args) < required_args_num:
        improper_usage(cmd)
        return 1  # Incorrect number of arguments

    # Incorrect argument types
    args_types = [
        int if arg.isnumeric() else type(arg) for arg in args[:required_args_num]
    ]

    # # For each required argument
    for i in range(required_args_num):
        if required_args_types[i] == any:  # No specific argument type
            continue

        if required_args_types[i] != args_types[i]:  # Incorrect argument type
            improper_usage(cmd)
            return 2  # Incorrect argument type

    # If empty tasks list
    if int in args_types and not tasks:
        print(f"No tasks to {cmd["name"]}.")
        return 3  # No tasks

    # Incorrect task number
    if int in args_types and int([arg for arg in args if arg.isnumeric()][0]) >= len(
        tasks
    ):
        print("Invalid task number.")
        return (
            4  # Invalid task number (task number is greater than the number of tasks)
        )

    return 0


def add_task(cmd: dict, args: list):
    """Adds a task to the tasks list"""
    # Validate arguments
    if is_valid_arguments(cmd, args, [any]) != 0:
        return False

    # Create task
    task = TASK_TEMPLATE.copy()

    task["task_id"] = len(tasks)
    task["description"] = " ".join(args)
    task["status"] = "todo"
    task["created_at"] = datetime.datetime.now().strftime(TIME_FORMAT)
    task["updated_at"] = datetime.datetime.now().strftime(TIME_FORMAT)

    tasks.append(task)

    # Print task details
    print_task(task, cmd)

    return True


def update_task(cmd: dict, args: list):
    """Updates an existing task in the tasks list"""
    # Validate arguments
    if is_valid_arguments(cmd, args, [int, any]) != 0:
        return False

    # Update task details
    task = tasks[int(args[0])]

    task["description"] = " ".join(args[1:])
    task["updated_at"] = datetime.datetime.now().strftime(TIME_FORMAT)

    # Print task details
    print_task(task, cmd)

    return True


def delete_task(cmd: dict, args: list):
    """Deletes an existing task from the tasks list."""
    # Validate arguments
    if is_valid_arguments(cmd, args, [int]) != 0:
        return False

    # Delete task
    deleted_task = tasks.pop(int(args[0]))

    # Reassign IDs (so they always start from 0 and increment up to len(tasks) - 1)
    for i, task in enumerate(tasks):
        task["task_id"] = i

    # Print task details
    print_task(deleted_task, cmd)

    return True


def mark(cmd: dict, args: list):
    """
    Marks a task as either "in-progress" or "done".

    Parameters:
    cmd (dict): A dictionary containing the command name and its arguments.
    args (list): A list of arguments passed to the command.

    Returns:
    bool: True if the task was marked successfully, False otherwise.
    """
    # Validate arguments
    if is_valid_arguments(cmd, args, [str, int]) != 0:
        return False

    # Validate status
    status = args[0]

    if status not in ["in-progress", "done"]:
        print(f'"{status}" is not a valid task status.')
        print('Try using "in-progress" or "done" instead.')
        return False

    # Update task details
    task = tasks[int(args[1])]

    task["status"] = status
    task["updated_at"] = datetime.datetime.now().strftime(TIME_FORMAT)

    # Print task details
    print_task(task, cmd)

    return True


# def list_done(cmd: dict, args: str):
#     print("listed done task")


# def list_todo(cmd: dict, args: str):
#     print("listed todo task")


# def list_in_progress(cmd: dict, args: str):
#     print("listed in progress task")


# def list_all(cmd: dict, args: str):
#     print("listed all task")


commands = [
    {"name": "add", "runner": add_task, "args": "<task description>"},
    {
        "name": "update",
        "runner": update_task,
        "args": "<task number> <task description>",
    },
    {"name": "delete", "runner": delete_task, "args": "<task number>"},
    {"name": "mark", "runner": mark, "args": "<in-progress/done> <task number>"},
    # {"name": "list done", "runner": list_done, "args": ""},
    # {"name": "list todo", "runner": list_todo, "args": ""},
    # {"name": "list in-progress", "runner": list_in_progress, "args": ""},
    # {"name": "list", "runner": list_all, "args": ""},
]


# REFACTOR pass arguments as a list
def execute_command(prompt: str):
    """Execute a command based on the given prompt."""
    matching_cmds = [cmd for cmd in commands if prompt.startswith(cmd["name"])]

    cmd_to_execute = matching_cmds[0]
    args = prompt.removeprefix(cmd_to_execute["name"])
    cmd_to_execute["runner"](cmd=cmd_to_execute, args=args.split())


def print_commands():
    """Displays the list of program commands"""
    # Heading
    command_to_argument = "Commands and their arguments"
    print(command_to_argument)
    print("-" * len(command_to_argument))

    # Notation explanation
    print("<> -> Required")
    # print("() -> Choose none or one")
    print()

    # Commands
    for command in commands:
        print(f"{command["name"]} {command["args"]}")
