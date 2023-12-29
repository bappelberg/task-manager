from typing import List

from task import Task


class TaskRepository:
    def __init__(self):
        self.tasks: List[Task] = []
        self.file_path = 'tasks.txt'
        self.next_task_id = 1
        # Load tasks from the file on initialization
        self.load_from_file(self.file_path)

    def add_task(self, task: Task) -> None:
        task.set_task_id(self.next_task_id)
        self.next_task_id += 1
        self.tasks.append(task)
        # Save the new task to the file immediately
        with open(self.file_path, 'a') as file:
            file.write(f"{task.get_task_id()},{task.title},{task.description},{task.story_points},{task.is_done}\n")

    def save_to_file(self, file_path: str) -> None:
        with open(self.file_path, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.get_task_id()},{task.title},{task.description},{task.story_points},{task.is_done}\n")

    def load_from_file(self, file_path: str) -> None:
        try:
            # Clear existing tasks before loading from the file
            self.tasks.clear()
            with open(file_path, 'r') as file:
                for line in file:
                    # Parse each line and create a Task object
                    task_id, title, description, story_points, is_done = map(str.strip, line.split(','))
                    task = Task(title, description, int(story_points))
                    task.set_task_id(int(task_id))
                    task.is_done = is_done.lower() == 'true'
                    self.tasks.append(task)

        except FileNotFoundError:
            print('File not found. No tasks loaded.')

        except Exception as e:
            print(f"Error loading tasks from file: {e}")

    def update_task(self, task_id: int, new_title: str, new_description: str, new_story_points: int,
                    new_is_done: bool) -> None:
        task = self.get_task_by_id(task_id)

        task.title = new_title
        task.description = new_description
        task.story_points = new_story_points
        task.is_done = new_is_done
        self.save_to_file(self.file_path)

    def delete_task(self, task_id: int) -> None:
        try:
            task = self.get_task_by_id(task_id)
            self.tasks.remove(task)

            self.save_to_file(self.file_path)
            print(f"Task {task_id} deleted successfully.")
        except ValueError as e:
            print(e)

    def get_all_tasks(self) -> List[Task]:
        self.load_from_file(self.file_path)
        return self.tasks

    def get_task_by_id(self, task_id: int) -> Task:
        for task in self.tasks:
            if task.get_task_id() == task_id:
                return task
        raise ValueError(f"Task with ID {task_id} not found")

    def __str__(self) -> str:
        return "\n".join(str(task) for task in self.tasks)
