import pytest
from pawpal_system import Owner, Pet, Task, Scheduler

def test_task_completion():
    """Verify that calling mark_complete() actually changes the task's status."""
    # Arrange
    task = Task(description="Evening Walk", time=20, frequency="Daily", priority="Medium")
    assert task.is_completed is False

    # Act
    task.mark_complete()

    # Assert
    assert task.is_completed is True


def test_task_addition():
    """Verify that adding a task to a Pet increases that pet's task count."""
    # Arrange
    pet = Pet(name="Biscuit", breed="Golden Retriever", age=3)
    assert len(pet.tasks) == 0

    # Act
    task1 = Task(description="Feeding", time=10, frequency="Daily", priority="High")
    pet.add_task(task1)

    # Assert
    assert len(pet.tasks) == 1
    assert pet.tasks[0].description == "Feeding"
