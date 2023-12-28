class Task:
	def __init__(self, title: str, description: str, story_points: int):
		self.title = title
		self.description = description
		self.story_points = story_points
		self.is_done = False
		self.task_id = None

	def get_task_id(self) -> int:
		return self.task_id

	def set_task_id(self, task_id: int) -> None:
		self.task_id = task_id

	def toggle_done(self) -> None:
		self.is_done = not self.is_done

	def __str__(self) -> str:
		return (f"ID: {self.task_id}, "
		        f"Title: {self.title}, "
		        f"Description: {self.description}, "
		        f"Story points: {self.story_points}, "
		        f"Is done: {self.is_done}"
		        )
