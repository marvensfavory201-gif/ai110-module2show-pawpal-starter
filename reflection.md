# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Description:  My initial UML design focused on separating data storage from scheduling logic to keep the application organized and modular. I broke the core functionality down into three principal classes.
-  Classes and Responsibilities:
  - `Pet`: Holds the basic state and metadata of the pet (name, breed, age) as well as owner constraints like total available care time for the day.
  - `Task`: Models an individual care activity. It tracks attributes such as task name, duration (in minutes), priority level (high, medium, low), and scheduling status.
  - `Scheduler`: Contains the algorithmic processing logic. Its sole responsibility is to take a collection of `Task` objects, apply filtering rules based on time limits, sort them by priority, and compile the final day's plan.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

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
