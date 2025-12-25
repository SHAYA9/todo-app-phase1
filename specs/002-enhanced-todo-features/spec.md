# Feature Specification: In-Memory Python Console Todo Application (Intermediate Level)

**Feature Branch**: `002-enhanced-todo-features`
**Created**: 2025-12-25
**Status**: Draft
**Input**: User description: "Phase: I – In-Memory Python Console Todo Application (Intermediate Level) Objective: Enhance the Phase-1 console Todo app with additional usability and organization features, while keeping all Phase-1 functionality intact. Functional Requirements: 1. Application Startup - Display a repeating main menu on launch - Application exits only when user selects Exit 2. Menu Options 1. Add Task 2. View Tasks 3. Update Task 4. Delete Task 5. Mark Task as Complete 6. Search / Filter Tasks 7. Sort Tasks 8. Exit 3. Add Task - Prompt user for task title - Title must be non-empty - Assign unique incremental integer ID starting from 1 - Task is incomplete by default - Store task in memory - Prompt user for optional: - Priority: High / Medium / Low - Tags/Categories: e.g., Work, Home, Personal - Validation: only allowed values 4. View Tasks - If no tasks exist, show empty message - Display each task with: - ID - Title - Completion status (Completed / Incomplete) - Priority - Tags/Categories 5. Update Task - Prompt for task ID - If ID not found, show error - Prompt for new title, priority, and tags - Update task data - ID must remain unchanged 6. Delete Task - Prompt for task ID - If ID not found, show error - Remove task from memory 7. Mark Task as Complete - Prompt for task ID - If ID not found, show error - Toggle completion status 8. Search / Filter Tasks - Search by keyword in task titles - Filter by: - Status (completed/incomplete) - Priority - Tag/Category 9. Sort Tasks - Sort tasks by: - Priority (High → Low) - Alphabetically by title - Optional: by due date (if implemented later) - Sorting must be stable 10. Input Validation - Reject invalid menu input - Reject empty titles - Handle invalid task IDs gracefully - Validate priorities and tags Non-Functional Requirements: - Python 3.x - Console-based - In-memory only - Standard library only - Single file implementation preferred Data Model: - Task: - id (int) - title (str) - completed (bool) - priority (str) - tags (list of str) Acceptance Criteria: - All previous Phase-1 features still work - New intermediate features work as described - Application runs without crashing on invalid input - Gemini-generated code runs without manual modification"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add, View, and Manage Tasks with Enhanced Details (Priority: P1)
As a user, I want to add new tasks with optional priority and tags, view them with these details, and modify these details later so that I can organize and track my tasks more effectively.

**Why this priority**: This extends the core task management with new attributes, making the application more functional and useful for organization.

**Independent Test**: A user can add a task with priority and tags, view these details in the task list, and then update them.

**Acceptance Scenarios**:
1. **Given** the application is running, **When** the user selects "Add Task" and enters a title, optional priority (High/Medium/Low), and optional tags, **Then** a new task is created with these details.
2. **Given** tasks exist with various priorities and tags, **When** the user selects "View Tasks", **Then** all tasks are displayed with their ID, title, completion status, priority, and tags.
3. **Given** a task exists, **When** the user selects "Update Task", provides the correct ID, and enters new priority and/or tags (along with an optional new title), **Then** the task's priority and/or tags are updated.
4. **Given** the user enters an invalid priority (not High/Medium/Low), **When** adding or updating a task, **Then** an error message is displayed, and the priority is not set or updated.

---

### User Story 2 - Search and Filter Tasks (Priority: P2)
As a user, I want to search for tasks by keywords and filter them by various criteria (status, priority, tags) so that I can quickly find specific tasks or subsets of my tasks.

**Why this priority**: Enhances usability significantly by allowing users to navigate potentially long task lists.

**Independent Test**: A user can add multiple tasks, then successfully search for them by title keyword or filter them by status, priority, or tags.

**Acceptance Scenarios**:
1. **Given** tasks exist with various titles, **When** the user selects "Search / Filter Tasks" and enters a keyword, **Then** only tasks whose titles contain the keyword are displayed.
2. **Given** tasks exist with various statuses, **When** the user selects "Search / Filter Tasks" and filters by "completed" status, **Then** only completed tasks are displayed.
3. **Given** tasks exist with various priorities, **When** the user selects "Search / Filter Tasks" and filters by a specific priority (e.g., "High"), **Then** only tasks with that priority are displayed.
4. **Given** tasks exist with various tags, **When** the user selects "Search / Filter Tasks" and filters by a specific tag, **Then** only tasks containing that tag are displayed.

