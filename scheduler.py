from collections import deque 
# An installation optimized to handle double-ended queues instantly
class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority

class TaskScheduler:
    def __init__(self, queue):
        self.queue = deque()

    def add_task(self):
        pass
    
    def view_next_task(self):
        pass

    def complete_task(self):
        pass

    def view_all_tasks(self):
        pass


def task_test():
    print("=== Test: Task Initialization ===")
    task = Task(
        title ='Walking the dog',
        description ='Walk to the ivy',
        due_date ='10/29/25',
        priority=1
    )
    print(f"Title: {task.title} | Description: {task.description}| Due Date: {task.due_date} | Priority{task.priority}")

task_test()
