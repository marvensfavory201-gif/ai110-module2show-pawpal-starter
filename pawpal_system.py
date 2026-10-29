from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Task:
    description: str
    time: int  # Duration in minutes
    frequency: str  # e.g., "Daily", "Weekly"
    is_completed: bool = False
    priority: str = "Medium"  # "High", "Medium", "Low"

    def to_dict(self) -> Dict:
        """Converts the task attributes into a dictionary for UI rendering."""
        return {
            "description": self.description,
            "time": self.time,
            "frequency": self.frequency,
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
        """
        Retrieves a flat list of all tasks across all pets.
        Includes a back-reference to which pet owns each task.
        """
        all_tasks = []
        for pet in self.pets:
            for task in pet.tasks:
                task_data = task.to_dict()
                task_data["pet_name"] = pet.name  # Link task to the pet context
                task_data["task_obj"] = task       # Keep object reference for scheduling updates
                all_tasks.append(task_data)
        return all_tasks


class Scheduler:
    def __init__(self):
        self.allocated_time: int = 0
        self.reasoning_log: List[str] = []

    def generate_daily_plan(self, owner: Owner, available_time_budget: int) -> List[Dict]:
        """
        The 'Brain' of the system.
        Retrieves all tasks from the Owner's pets, sorts them by priority level,
        and packs them into the day's time budget.
        """
        priority_weights = {"High": 3, "Medium": 2, "Low": 1}
        self.allocated_time = 0
        self.reasoning_log = []
        
        # 1. Retrieve all tasks across pets using the Owner's access method
        raw_tasks = owner.get_all_tasks_across_pets()
        
        # 2. Organize: Sort by priority weight (highest first), then by duration (shorter first)
        sorted_tasks = sorted(
            raw_tasks,
            key=lambda t: (-priority_weights.get(t["priority"], 2), t["time"])
        )
        
        scheduled_plan = []
        remaining_time = available_time_budget
        
        # 3. Schedule within constraints
        for item in sorted_tasks:
            task_obj = item["task_obj"]
            if item["time"] <= remaining_time:
                task_obj.is_completed = True  # Mark as scheduled/completed for the day
                remaining_time -= item["time"]
                self.allocated_time += item["time"]
                
                # Add to final plan view
                scheduled_plan.append({
                    "pet_name": item["pet_name"],
                    "description": item["description"],
                    "time": item["time"],
                    "priority": item["priority"]
                })
                self.reasoning_log.append(
                    f"Scheduled '{item['description']}' for {item['pet_name']} ({item['time']} min) [Priority: {item['priority']}]"
                )
            else:
                task_obj.is_completed = False
                self.reasoning_log.append(
                    f"Skipped '{item['description']}' for {item['pet_name']} ({item['time']} min) — Exceeds remaining budget of {remaining_time} min."
                )
                
        return scheduled_plan

    def get_reasoning_summary(self) -> str:
        """Returns a natural language breakdown of schedule decisions."""
        if not self.reasoning_log:
            return "No plan has been generated yet."
        return "Daily Schedule Reasoning:\n" + "\n".join([f"- {log}" for log in self.reasoning_log])
