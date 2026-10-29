from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Task:
    description: str
    time: int  # Duration in minutes
    frequency: str  # e.g., "Daily", "Weekly"
    start_time: str = "08:00"  # Format: "HH:MM" (e.g., "09:30", "14:00")
    is_completed: bool = False
    priority: str = "Medium"  # "High", "Medium", "Low"

    def mark_complete(self) -> None:
        """Changes the task completion status to True."""
        self.is_completed = True

    def to_dict(self) -> Dict:
        """Converts the task attributes into a dictionary for UI rendering."""
        return {
            "description": self.description,
            "time": self.time,
            "frequency": self.frequency,
            "start_time": self.start_time,
            "is_completed": self.is_completed,
            "priority": self.priority
        }


@dataclass
class Pet:
    name: str
    breed: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Adds a care task directly to this pet's profile."""
        self.tasks.append(task)


class Owner:
    def __init__(self, name: str, email: str):
        self.name: str = name
        self.email: str = email
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Associates a new pet profile with this owner."""
        self.pets.append(pet)

    def get_all_tasks_across_pets(self) -> List[Dict]:
        """Retrieves a flat list of all tasks across all pets with back-references."""
        all_tasks = []
        for pet in self.pets:
            for task in pet.tasks:
                task_data = task.to_dict()
                task_data["pet_name"] = pet.name
                task_data["task_obj"] = task
                all_tasks.append(task_data)
        return all_tasks


class Scheduler:
    def __init__(self):
        self.allocated_time: int = 0
        self.reasoning_log: List[str] = []

    def sort_by_time(self, tasks: List[Dict]) -> List[Dict]:
        """Sorts a list of task dictionaries chronologically by their HH:MM start time string."""
        return sorted(tasks, key=lambda t: t["start_time"])

    def filter_tasks(self, tasks: List[Dict], exclude_completed: bool = False, pet_name: str = None) -> List[Dict]:
        """Filters tasks by completion status or specific pet name attributes."""
        filtered = tasks
        if exclude_completed:
            filtered = [t for t in filtered if not t["is_completed"]]
        if pet_name:
            filtered = [t for t in filtered if t["pet_name"].lower() == pet_name.lower()]
        return filtered

    def generate_daily_plan(self, owner: Owner, available_time_budget: int) -> List[Dict]:
        """Retrieves, sorts chronologically, filters out completed tasks, and fits into budget."""
        self.allocated_time = 0
        self.reasoning_log = []
        
        # 1. Fetch raw list
        raw_tasks = owner.get_all_tasks_across_pets()
        
        # 2. Filter out already completed tasks so they don't block fresh time budgets
        active_tasks = self.filter_tasks(raw_tasks, exclude_completed=True)
        
        # 3. Sort Chronologically by string time using our updated method
        sorted_tasks = self.sort_by_time(active_tasks)
        
        scheduled_plan = []
        remaining_time = available_time_budget
        
        # 4. Fit into time constraint
        for item in sorted_tasks:
            task_obj = item["task_obj"]
            if item["time"] <= remaining_time:
                remaining_time -= item["time"]
                self.allocated_time += item["time"]
                scheduled_plan.append({
                    "pet_name": item["pet_name"],
                    "description": item["description"],
                    "time": item["time"],
                    "start_time": item["start_time"],
                    "priority": item["priority"]
                })
                self.reasoning_log.append(
                    f"Scheduled '{item['description']}' at {item['start_time']} ({item['time']} min)"
                )
            else:
                self.reasoning_log.append(
                    f"Skipped '{item['description']}' at {item['start_time']} — Exceeds remaining budget."
                )
                
        return scheduled_plan

    def get_reasoning_summary(self) -> str:
        """Returns a natural language breakdown of schedule decisions."""
        if not self.reasoning_log:
            return "No plan has been generated yet."
        return "Daily Schedule Reasoning:\n" + "\n".join([f"- {log}" for log in self.reasoning_log])
