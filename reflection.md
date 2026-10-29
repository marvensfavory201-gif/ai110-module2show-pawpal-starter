# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Description:  My initial UML design focused on separating data storage from scheduling logic to keep the application organized and modular. I broke the core functionality down into three principal classes.
-  Classes and Responsibilities:
  - `Pet`: Holds the basic state and metadata of the pet (name, breed, age) as well as owner constraints like total available care time for the day.
  - `Task`: Models an individual care activity. It tracks attributes such as task name, duration (in minutes), priority level (high, medium, low), and scheduling status.
  - `Scheduler`: Contains the algorithmic processing logic. Its sole responsibility is to take a collection of `Task` objects, apply filtering rules based on time limits, sort them by priority, and compile the final day's plan.

**b. Design changes**

-  I updated the `Scheduler` class to  link with a `Pet` instance, and introduced an internal priority-weight mapping dictionary for tasks.
-  Originally, the `Scheduler` existed as a disconnected utility class. By linking the scheduler directly to a pet profile, it can pull the owner's available care time constraint for that day. 

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

-  The scheduler considers the daily total available time budget and the categorical priority level assigned to each task.
- The system maps categorical priority levels directly to numerical weights. High-priority items like medication or feeding are given absolute weight precedence. If tasks share an identical priority rank, the tie-breaker rule arranges them by shorter durations first to  squeeze maximum care coverage out of a tight time window.

**b. Tradeoffs**

- The algorithm uses a greedy approach, packing tasks completely in descending priority order. It does not try to calculate complex permutations to maximize exact minute density.
-  For a pet parent, a medical task or feeding must  happen over an optional task like grooming, even if skipping a long grooming session leaves some minutes on the clock unallocated.

---

## 3. AI Collaboration

**a. How you used AI**

-  I used AI to turn my initial ideas into Python code stubs, build the core scheduling loop, and fix my Git terminal push errors.
-  Prompts asking about how classes connect were the most useful, like: *"How should the Scheduler retrieve all tasks from the Owner's pets?"*

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
 The AI initially suggested a loose, standalone scheduling algorithm that did not match how the structural data classes were set up.

- How did you evaluate or verify what the AI suggested?
I did not accept that setup. I instead verified the classes and built a custom method inside the `Owner` class (`get_all_tasks_across_pets`) so the scheduler could pull data correctly across multiple pets.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
