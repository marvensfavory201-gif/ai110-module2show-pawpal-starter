from pawpal_system import Owner, Pet, Task, Scheduler

def main():
    owner = Owner(name="Alex", email="alex@example.com")
    biscuit = Pet(name="Biscuit", breed="Golden Retriever", age=3)
    cleo = Pet(name="Cleo", breed="Siamese Cat", age=5)
    owner.add_pet(biscuit)
    owner.add_pet(cleo)

    # 1. Add tasks explicitly OUT OF ORDER chronologically
    biscuit.add_task(Task(description="Night Walk", time=20, frequency="Daily", start_time="20:00"))
    biscuit.add_task(Task(description="Morning Meds", time=10, frequency="Daily", start_time="07:30"))
    cleo.add_task(Task(description="Afternoon Grooming", time=30, frequency="Weekly", start_time="14:15"))
    cleo.add_task(Task(description="Midday Feeding", time=15, frequency="Daily", start_time="12:00"))

    scheduler = Scheduler()
    all_tasks = owner.get_all_tasks_across_pets()

    print("=" * 60)
    print("🔍 VERIFYING CHRONOLOGICAL HH:MM SORTING METHOD")
    print("=" * 60)
    sorted_res = scheduler.sort_by_time(all_tasks)
    for t in sorted_res:
        print(f"⏰ [{t['start_time']}] - {t['pet_name']}: {t['description']}")

    print("\n" + "=" * 60)
    print("🔍 VERIFYING SPECIFIC PET FILTER METHOD (Cleo Only)")
    print("=" * 60)
    cleo_only = scheduler.filter_tasks(all_tasks, pet_name="Cleo")
    for t in cleo_only:
        print(f"🐱 Filtered Item -> {t['pet_name']}: {t['description']}")

if __name__ == "__main__":
    main()
