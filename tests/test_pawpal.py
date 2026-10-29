import pytest
from datetime import date, timedelta
from pawpal_system import Owner, Pet, Task, Scheduler

def test_sorting_correctness():
    """Verify that tasks are accurately arranged in chronological order by their HH:MM string."""
    scheduler = Scheduler()
    
    # Define tasks completely out of order
    tasks = [
        {"description": "Night Walk", "start_time": "21:00"},
        {"description": "Morning Feeding", "start_time": "07:30"},
        {"description": "Midday Playtime", "start_time": "12:15"}
    ]
    
    # Sort using our algorithm
    sorted_tasks = scheduler.sort_by_time(tasks)
    
    # Assert they follow morning-to-night chronological alignment
    assert sorted_tasks[0]["start_time"] == "07:30"
    assert sorted_tasks[1]["start_time"] == "12:15"
    assert sorted_tasks[2]["start_time"] == "21:00"


def test_recurrence_logic():
    """Confirm that marking a daily task complete creates a new pending task for the following day."""
    pet = Pet(name="Biscuit", breed="Golden Retriever", age=3)
    today_date = date.today()
    
    # Create a Daily task instance
    task = Task(description="Insulin Medication", time=10, frequency="Daily", due_date=today_date)
    pet.add_task(task)
    
    # Complete the task attached to the pet context
    task.mark_complete(pet=pet)
    
    # Assertions: original task is completed, and a brand new task is spawned for tomorrow
    assert task.is_completed is True
    assert len(pet.tasks) == 2
    
    new_task = pet.tasks[1]
    assert new_task.description == "Insulin Medication"
    assert new_task.is_completed is False
    assert new_task.due_date == today_date + timedelta(days=1)


def test_conflict_detection():
    """Verify that the Scheduler successfully catches and flags duplicate start times across tasks."""
    scheduler = Scheduler()
    
    # Simulate a schedule where two pets are booked at the exact same hour block
    scheduled_plan = [
        {"pet_name": "Biscuit", "description": "Feeding", "start_time": "08:00"},
        {"pet_name": "Cleo", "description": "Meds", "start_time": "08:00"}
    ]
    
    # Run conflict evaluation
    scheduler.detect_conflicts(scheduled_plan)
    
    # Assert a non-crashing warning string was safely populated in our logs
    assert len(scheduler.conflicts) == 1
    assert "TIME OVERLAP DETECTED AT 08:00" in scheduler.conflicts[0]
