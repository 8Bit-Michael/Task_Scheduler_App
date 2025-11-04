This repository contains a command-line task scheduling system that uses queues for task management.
Tasks are sorted by priority (1–5) and follow a first-in, first-out (FIFO) order within each priority level.

Here's an example of the usage:

Enter a command:
1. Add task
2. View next task
3. Complete task
4. View all tasks
5. Save tasks
6. Load tasks
0. Exit

> 1
Enter your task title: clean up room
Enter your task description: sweep floor, make bed, pick up trash
Enter your task due date (MM/DD/YY): 11/14/25
Enter your task priority (1-5, 1 is lowest): 4
'clean up room' added as the first task.

> 1
Enter your task title: buy groceries
Enter your task description: buy bread, milk, eggs
Enter your task due date (MM/DD/YY): 11/5/25
Enter your task priority (1-5, 1 is lowest): 5
'buy groceries' added at position 0 in the queue.

> 4
[('buy groceries', 'buy bread, milk, eggs', '11/5/25', 5),
 ('clean up room', 'sweep floor, make bed, pick up trash', '11/14/25', 4)]

> 3
'buy groceries' completed. 1 task remaining.

> 2
Head task: ('clean up room', 'sweep floor, make bed, pick up trash', '11/14/25', 4)

> 5
Enter filename to save tasks: test_file.txt
Tasks saved successfully.

> 6
Enter filename to load tasks: test_file.txt
Tasks successfully loaded.

> 4
[('clean up room', 'sweep floor, make bed, pick up trash', '11/14/25', 4)]
