class Task:
    def __init__(self, description, priority, due_date, completed=False):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

import pickle

class TaskManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_path, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.file_path, 'wb') as file:
            pickle.dump(self.tasks, file)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task):
        self.tasks.remove(task)
        self.save_tasks()

    def mark_completed(self, task):
        task.completed = True
        self.save_tasks()

    def get_tasks(self):
        return self.tasks

def display_tasks(tasks):
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task.completed else "Pending"
        print(f"{index}. {task.description} (Priority: {task.priority}, Due Date: {task.due_date}, Status: {status})")

def main():
    file_path = 'tasks.pkl'
    task_manager = TaskManager(file_path)

    while True:
        print("I. Add  Your Task")
        print("II. Remove Task")
        print("III. Mark Task as Completed")
        print("IV. View Tasks")
        print("V. Exit")
        choice = input("Enter your choice: ")

        if choice == 'I':
            description = input("Enter task description: ")
            priority = input("Enter task priority (high/medium/low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = Task(description, priority, due_date)
            task_manager.add_task(task)
        elif choice == 'II':
            tasks = task_manager.get_tasks()
            display_tasks(tasks)
            index = int(input("Enter the task number to remove: ")) - 1
            task_manager.remove_task(tasks[index])
        elif choice == 'III':
            tasks = task_manager.get_tasks()
            display_tasks(tasks)
            index = int(input("Enter the task number to mark as completed: ")) - 1
            task_manager.mark_completed(tasks[index])
        elif choice == 'IV':
            tasks = task_manager.get_tasks()
            display_tasks(tasks)
        elif choice == 'V':
            print("Thank You....")
            break
        else:
            print("access denied")

if __name__ == "__main__":
    main()