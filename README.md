# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

```text
============================================================
📅 TODAY'S GENERATED CARE SCHEDULE (Budget: 75 mins)
============================================================
🐾 [Biscuit] Morning Insulin Medication
   ⏱️  Duration: 10 mins | ⭐ Priority: High
------------------------------------------------------------
🐾 [Cleo] Morning Feeding
   ⏱️  Duration: 15 mins | ⭐ Priority: High
------------------------------------------------------------
🐾 [Biscuit] Long Park Walk
   ⏱️  Duration: 45 mins | ⭐ Priority: Medium
------------------------------------------------------------

============================================================
🧠 SCHEDULER LOGS & DECISION REASONING
============================================================
Daily Schedule Reasoning:
- Scheduled 'Morning Insulin Medication' for Biscuit (10 min) [Priority: High]
- Scheduled 'Morning Feeding' for Cleo (15 min) [Priority: High]
- Scheduled 'Long Park Walk' for Biscuit (45 min) [Priority: Medium]
- Skipped 'Full Grooming & Brushing' for Cleo (30 min) — Exceeds remaining budget of 5 min.
============================================================
```

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```

## 🧪 Testing PawPal+

To verify that the calendar rules, timeline ordering, and warning pipelines function correctly without structural failure, run the automated test suite with the following terminal command:

```bash
# Run the full test suite:
python -m pytest

# Run with coverage:
- **`test_sorting_correctness`:** Assures that out-of-order task lists are successfully organized chronologically by their `"HH:MM"` text stamps.
- **`test_recurrence_logic`:** Confirms that checking off daily items automatically updates calendars for the following day using `timedelta` adjustments.
- **`test_conflict_detection`:** Verifies that overlapping task milestones generate explicit safety alerts without crashing execution modules.

```

Sample test output:
============================= test session starts =============================
platform win32 -- Python 3.11.5, pytest-7.4.0, pluggy-1.2.0
rootdir: C:\Users\Student\Projects\ai110-module2show-pawpal-starter
collected 3 items

tests/test_pawpal.py ...                                                 [100%]

============================== 3 passed in 0.08s ==============================
```
```
# Paste your pytest output here
```
⭐ ⭐ ⭐ ⭐ ⭐ (5/5 Stars)  
The suite aggressively isolates individual behavior methods, confirming that date transitions, calendar sort structures, and time-block overlap constraints operate correctly under both optimal and conflicting real-world scenarios.

##   📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` | Organizes all active, pending care activities chronologically using string `"HH:MM"` sorting. |
| Filtering | `Scheduler.filter_tasks()` | Allows isolation of workflows by pet name parameters and automatically filters out pre-completed tasks. |
| Conflict handling | `Scheduler.detect_conflicts()` | Scans scheduled blocks and logs safe, non-crashing warnings if tasks share an identical starting slot. |
| Recurring tasks | `Task.mark_complete()` | Employs Python `timedelta` offsets to auto-schedule the next occurrence date for continuous daily/weekly patterns. |


## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:
PawPal+ functions as an intelligent daily care assistant. Below is a detailed text walkthrough of the application's user interface features, algorithmic workflows, and scheduling behaviors.

### Main UI Features and User Actions
- **Profile Management Sidebar/Form:** Allows pet owners to create persistent, unique profiles for multiple pets by specifying their name, breed, and age.
- **Dynamic Care Task Creator:** Captures required care operations including custom task description, duration in minutes, preferred start time block (HH:MM style), frequency pattern (One-time, Daily, Weekly), and priority urgency tier.
- **Active Profile Rosters:** Displays a breakdown of how many active care operations are currently configured per registered pet profile.
-* **Daily Scheduler Control Column:** Features an interactive slider to throttle total available time constraints alongside a primary trigger button to run the scheduling engine logic.

---



---



---

### 🖥️ Fenced CLI Sample Output (`main.py`)
Running the terminal script demonstrates how the core algorithmic layers operate seamlessly outside of the graphical interface:

```text
============================================================
🚀 GENERATING DAILY PLAN WITH EXPECTED OVERLAP CONFLICTS
============================================================
🐾 [08:00] Biscuit: Morning Insulin Dose
🐾 [08:00] Cleo: Morning Feeding Meal
🐾 [15:30] Biscuit: Afternoon Walk

============================================================
🧠 REVIEWING SCHEDULER LOG OUTPUT & OVERLAP SAFETY WARNINGS
============================================================
Daily Schedule Reasoning:
- Scheduled 'Morning Insulin Dose' at 08:00.
- Scheduled 'Morning Feeding Meal' at 08:00.
- Scheduled 'Afternoon Walk' at 15:30.

⚠️ SYSTEM INTEGRITY WARNINGS:
- ⚠️ TIME OVERLAP DETECTED AT 08:00: Biscuit's Morning Insulin Dose and Cleo's Morning Feeding Meal are scheduled simultaneously!
============================================================
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
