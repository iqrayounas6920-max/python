tasks = []

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # ✅ Add Task
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    # ✅ View Tasks
    elif choice == "2":
        print("\nYour Tasks:")

        if len(tasks) == 0:
            print("No task yet")
        else:
            for i, task in enumerate(tasks):
                print(i, task)

    # ✅ Delete Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No task to delete")
        else:
            for i, task in enumerate(tasks):
                print(i, task)

            try:
                index = int(input("Enter task number to delete: "))
                tasks.pop(index)
                print("Task deleted!")
            except:
                print("Invalid input")

    # ✅ Exit
    elif choice == "4":
        print("Goodbye!")
        break

    # ❌ Invalid
    else:
        print("Invalid choice")


