Hi! this repository contains a task scheduling system in a command line interface, using queues when it comes to the task handling system.
The tasks entered are sorted by priority levels, ranging from 1-5, along with the order in which they were added(first-in, first-out rule). 

The following is an example of how the application can be used:

Enter a command:
        1. Add task
        2. View next task
        3. Complete task
        4. View all tasks
        5. Save tasks
        6. Load tasks
        0. Exit
        1
Enter your task title: clean up room  
Enter your task description: sweep floor, make bed, pick up trash
Enter your task due date (MM/DD/YY): 11/14/25
Enter your task priority (1-5, 1 is lowest priority): 4
'clean up room' added as the first task.
Enter a command:
        1. Add task
        2. View next task
        3. Complete task
        4. View all tasks
        5. Save tasks
        6. Load tasks
        0. Exit
        1
Enter your task title: buy groceries  
Enter your task description: buy bread, milk, eggs
Enter your task due date (MM/DD/YY): 11/5/25
Enter your task priority (1-5, 1 is lowest priority): 5
buy groceries added at position 0 in the queue.
Enter a command:
        1. Add task
        2. View next task
        3. Complete task
        4. View all tasks
        5. Save tasks
        6. Load tasks
        0. Exit
        4
[('buy groceries', 'buy bread, milk, eggs', '11/5/25', 5), ('clean up room', 'sweep floor, make bed, pick up trash', '11/14/25', 4)]
Enter a command:
        1. Add task
        2. View next task
        3. Complete task
        4. View all tasks
        5. Save tasks
        6. Load tasks
        0. Exit
        3
'buy groceries' completed. 1 tasks remaining.
Enter a command:
        1. Add task
        2. View next task
        3. Complete task
        4. View all tasks
        5. Save tasks
        6. Load tasks
        0. Exit
        2
Head task: ('clean up room', 'sweep floor, make bed, pick up trash', '11/14/25', 4)
Enter a command:
        1. Add task
        2. View next task
        3. Complete task
        4. View all tasks
        5. Save tasks
        6. Load tasks
        0. Exit
        5
Enter filename to save tasks: test_file.txt
Tasks saved successfully
Enter a command:
        1. Add task
        2. View next task
        3. Complete task
        4. View all tasks
        5. Save tasks
        6. Load tasks
        0. Exit
        6
Enter filename to load tasks: test_file.txt 
Tasks successfully loaded
Enter a command:
        1. Add task
        2. View next task
        3. Complete task
        4. View all tasks
        5. Save tasks
        6. Load tasks
        0. Exit
        4
["('clean up room', 'sweep floor, make bed, pick up trash', '11/14/25', 4)"]
        5. Save tasks
        6. Load tasks
        0. Exit
