
def viewer(task_list):

    if not task_list:  # Check if the list is empty
        print("No tasks to display.")
    else:
        print("Here are your tasks:")
        for i, task in enumerate(task_list, 1):  # Enumerate to number the tasks
            print(f"{i}. {task}")
def viewer(task_list):
    if not task_list:  # Check if the list is empty
        print("No tasks to display.")
    else:
        print("Here are your tasks:")
        for i, task in enumerate(task_list, 1):  # Enumerate to number the tasks
            print(f"{i}. {task}")


def addTask(task_list):

      # Define the list inside the function
    n = int(input("How many tasks do you want to add? "))

    i = 0  # Initialize counter for the while loop
    while i < n:  # Use a while loop instead of for loop
        task1 = input("What task do you want to add: ")
        task_list.append(task1)
        i += 1  # Increment the counter
    return task_list  # Return the list of tasks



def Delete(task_list):
    viewer(task_list)
    remove = (input("Select the index of the task you want to delete or you've just completed: "))

    if not remove.isdigit() or int(remove) < 1 or int(remove) > len(task_list):
        print("Invalid input. Please enter a valid index.")
        return task_list

    task_list.pop(int(remove) - 1)  # Subtract 1 to match list index
    
    return task_list

def print_menu(task_list):
    while True:
        print('\nTodo List Menu:')
        print('1. View Tasks')
        print('2. Add a Task')
        print('3. Remove a Task')
        print('4. Exit')

        choice = int(input("Enter your choice: "))
        menu_index = [1, 2, 3, 4]

        if choice not in menu_index:
            print("Invalid input. Please enter a valid option.")
        elif choice == 1:
            viewer(task_list)
        elif choice == 2:
            addTask(task_list)
        elif choice == 3:
            Delete(task_list)
        elif choice == 4:
            print("Exiting the menu.")
            break  # Exit the loop to end the program


task_list =[]
print_menu(task_list)