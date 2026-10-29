from pawpal_system import Owner, Pet, Task, Scheduler

def main():
    owner = Owner(name="Alex", email="alex@example.com")
    biscuit = Pet(name="Biscuit", breed="Golden Retriever", age=3)
    cleo = Pet(name="Cleo", breed="Siamese Cat", age=5)
    owner.add_pet(biscuit)
    owner.add_pet(cleo)

    # 1. Add two completely different tasks at the exact same start time
    biscuit.add_task(Task(description="Morning Insulin Dose", time=10, frequency="Daily", start_time="08:00", priority="High"))
    cleo.add_task(Task(description="Morning Feeding Meal", time=15, frequency="Daily", start_time="08:00", priority="High"))
    biscuit.add_task(Task(description="Afternoon Walk", time=30, frequency="Daily", start_time="15:30", priority="Medium"))

    scheduler = Scheduler()
    
    print("=" * 60)
    print("🚀 GENERATING DAILY PLAN WITH EXPECTED OVERLAP CONFLICTS")
    print("=" * 60)
    
    # Run scheduling generation
    plan = scheduler.generate_daily_plan(owner, available_time_budget=120)
    
    for t in plan:
        print(f"🐾 [{t['start_time']}] {t['pet_name']}: {t['description']}")
        
    print("\n" + "=" * 60)
    print("🧠 REVIEWING SCHEDULER LOG OUTPUT & OVERLAP SAFETY WARNINGS")
    print("=" * 60)
    print(scheduler.get_reasoning_summary())

if __name__ == "__main__":
    main()
