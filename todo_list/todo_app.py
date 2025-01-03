def display_menu():
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark as Done")
    print("4. Exit")
    
def add_task(tasks_list):
    task = input("Add task description: ")
    tasks_list.append(task) #add task to tasks list
    print("Task added successfully")
    
def view_task(tasks_list):
    print("\nTasks:") #show list like 1.{task} \n2.{task}
    for i, task in enumerate(tasks_list, start=1):
        print(f"{i}. {task}")
        #enumerate(iterable/object, a number for index default is 0)  = a counter, can change start index
        
def mark_as_done(tasks_list):
    if not tasks_list:
        print("No tasks to mark as done")
        
    view_task(tasks_list) # Display tasks with indices
    mark_task = input("Enter task index to mark as done: ")
    index = int(mark_task) - 1 #int() convert string to int
    
    if 0 <= index < len(tasks_list):
        removed_task = tasks_list.pop(index)
        print(f"Task '{removed_task}' marked as done and removed")
    else:
        print('Invalid task index')

def save_tasks(tasks_list):
    #write tasks_list to file 
    with open("tasks_list.txt", "w") as f:
        for task in tasks_list:
            f.write(task + '\n')
            
def load_tasks():
    #read file
    try:
        with open("tasks_list.txt", 'r') as f:
            return f.read().splitlines()
    
    except FileExistsError:
        return []
        
def main():
    tasks_list = load_tasks()
    #initialize an empty list
    
    while True:
        display_menu() #show menu
        
        choice = input("Enter your choice: ")
        #pick 1-4
        if choice == '1':
            add_task(tasks_list)
        elif choice == '2':
            view_task(tasks_list)
        elif choice == '3':
            mark_as_done(tasks_list)
        elif choice == '4':
            print("Exiting..")
            save_tasks(tasks_list)
            break
        else:
            print("Invalid choice. Please select a valid numnber")
    
#main() to show up in terminal    
if __name__ == "__main__":
    main()
        
    
