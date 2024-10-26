'''3. Task Management System
Problem Statement: Develop a to-do list where users can add, mark as complete, delete, and categorize tasks.
Steps:
Define a Task class with attributes like description, due date, and completion status.
Add methods for adding, completing, and removing tasks.
Organize tasks into categories and sort by priority or due date.'''

from datetime import datetime 

class Task:
    def __init__(self, description, due_date = None, prioirty = 'Medium', category = 'General'):
        '''To initialize a task with a description , optional due date, priority and category.'''
        self.description = description
        self.due_date = datetime.strptime(due_date, '%Y-%m-%d') if due_date else None
        self.priority = prioirty # Low , Medium , High
        self.category = category 
        self.completed = False

    def mark_complete(self):
        '''Mark the tesk complete'''
        self.completed = True
        print(f"Task '{self.description}' marked as complete. ")
    
    def __str__(self):
        '''Return a string representaion of the task.'''
        status = 'Completed' if self.completed else  "Not completed"
        due = self.due_date.strftime('%Y-%m-%d') if self.due_date else 'No due Date'
        return f"{self.description} | Due : {due} | Priorities : {self.priority} | Categories : {self.category} | Status : {self.category} | Status : {status}"

class TaskManager:
    def __init__(self):
        '''Initialize the task manager with an empty list of tasks.'''
        self.tasks = []

    def add_task(self, description, due_date = None, priority = 'Medium', category = 'General'):
        '''Add a new task to the task list. '''
        new_task = Task(description, due_date, priority, category)
        self.tasks.append(new_task)
        print(f"Task '{description}' added to the task list.")
    
    def remove_task (self, description):
        '''Remove a task by description if it exists.'''
        for task in self.tasks:
            if task.description == description:
                self.tasks.remove(task)
                print(f"Task '{description}' remove from the tasks list.")
                return True
            print("f Task '{description}' not found. ")
            return False
    

    def mark_task_complete(self, description):
        '''Mark a specific task as completed by its description.'''

        for task in self.tasks:
            if task.description == description:
                task.mark_complete()
                return True
            print(f"Task '{description}' not found.")
            return False 
        
    def list_tasks(self, category = None, sort_by = 'due_date'):
        '''List all tasks, optionally filterred by category and sorted by due date or priority.'''
        tasks_to_display = [task for task in self.tasks if (category is None or task.category == category)]
        
        if sort_by == 'due_date':
            tasks_to_display.sort(key  = lambda task: (task.due_date is not None, task.due_date))
        elif sort_by == 'priority':
            priority_order = {'High': 1, 'Medium': 2, 'Low': 3}
            tasks_to_display.sort(key= lambda task: priority_order.get(task.priority, 3))

        print("Task: ")
        for task in tasks_to_display:
            print(task)



if __name__ == "__main__":
    
    manager = TaskManager()

    ## Adding tasks 
    manager.add_task("Project 1", '2024-11-01', priority="High", category='Work')
    manager.add_task("Project 2", '2024-11-04', priority="Medium", category='Personal')
    manager.add_task("Project 3", '2024-11-03', priority="High", category='Work')
    manager.add_task("Project 4", '2024-11-05', priority="Low", category='Health')
    manager.add_task("Project 5", '2024-11-03', priority="High", category='Health')


    manager.mark_task_complete('Project 2')
    manager.remove_task('Project 3')


    print("\nAll tasks sorted by due date: ")
    manager.list_tasks(sort_by='due_date')

    print('\nHealth tasks sorted by priorities: ')
    manager.list_tasks(category="Health", sort_by='priorities')
