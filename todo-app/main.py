import json
import os

class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            title=data["title"],
            completed=data["completed"]
        )

class TodoManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        if not os.path.exists("todos.json"):
            return
        
        try:
            with open("todos.json", "r") as file:
                data = json.load(file)
                for item in data:
                    task = Task.from_dict(item)
                    self.tasks.append(task)
        except:
            print("Error loading tasks. Starting fresh.")
    
    def save_tasks(self):
        task_list = [task.to_dict() for task in self.tasks]
        with open("todos.json", "w") as file:
            json.dump(task_list, file, indent=2)
    
    def add_task(self, title):
        if not title.strip():
            print("Task title cannot be empty!")
            return
        
        new_id = max([task.id for task in self.tasks], default=0) + 1
        new_task = Task(new_id, title.strip())
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task added (ID: {new_id})")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        
        print("\n" + "=" * 50)
        print(f"{'ID':<5} {'Status':<12} {'Title':<30}")
        print("=" * 50)
        
        for task in self.tasks:
            status = "Completed" if task.completed else "Pending"
            print(f"{task.id:<5} {status:<12} {task.title:<30}")
        print("=" * 50)
    
    def update_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                new_title = input(f"New title (current: '{task.title}'): ").strip()
                if new_title:
                    task.title = new_title
                
                status_input = input("Mark as completed? (y/n): ").lower()
                if status_input == 'y':
                    task.completed = True
                elif status_input == 'n':
                    task.completed = False
                
                self.save_tasks()
                print("Task updated.")
                return
        
        print(f"Task ID {task_id} not found.")
    
    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print("Task deleted.")
                return
        
        print(f"Task ID {task_id} not found.")

def main():
    manager = TodoManager()
    
    while True:
        print("\n" + "=" * 30)
        print("TODO LIST MANAGER")
        print("=" * 30)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose (1-5): ").strip()
        
        if choice == "1":
            title = input("Enter task title: ")
            manager.add_task(title)
        
        elif choice == "2":
            manager.view_tasks()
        
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to update: "))
                manager.update_task(task_id)
            except:
                print("Invalid input!")
        
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                manager.delete_task(task_id)
            except:
                print("Invalid input!")
        
        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()