#task management system using Python

import json

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def mark_as_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f'Task "{self.tasks[task_index]["task"]}" marked as complete.')
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Complete" if task["completed"] else "Incomplete"
                print(f'{i + 1}. {task["task"]} - {status}')

    def save_tasks(self, filename="tasks.json"):
        with open(filename, "w") as file:
            json.dump(self.tasks, file)

    def load_tasks(self, filename="tasks.json"):
        try:
            with open(filename, "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            print("No saved tasks found.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Tasks")
        print("4. Save Tasks")
        print("5. Load Tasks")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            task = input("Enter the task: ")
            task_manager.add_task(task)
        elif choice == "2":
            task_manager.view_tasks()
            task_index = int(input("Enter the task index to mark as complete: ")) - 1
            task_manager.mark_as_complete(task_index)
        elif choice == "3":
            task_manager.view_tasks()
        elif choice == "4":
            task_manager.save_tasks()
            print("Tasks saved successfully.")
        elif choice == "5":
            task_manager.load_tasks()
            print("Tasks loaded successfully.")
        elif choice == "6":
            print("Exiting the Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
