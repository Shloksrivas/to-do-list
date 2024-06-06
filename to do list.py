tasks=[]

def addTask():
    task=input("Enter a task: ")
    tasks.append({"task": task, "done": False})
    print(f"The task '{task}' is added to the list")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the task number to be deleted: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} is removed from the list")
        else:
            print(f"Task {taskToDelete} is not present in the to do list")
    except ValueError:
        print("Invalid Input. Please input a valid task number")

def listTasks():
    if not tasks:
        print("There are no tasks currently in your to do list")
    else:
        print("Your current tasks are: ")
        for index, task in enumerate(tasks):
            status = "Done" if task["done"] else "Not Done"
            print(f"Task {index}. {task['task']} - {status}")   

def markTaskCompleted():
    try:
        task_number = int(input("Enter the task to be marked completed: "))
        if 0 <= task_number and task_number <= len(tasks):
            tasks[task_number]["done"] = True
            print(f"Marked task as completed: {tasks[task_number]['task']}")
        else:
            print("This task number isn't present")
    except ValueError:
        print("Invalid Input. Please enter a valid task number")

if __name__ == "__main__":
    print("welcome to your to do list")
    while True:
        print("\n")
        print("please select one of the following operations")
        print("_____________________________________________")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. Lists the task")
        print("4. Mark the task completed")
        print("5. Quit")

        choice= input("Enter your choice: ")

        if(choice == "1"):
            addTask()
        elif(choice =="2"):
            deleteTask()
        elif(choice == "3"):
            listTasks()
        elif(choice == "4"):
            markTaskCompleted()
        elif(choice == "5"):
            break
        else:
            print("There is no such operations. Please try something else")

    print("Done with your to do lists!")
           