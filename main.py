from pawpal_system import Owner, Pet, Task, Scheduler

def main():
    # 1. Create an Owner
    owner = Owner(name="Alex", email="alex@example.com")

    # 2. Create at least two Pets
    biscuit = Pet(name="Biscuit", breed="Golden Retriever", age=3)
    cleo = Pet(name="Cleo", breed="Siamese Cat", age=5)

    owner.add_pet(biscuit)
    owner.add_pet(cleo)

    # 3. Add at least three Tasks with different times and priorities
    # High Priority task (Should schedule first)
    biscuit.add_task(Task(description="Morning Insulin Medication", time=10, frequency="Daily", priority="High"))
    
    # Medium Priority task
    biscuit.add_task(Task(description="Long Park Walk", time=45, frequency="Daily", priority="Medium"))
    
    # Low Priority task (May get skipped if time runs out)
    cleo.add_task(Task(description="Full Grooming & Brushing", time=30, frequency="Weekly", priority="Low"))
    
    # Another High Priority task
    cleo.add_task(Task(description="Morning Feeding", time=15, frequency="Daily", priority="High"))

    # 4. Instantiate the Scheduler and run with a 75-minute total time budget
    scheduler = Scheduler()
    time_budget = 75
    
    plan = scheduler.generate_daily_plan(owner, available_time_budget=time_budget)

    # 5. Clear, readable output formatting for the terminal
    print("=" * 60)
    print(f"📅 TODAY'S GENERATED CARE SCHEDULE (Budget: {time_budget} mins)")
    print("=" * 60)
    
    if not plan:
        print("No tasks could be scheduled today.")
    else:
        for item in plan:
            print(f"🐾 [{item['pet_name']}] {item['description']}")
            print(f"   ⏱️  Duration: {item['time']} mins | ⭐ Priority: {item['priority']}")
            print("-" * 60)
            
    print("\n" + "=" * 60)
    print("🧠 SCHEDULER LOGS & DECISION REASONING")
    print("=" * 60)
    print(scheduler.get_reasoning_summary())
    print("=" * 60)

if __name__ == "__main__":
    main()
