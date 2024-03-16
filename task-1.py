class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Invalid task index")

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            print(f"Task {task_index + 1}: {task} is marked as completed")
        else:
            print("Invalid task index")

    def display_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"Task {i + 1}: {task}")

def main():
    to_do_list = ToDoList()
    while True:
        print("\nTo-Do List Application")
        print("1. Add task")
        print("2. Delete task")
        print("3. Mark as completed")
        print("4. Display tasks")
        print("5. Quit")
        option = int(input("Enter your option: "))
        if option == 1:
            task = input("Enter the task: ")
            to_do_list.add_task(task)
        elif option == 2:
            task_index = int(input("Enter the task index to delete: ")) - 1
            to_do_list.delete_task(task_index)
        elif option == 3:
            task_index = int(input("Enter the task index to mark as completed: ")) - 1
            to_do_list.mark_completed(task_index)
        elif option == 4:
            to_do_list.display_tasks()
        elif option == 5:
            break
        else:
            print("Invalid option, please try again")

if __name__ == "__main__":
    main()