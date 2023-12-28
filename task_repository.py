from typing import List

from task import Task


class TaskRepository:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        task_id = len(self.tasks) + 1
        task.set_task_id(task_id)
        self.tasks.append(task)

    def update_task(self, task_id: int, new_title: str, new_description: str, new_story_points: int, new_is_done: bool) -> None:
        task = self.get_task_by_id(task_id)

        task.title = new_title
        task.description = new_description
        task.story_points = new_story_points
        task.is_done = new_is_done

    def delete_task(self, task_id: int) -> None:
        task = self.get_task_by_id(task_id)
        self.tasks.remove(task)

    def get_all_tasks(self) -> List[Task]:
        return self.tasks

    def get_task_by_id(self, task_id: int) -> Task:
        for task in self.tasks:
            if task.get_task_id() == task_id:
                return task
        raise ValueError(f"Task with ID {task_id} not found")

    def toggle_done(self, task_id: int) -> None:
        task = self.get_task_by_id(task_id)
        task.toggle_done()

    def __str__(self) -> str:
        return "\n".join(str(task) for task in self.tasks)

