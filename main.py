from task import Task
from task_repository import TaskRepository


class CommandLineTaskManager:
    def __init__(self):
        self.task_repository = TaskRepository()

    def run(self):
        while True:
            print("\nTask Manager Menu:")
            print("1. List All Tasks")
            print("2. Add Task")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.list_all_tasks()
            elif choice == "2":
                self.add_task()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                print("Exiting Task Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    def list_all_tasks(self):
        tasks = self.task_repository.get_all_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            for task in tasks:
                print(task)

    def add_task(self):
        title = ""
        description = ""
        story_points = 0

        while True:
            try:
                if not title:
                    title = input("Enter task title: ")
                    if not title:
                        raise ValueError("Title cannot be empty")

                if not description:
                    description = input("Enter task description: ")
                    if not description:
                        raise ValueError("Description cannot be empty")

                if not story_points:
                    story_points_str = input("Enter task story points: ")
                    if not story_points_str:
                        raise ValueError("Story points cannot be empty")

                    story_points = int(story_points_str)

                    if story_points < 0:
                        story_points = 0
                        raise ValueError("Story points must be a non-negative integer")

                new_task = Task(title, description, story_points)
                self.task_repository.add_task(new_task)
                print("Task added successfully.")
                break
            except ValueError as e:
                print(e)
                retry = input("Do you want to retry? (Y/n): ")
                if retry.lower() == "y":
                    continue
                else:
                    break

    def update_task(self):
        old = None
        new_is_done = None
        new_title = ""
        new_description = ""
        new_story_points_str = ""
        new_story_points = 0

        while True:
            try:
                task_id_str = ''
                if not task_id_str:
                    task_id_str = input("Enter the ID of the task to update: ")
                    if not task_id_str:
                        raise ValueError("Task ID cannot be empty")
                    if not task_id_str.isnumeric():
                        task_id_str = ""
                        raise ValueError("Task ID must be an integer greater than 0")

                task_id = int(task_id_str)

                old = self.task_repository.get_task_by_id(task_id)

                print(
                    f"Updating Task {task_id}. Current values: {new_title or old.title, new_description or old.description, new_story_points or old.story_points, old.is_done}"
                )
                break
            except ValueError as e:
                print(e)
                retry = input("Do you want to retry? (Y/n): ")
                if retry.lower() == "y":
                    continue
                else:
                    break

        while True:
            if not old:
                break
            try:
                if not new_title:
                    new_title = (
                            input("New Title (Enter to skip): ") or old.title
                    )
                if not new_description:
                    new_description = (
                            input("New Description (Enter to skip): ")
                            or old.description
                    )

                if not new_story_points_str:
                    new_story_points_str = input("New Story Points (Enter to skip): ")
                    if not new_story_points_str:
                        new_story_points = old.story_points
                    else:
                        if not new_story_points_str.isnumeric():
                            new_story_points_str = ""
                            raise ValueError(
                                "Story points must be a non-negative integer"
                            )
                        new_story_points = int(new_story_points_str)
                        if new_story_points < 0:
                            new_story_points_str = ""
                            raise ValueError(
                                "Story points must be a non-negative integer"
                            )
                new_is_done = (
                    True
                    if input(
                        f"Switch Is Done from {old.is_done} to {not old.is_done}  (Y or enter to skip): "
                    ).lower()
                       == 'y'
                    else old.is_done
                )
                self.task_repository.update_task(
                    old.task_id, new_title, new_description, new_story_points, new_is_done
                )
                print(f"Task {old.task_id} updated successfully.")

                break
            except ValueError as e:
                print(e)
                retry = input("Do you want to retry? (Y/n): ")
                if retry.lower() == "y":
                    continue
                else:
                    break

    def delete_task(self):
        task_id = int(input("Enter the ID of the task to delete: "))
        try:
            self.task_repository.delete_task(task_id)
            print(f"Task {task_id} deleted successfully.")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    command_line_app = CommandLineTaskManager()
    command_line_app.run()
