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

    def add_task(self, title, description, due_date, priority):
        if priority < 1 or priority > 5:
            # the return in this condition would stop the function
            return f"Priority must be between 1 and 5."
        
        # however if the function has not stopped then we can proceed
        task = Task(title, description, due_date, priority)

        # if queue is empty just add
        if not self.queue:
            self.queue.append(task)
            return 
        
        # otherwise use the algorithm to insert based on priority
        
        # for the tuple inside of self.queue
        for idx, existing in enumerate(self.queue):
            # if the existing task has a lower priority than the new task
            if existing.priority < priority:
                # insert the new task before the existing one
                self.queue.insert(idx, task)
                return

        # If none are found append at the end
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
        tasks = []
        for i in self.queue:
            tasks.append(i)
        return tasks

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
    scheduler.add_task(
        "Go get groceries", 
        "Buy milk, eggs, and bread",
        "11/7/25",
        5
        )
    print(f"Task successfully added: {scheduler.queue[len(scheduler.queue)-1]}") 
    scheduler.add_task(
        "Finish your homework", 
        "Social Studies worksheet and Math problems",
        "11/3/25",
        1
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

def view_all_test():
    print("=== Test: View All Tasks ===")
    all_tasks = scheduler.view_all_tasks()
    if not all_tasks:
        print("No tasks in the queue.")
        return
    print("[")
    for i, t in enumerate(all_tasks): # t is there for the task and the i for index
        suffix = "," if i < len(all_tasks) - 1 else "" # Add a comma except for the last item
        print(f"    {t}{suffix}") # Indent for readability
    print("]")

task_test() # Make a test instance that shouldn't appear in the actual queue
add_test() # Use the add function for automation in same queue
view_next_test() # Look at task[0]
complete_task() # Complete task[0]
view_next_test() # Look at task[0] again(should be different now)
view_all_test() # View all tasks in the queue (should be sorted by priority)
    
