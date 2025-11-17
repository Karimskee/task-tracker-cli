"""
Self-implemented helper classes, variables and functions
"""


class Task:
    def __init__(self, id, description, status, createdAt, updatedAt):
        self._id = id
        self._description = description
        self._status = status
        self._createdAt = createdAt
        self._updatedAt = updatedAt

    # TODO: Retrieve tasks from file

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


class Command:
    def __init__(self, name, arg_desc, arg_count):
        self.name = name
        self.arg_desc = arg_desc
        self.arg_count = arg_count

    # TODO: Command execution method


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
