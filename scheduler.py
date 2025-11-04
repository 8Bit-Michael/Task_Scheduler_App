from collections import deque 
import os

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
        
        if due_date.count('/') != 2:
            return f"Due date must be in MM/DD/YY format."
        
        # however if the function has not stopped then we can proceed
        task = Task(title, description, due_date, priority)

        # if queue is empty just add
        if not self.queue:
            self.queue.append(task)
            return f"'{task.title}' added as the first task."
        
        # otherwise use the algorithm to insert based on priority
        
        # for the tuple inside of self.queue
        for idx, existing in enumerate(self.queue):
            # if the existing task has a lower priority than the new task
            if existing.priority < priority:
                # insert the new task before the existing one
                self.queue.insert(idx, task)
                return f'{task.title} added at position {idx} in the queue.'

        # If none are found append at the end
        self.queue.append(task)
        return f"{task.title} added at the end of the queue."

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
        if not self.queue:
            return "No tasks in the queue."
        else:
            for i in self.queue:
                tasks.append(i)
            return tasks

    def save_to_file(self, filename):
        """Save notes to a text file."""
        with open(filename, 'w') as f:
            for task in self.queue:
                f.write(f"{task}\n")
        return "Tasks saved successfully"

    def load_from_file(self, filename):
        """Load notes from a text file."""
        if not os.path.exists(filename):
            return f"{filename} does not exist"
        with open(filename, 'r') as f:
            self.queue = [line.strip() for line in f.readlines()]
        return "Tasks successfully loaded"
