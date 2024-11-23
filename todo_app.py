def deletetask():
    try:
        with open("list.txt", 'r') as tasklist:
            tasks = tasklist.readlines()  # Read all tasks as a list
    except FileNotFoundError:
        print("No tasks available. The file does not exist.")
        return

    if not tasks: # Check if task list is empty
        print("No task available.")
        return

    # Display tasks for the user to choose
    print("Here are your current tasks:")
    for index, task in enumerate(tasks, 1):  # Display tasks with index starting from 1
        print(f"{index}. {task.strip()}")

    # Get the task number to delete
    try:
        task_to_del = int(input("Which task would you like to delete: "))
        if  task_to_del < 1 or task_to_del > len(tasks):
            print(f"Invalid task number. Please enter a number between 1 and {len(tasks)}.")
            return
    except ValueError:
        print("Please enter a valid task number.")
        return

    # Remove the task and save the updated list to the file
    delete_task = tasks.pop(task_to_del-1) # Remove the selected task
    with open("list.txt",'w') as taskfile:
        taskfile.writelines(tasks) # Write updated tasks back to the file

    print(f"Task '{delete_task.strip()}' has been deleted.")


def addtask(): # Adds a new task to the task list.
    try:
        # Open the file in append mode to add a new task
        with open("list.txt", "a") as taskfile:
            task_to_add = input("Enter the task to add: ").strip()
            if task_to_add:
                taskfile.write(task_to_add + "\n")
                print(f"Task '{task_to_add}' has been added to the list.")
            else:
                print("Task cannot be empty. Please provide a valid task description.")
    except Exception as e:
        print(f"An error occurred while adding the task: {e}")


def viewtask():
    try:
        # Open the file in read mode
        with open("list.txt", "r") as taskfile:
            tasks = taskfile.readlines()  # Read all tasks into a list

        if tasks:  # Check if the task list is not empty
            print(" -: Task List :- ")
            for index, task in enumerate(tasks, 1):  # Display tasks with index
                print(f"{index}. {task.strip()}")
        else:
            print("No tasks available.")
    except FileNotFoundError:  # Handle case where file does not exist
        print("No tasks available. The file does not exist.")



def todo_app():
    """Main function for the To-Do App."""
    print("WELCOME to the To-Do App!")
    print("Options: v(view tasks), a(add task), d(delete task), q(quit)")

    while True:
        taskinput = input("\nWhat would you like to do? (v/a/d/q): ").strip().lower()
        if taskinput == "v":
            viewtask()
        elif taskinput == "a":
            addtask()
        elif taskinput == "d":
            deletetask()
        elif taskinput == "q":
            print("Thank you for using the To-Do App. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'v', 'a', 'd', or 'q'.\n")



# Start the app
todo_app()