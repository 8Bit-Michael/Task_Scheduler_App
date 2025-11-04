from scheduler import TaskScheduler
from difflib import get_close_matches

def match_input(user_input, options, cutoff=0.6):
    return get_close_matches(user_input.lower(), options, n=1, cutoff=cutoff)
    
    
def main():
    scheduler = TaskScheduler([])

    while True:
        command = input("""Enter a command:
        1. Add task
        2. View next task
        3. Complete task
        4. View all tasks
        5. Save tasks
        6. Load tasks
        0. Exit
        """)

        # title, description, due_date, priority

        if match_input(command, ['add task', '1']):
            title = input("Enter your task title: ")
            description = input("Enter your task description: ")
            due_date = input("Enter your task due date (MM/DD/YY): ")
            priority = int(input("Enter your task priority (1-5, 1 is lowest priority): "))
            result = scheduler.add_task(title, description, due_date, priority)
            print(result)
        
        elif match_input(command, ['view next task', '2']):
            result = scheduler.view_next_task()
            print(result)

        elif match_input(command, ['complete task', '3']):
            result = scheduler.complete_task()
            print(result)
        
        elif match_input(command, ['view all tasks', '4']):
            result = scheduler.view_all_tasks()
            print(result)

        elif match_input(command, ['save tasks', '5']):
            filename = input("Enter filename to save tasks: ")
            result = scheduler.save_to_file(filename)
            print(result)
        
        elif match_input(command, ['load tasks', '6']):
            filename = input("Enter filename to load tasks: ")
            result = scheduler.load_from_file(filename)
            print(result)

        elif match_input(command, ['exit', '0']):
            print("Exiting the application.")
            exit(0)

        else:
            matches = match_input(command, 
            ['add', 'delete', 'undo', 'redo', 'show', 'save', 
             'load', 'exit', '1', '2', '3', '4', '5', '6', '7', '0'])
            if matches:
                command = input(f"Did you mean '{matches[0]}'?")
                print("Returning to menu...")
                return
            else:
                print("Unknown command. Please try again.")
                return


while __name__ == '__main__':
    main()
