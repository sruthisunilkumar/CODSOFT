# Define an empty list to store tasks
todo_list = []

# Function to add a task to the list
def add_task(task):
    todo_list.append(task)
    print("Task added successfully.")

# Function to remove a task from the list
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print("Task removed successfully.")
    else:
        print("Task not found.")

# Function to view all tasks in the list
def view_tasks():
    if todo_list:
        print("Tasks:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks in the list.")

# Main function to interact with the user
def main():
    while True:
        print("\nChoose an option:")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if _name_ == "_main_":
    main()
