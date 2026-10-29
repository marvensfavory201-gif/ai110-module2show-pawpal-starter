from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Task:
    name: str
    duration: int
    priority: str  # e.g., "High", "Medium", "Low"
    is_scheduled: bool = False

    def to_dict(self) -> Dict:
        """Converts the task attributes into a dictionary for UI rendering."""
        pass


@dataclass
class Pet:
    name: str
    breed: str
    age: int
    available_time: int  # Total minutes the owner has available today

    def get_profile_summary(self) -> str:
        """Returns a formatted summary string of the pet's profile."""
        pass


class Scheduler:
    def __init__(self):
        self.tasks: List[Task] = []
        self.allocated_time: int = 0

    def add_task(self, task: Task) -> None:
        """Adds a task to the evaluation pool."""
        pass

    def generate_plan(self, max_time: int) -> List[Task]:
        """Sorts, filters, and generates a plan within max_time limits."""
        pass

    def get_reasoning_summary(self) -> str:
        """Returns a natural language breakdown of schedule decisions."""
        pass


class Owner:
    def __init__(self, name: str, email: str):
        self.name: str = name
        self.email: str = email
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Associates a new pet profile with this owner."""
        pass

    def get_all_plans(self) -> str:
        """Retrieves formatted schedules across all owned pets."""
        pass
