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

    
    def execute_command(self, command, input):
        if  command.name == "add" and \
            len(input) >= 3:
                command.add()
                print("Task has been added.")

        elif command.name == "update" and \
             len(input) >= 4 and \
             input[2].isnumeric():
                command.update()
                print("Task has been updated.")

        elif command.name == "delete" and \
             len(input) >= 3 and \
             input[2].isnumeric():
                command.delete()
                print("Task has been deleted.")

        elif command.name == "mark-in-progress" and \
             len(input) >= 3 and \
             input[2].isnumeric():
                command.mark_in_progress()
                print("Task has been marked in progress.")

        elif command.name == "mark-done" and \
             len(input) >= 3 and \
             input[2].isnumeric():
                command.mark_done()
                print("Task has been marked done.")

        elif command.name == "list":
                if len(input) >= 3 and input[2] == "done":
                    command.list_done()
                    print("Finished tasks have been displayed.")
                    
                elif len(input) >= 3 and input[2] == "todo":
                    command.list_todo()
                    print("Todo tasks have been displayed.")

                elif len(input) >= 3 and input[2] == "in-progress":
                    command.list_in_progress()
                    print("In progress tasks have been displayed.")

                else:
                    command.list()
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
