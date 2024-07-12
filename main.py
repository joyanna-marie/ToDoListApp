tasks = []

def addTask():
  task = input("Please enter a task: ")
  tasks.append(task)
  print(f"Task '{task}' added successfully!")

def listTasks():
  if not tasks:
    print("There are currently no tasks.")
  else:
    print("Current Tasks:*")
    for index, task in enumerate(tasks):
      print(f"{index}. {task}")

def deletetask():
  listTasks()
  try:
    taskToDelete = int(input("Eneter the number of the task to delete: "))
    if taskToDelete >0 and taskToDelete < len(tasks):
      tasks.pop(taskToDelete)
      print(f"Task {taskToDelete} deleted successfully!")
    else:
      print
  except:
    print("Invalid input.")

if __name__ == "__main__":
  ### Creating a loop to run the app
  print("Welcome to the to do list app!")
  while True:
    print("\n")
    print("Please select one of the follwing options")
    print("-------------------------")
    print("1. Add a task")
    print("2. Delete a task")
    print("3. View all tasks")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
      task = input("Enter the task: ")
      tasks.append(task)
      print("Task added successfully")
    elif choice == "2":
      if len(tasks) == 0:
        print("No tasks to delete")
      else:
        print("Tasks:")
        for i, task in enumerate(tasks):
          print(f"{i+1}. {task}")
        task_index = int(input("Enter the task number to delete: "))
        if task_index > 0 and task_index <= len(tasks):
          del tasks[task_index - 1]
          print("Task deleted successfully")
        else:
          print("Invalid task number")
    elif choice == "3":
      if len(tasks) == 0:
        print("No tasks to view")
      else:
        print("Tasks:")
        for i, task in enumerate(tasks):
          print(f"{i+1}. {task}")
    elif choice == "4":
      print("Exiting the app")
      break
      
