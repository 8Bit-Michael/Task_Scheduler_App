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
        if not self.queue:
            return f"No tasks in the queue."
        return f"Head task: {self.queue[0]}"

    def complete_task(self):
        if not self.queue:
            return f"No tasks to complete."
        else:
            deleted = self.queue.popleft() # Removes the task at index 0 
            return f"'{deleted.title}' completed. {len(self.queue)} tasks remaining."

    def view_all_tasks(self):
        pass


scheduler = TaskScheduler([])

def task_test(): # Created an instance BUT didn't add it to the actual queue
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
    scheduler.add_task(
        "Make your bed", 
        "Clean up your bed and arrange pillows",
        "11/1/25",
        4
        )
    print(f"Task successfully added: {scheduler.queue[len(scheduler.queue)-1]}") 

def view_next_test():
    print("=== Test: View Next Task ===")
    next_task = scheduler.view_next_task()
    print(next_task)
    
def complete_task():
    print("=== Test: Complete Task ===")
    result = scheduler.complete_task()
    print(result)

task_test() # Make a test instance that shouldn't appear in the actual queue
add_test() # Use the add function for automation in same queue
view_next_test() # Look at task[0]
complete_task() # Complete task[0]
view_next_test() # Look at task[0] again(should be different now)
    
