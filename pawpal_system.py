from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Task:
    name: str
    duration: int
    priority: str  # "High", "Medium", or "Low"
    is_scheduled: bool = False

    def to_dict(self) -> Dict:
        """Converts the task attributes into a dictionary for UI rendering."""
        return {
            "name": self.name,
            "duration": self.duration,
            "priority": self.priority,
            "is_scheduled": self.is_scheduled
        }


@dataclass
class Pet:
    name: str
    breed: str
    age: int
    available_time: int  # Total minutes the owner has available today

    def get_profile_summary(self) -> str:
        """Returns a formatted summary string of the pet's profile."""
        return f"{self.name} ({self.breed}, Age: {self.age}) - Available Time: {self.available_time} mins"


class Scheduler:
    def __init__(self, pet: Pet):
        self.pet: Pet = pet
        self.tasks: List[Task] = []
        self.allocated_time: int = 0
        self.reasoning_log: List[str] = []

    def add_task(self, task: Task) -> None:
        """Adds a task to the evaluation pool."""
        self.tasks.append(task)

    def generate_plan(self) -> List[Task]:
        """Sorts, filters, and generates an optimized plan within the pet's available time."""
        # Define priority mapping for explicit sorting weights
        priority_weights = {"High": 3, "Medium": 2, "Low": 1}
        
        # Reset current scheduler metrics
        self.allocated_time = 0
        self.reasoning_log = []
        
        # Sort tasks: highest priority weight first; if tied, shorter tasks first
        sorted_tasks = sorted(
            self.tasks, 
            key=lambda t: (-priority_weights.get(t.priority, 0), t.duration)
        )
        
        scheduled_plan = []
        remaining_time = self.pet.available_time
        
        for task in sorted_tasks:
            if task.duration <= remaining_time:
                task.is_scheduled = True
                remaining_time -= task.duration
                self.allocated_time += task.duration
                scheduled_plan.append(task)
                self.reasoning_log.append(f"Scheduled '{task.name}' ({task.duration} min) due to available time budget.")
            else:
                task.is_scheduled = False
                self.reasoning_log.append(f"Skipped '{task.name}' ({task.duration} min) because it exceeds the remaining {remaining_time} minute budget.")
                
        return scheduled_plan

    def get_reasoning_summary(self) -> str:
        """Returns a natural language breakdown of schedule decisions."""
        if not self.reasoning_log:
            return "No plan has been generated yet."
        summary = f"Schedule Analysis for {self.pet.name}:\n"
        summary += f"- Total allocated time: {self.allocated_time}/{self.pet.available_time} minutes.\n"
        summary += "\nLogs:\n" + "\n".join([f"  * {log}" for log in self.reasoning_log])
        return summary


class Owner:
    def __init__(self, name: str, email: str):
        self.name: str = name
        self.email: str = email
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Associates a new pet profile with this owner."""
        self.pets.append(pet)

    def get_all_plans(self) -> str:
        """Retrieves formatted schedules across all owned pets."""
        return f"Owner Profile: {self.name} tracks care for {len(self.pets)} pet(s)."
