from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List, Dict

@dataclass
class Task:
    description: str
    time: int  # Duration in minutes
    frequency: str  # "Daily", "Weekly", or "One-time"
    start_time: str = "08:00"  # Format: "HH:MM"
    is_completed: bool = False
    priority: str = "Medium"  # "High", "Medium", "Low"
    due_date: date = field(default_factory=date.today)

    def mark_complete(self, pet=None) -> None:
        """Marks the task complete and creates the next instance if recurring."""
        if self.is_completed:
            return  # Already completed
            
        self.is_completed = True
        
        # Automate next recurrence if connected to a pet profile
        if pet and self.frequency in ["Daily", "Weekly"]:
            days_to_add = 1 if self.frequency == "Daily" else 7
            next_due_date = self.due_date + timedelta(days=days_to_add)
            
            # Spawn a fresh instance scheduled for the future occurrence date
            next_task = Task(
                description=self.description,
                time=self.time,
                frequency=self.frequency,
                start_time=self.start_time,
                priority=self.priority,
                due_date=next_due_date,
                is_completed=False
            )
            pet.add_task(next_task)

    def to_dict(self) -> Dict:
        """Converts the task attributes into a dictionary for UI rendering."""
        return {
            "description": self.description,
            "time": self.time,
            "frequency": self.frequency,
            "start_time": self.start_time,
            "is_completed": self.is_completed,
            "priority": self.priority,
            "due_date": self.due_date.strftime("%Y-%m-%d")
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
        """Retrieves a flat list of all tasks across all pets with object references."""
        all_tasks = []
        for pet in self.pets:
            for task in pet.tasks:
                task_data = task.to_dict()
                task_data["pet_name"] = pet.name
                task_data["pet_obj"] = pet        # Reference to pet for automation hooks
                task_data["task_obj"] = task
                all_tasks.append(task_data)
        return all_tasks


class Scheduler:
    def __init__(self):
        self.allocated_time: int = 0
        self.reasoning_log: List[str] = []

    def sort_by_time(self, tasks: List[Dict]) -> List[Dict]:
        """Sorts a list of task dictionaries chronologically by start time string."""
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
        """Generates an ordered dynamic plan filtering out already completed tasks."""
        self.allocated_time = 0
        self.reasoning_log = []
        
        raw_tasks = owner.get_all_tasks_across_pets()
        
        # Only process tasks due today or earlier that aren't finished yet
        today_str = date.today().strftime("%Y-%m-%d")
        active_tasks = [t for t in raw_tasks if not t["is_completed"] and t["due_date"] <= today_str]
        
        sorted_tasks = self.sort_by_time(active_tasks)
        scheduled_plan = []
        remaining_time = available_time_budget
        
        for item in sorted_tasks:
            task_obj = item["task_obj"]
            pet_obj = item["pet_obj"]
            if item["time"] <= remaining_time:
                # Wire task completion to trigger the next recurrence automatically
                task_obj.mark_complete(pet=pet_obj)
                
                remaining_time -= item["time"]
                self.allocated_time += item["time"]
                scheduled_plan.append({
                    "pet_name": item["pet_name"],
                    "description": item["description"],
                    "time": item["time"],
                    "start_time": item["start_time"],
                    "priority": item["priority"],
                    "due_date": item["due_date"]
                })
                self.reasoning_log.append(
                    f"Scheduled & Automated recurrence for '{item['description']}' at {item['start_time']}."
                )
            else:
                self.reasoning_log.append(
                    f"Skipped '{item['description']}' — Exceeds remaining budget."
                )
                
        return scheduled_plan

    def get_reasoning_summary(self) -> str:
        """Returns a natural language breakdown of schedule decisions."""
        if not self.reasoning_log:
            return "No plan has been generated yet."
        return "Daily Schedule Reasoning:\n" + "\n".join([f"- {log}" for log in self.reasoning_log])
