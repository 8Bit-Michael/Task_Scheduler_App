from collections import deque 
# An installation optimized to handle double-ended queues instantly
class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
    
    def __repr__(self): 
        # Makes the code readable and not just an object address, but rather the object of the address
        return f"({self.title!r}, {self.description!r}, {self.due_date!r}, {self.priority})"

class TaskScheduler:
    def __init__(self, queue):
        self.queue = deque(queue or [])

    def add_task(self, title, description, due_date, priority): # This goes to the back
        task = Task(title, description, due_date, priority)
        self.queue.append(task)

    def view_next_task(self):
        return self.queue[0]

    def complete_task(self):
        pass

    def view_all_tasks(self):
        pass


scheduler = TaskScheduler([])

def task_test():
    print("=== Test: Task Initialization ===")
    task = Task(
        title ='Walking the dog',
        description ='Walk to the ivy',
        due_date ='10/29/25',
        priority=1
    )
    print(f"Title: {task.title} | Description: {task.description}| Due Date: {task.due_date} | Priority: {task.priority}")

def add_test():
    print("=== Test: Task Insertion ===")
    scheduler.add_task(
        "Clean your Clothes", 
        "Take your clothes into the wash",
        "11/2/25",
        2
        )
    print(f"Task successfully added: {scheduler.queue[len(scheduler.queue)-1]}")

task_test()
add_test()
    
    