---

### User Story 3 - Sort Tasks (Priority: P3)
As a user, I want to sort my tasks by priority or alphabetically by title so that I can organize my task list according to my current needs.

**Why this priority**: Provides additional organizational capabilities, making the task list easier to manage.

**Independent Test**: A user can add multiple tasks with varying priorities and titles, then successfully sort them by priority (High to Low) and alphabetically by title.

**Acceptance Scenarios**:
1. **Given** tasks exist with different priorities, **When** the user selects "Sort Tasks" and chooses to sort by priority, **Then** the tasks are displayed sorted by priority (High > Medium > Low), with tasks of the same priority maintaining their original relative order (stable sort).
2. **Given** tasks exist with different titles, **When** the user selects "Sort Tasks" and chooses to sort by title, **Then** the tasks are displayed sorted alphabetically by title, with tasks having the same title maintaining their original relative order (stable sort).

---
### Edge Cases
- What happens when a search keyword yields no results?
- What happens if the user tries to filter by a tag that doesn't exist on any task?
- How does the system handle an empty list of tasks when sorting is attempted?
- What happens if the user enters non-integer input for a menu selection or task ID?
- How are multiple tags handled (e.g., comma-separated input)?

## Requirements *(mandatory)*

### Functional Requirements
- **FR-001**: The system MUST display a main menu with numbered options, including "Search / Filter Tasks" and "Sort Tasks".
- **FR-002**: The main menu MUST repeat after each action until the user chooses to exit.
- **FR-003**: Users MUST be able to add a task with a non-empty title, and optional priority (High/Medium/Low) and tags (list of strings).
- **FR-004**: The system MUST assign a unique, positive, incremental integer ID to each new task, starting from 1.
- **FR-005**: All new tasks MUST default to a completion status of "Incomplete".
- **FR-006**: Users MUST be able to view a list of all tasks, including their ID, title, completion status, priority, and tags.
- **FR-007**: The system MUST display a message if the user tries to view tasks when none exist.
- **FR-008**: Users MUST be able to update the title, priority, and tags of an existing task by providing its ID. The task ID must remain unchanged.
- **FR-009**: Users MUST be able to toggle the completion status of an existing task by providing its ID.
- **FR-010**: Users MUST be able to delete an existing task by providing its ID.
- **FR-011**: Deleted task IDs MUST NOT be reused.
- **FR-012**: Users MUST be able to search for tasks by keyword in their titles.
- **FR-013**: Users MUST be able to filter tasks by status (completed/incomplete), priority (High/Medium/Low), and tags.
- **FR-014**: Users MUST be able to sort tasks by priority (High → Low) and alphabetically by title. Sorting MUST be stable.
- **FR-015**: The system MUST handle invalid user input gracefully (e.g., non-numeric menu choices, non-existent task IDs, invalid priority values) by showing an error message and not crashing.

### Non-Functional Requirements
- **NFR-001**: The application MUST be a console-based application.
- **NFR-002**: The application MUST be written in Python 3.x.
- **NFR-003**: The application MUST NOT use any external libraries; only the Python standard library is permitted.
- **NFR-004**: All task data MUST be stored in-memory. The application state is lost when it exits.
- **NFR-005**: The entire application logic SHOULD preferably be contained within a single Python file, but modularization is acceptable if complexity necessitates it and is approved in the plan.

### Key Entities
- **Task**: Represents a single todo item.
  - **id** (integer): A unique identifier for the task.
  - **title** (string): A description of the task.
  - **completed** (boolean): The completion status of the task.
  - **priority** (string): The urgency of the task. Valid values: "High", "Medium", "Low". Default: "Medium".
  - **tags** (list of strings): A list of categories or keywords associated with the task. Default: empty list.

## Success Criteria *(mandatory)*

### Measurable Outcomes
- **SC-001**: 100% of the Phase-1 features continue to function correctly.
- **SC-002**: 100% of the new intermediate features (Add with details, View with details, Update details, Search, Filter, Sort) are implemented and work correctly as per the acceptance scenarios.
- **SC-003**: The application demonstrates 0 crashes or unhandled exceptions during a standard testing session covering all features and common invalid inputs.
- **SC-004**: A user can successfully add, view, update, search, filter, and sort tasks within the console application.
- **SC-005**: The final, AI-generated Python script runs without any manual modifications.