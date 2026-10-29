import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+ Care Planner", page_icon="🐾", layout="wide")

st.title("🐾 PawPal+ Care Task Planner")
st.subheader("Plan smart, recurring care routines across all your pets.")

if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Pet Parent", email="parent@example.com")
if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler()

owner = st.session_state.owner
scheduler = st.session_state.scheduler

col1, col2 = st.columns(2)

with col1:
    st.header("🗂️ Profiles & Management")
    
    with st.expander("➕ Add New Pet Profile", expanded=len(owner.pets) == 0):
        with st.form("pet_form", clear_on_submit=True):
            p_name = st.text_input("Pet Name", placeholder="Biscuit")
            p_breed = st.text_input("Breed", placeholder="Golden Retriever")
            p_age = st.number_input("Age", min_value=0, max_value=30, value=2)
            submit_pet = st.form_submit_button("Save Pet Profile")
            
            if submit_pet and p_name:
                new_pet = Pet(name=p_name, breed=p_breed, age=p_age)
                owner.add_pet(new_pet)
                st.success(f"Added profile for {p_name}!")
                st.rerun()

    if owner.pets:
        with st.expander("📋 Add Care Task", expanded=True):
            with st.form("task_form", clear_on_submit=True):
                target_pet_name = st.selectbox("Assign to Pet", [p.name for p in owner.pets])
                t_desc = st.text_input("Task Description", placeholder="Morning Feeding")
                t_time = st.number_input("Duration (Minutes)", min_value=5, max_value=240, value=20, step=5)
                t_start = st.text_input("Preferred Start Time (HH:MM)", value="08:00")
                t_freq = st.selectbox("Frequency Pattern", ["One-time", "Daily", "Weekly"])
                t_priority = st.selectbox("Priority Level", ["High", "Medium", "Low"])
                submit_task = st.form_submit_button("Add Task")
                
                if submit_task and t_desc:
                    target_pet = next(p for p in owner.pets if p.name == target_pet_name)
                    new_task = Task(description=t_desc, time=t_time, frequency=t_freq, start_time=t_start, priority=t_priority)
                    target_pet.add_task(new_task)
                    st.success(f"Added {t_freq} task '{t_desc}' to {target_pet_name}!")
                    st.rerun()
                    
        st.write("### Active Care Schedules:")
        for pet in owner.pets:
            with st.container():
                st.markdown(f"#### 🐕 {pet.name}'s Tracked Tasks")
                for t in pet.tasks:
                    status = "✅ Completed/Scheduled" if t.is_completed else "⏳ Pending"
                    st.caption(f"- **{t.description}** ({t.time} min) | Cadence: `{t.frequency}` | Due: `{t.due_date}` | Status: *{status}*")
    else:
        st.warning("Please add at least one pet profile to unlock task entry fields.")

with col2:
    st.header("🗓️ Daily Scheduler Pipeline")
    
    if owner.pets:
        time_budget = st.slider("Total Available Time Budget Today (Minutes)", min_value=15, max_value=480, value=90, step=15)
        
        if st.button("🚀 Generate & Automate Recurrences", type="primary"):
            daily_plan = scheduler.generate_daily_plan(owner, available_time_budget=time_budget)
            
            st.write("### 📅 Today's Active Schedule")
            if not daily_plan:
                st.warning("No tasks fit within your active time budget today.")
            else:
                for idx, task in enumerate(daily_plan):
                    st.markdown(f"#### `{idx + 1}` **[{task['pet_name']}]** {task['description']} at {task['start_time']}")
                    st.text(f"⏱️ Duration: {task['time']} mins | Date Logged: {task['due_date']} | Priority: {task['priority']}")
                    st.divider()
            
            st.write("### 🧠 Logic Engine & Schedule Reasoning")
            st.code(scheduler.get_reasoning_summary(), language="text")
            
            # Simple button to refresh state views after task instantiation
            if st.button("🔄 Sync & View Future Occurrences"):
                st.rerun()
    else:
        st.info("Configure your profiles on the left to activate the automated pipeline.")
