# Feature Specification: In-Memory Python Console Todo Application

**Feature Branch**: `001-in-memory-todo-app`
**Created**: 2025-12-25
**Status**: Draft
**Input**: User description: "Phase: I Title: In-Memory Python Console Todo Application Objective: Implement a fully functional console-based Todo application using Python that manages tasks entirely in memory and follows the Phase I constitution. Functional Requirements: 1. Application Startup - Display a repeating main menu on launch - Application exits only when user selects Exit 2. Menu Options 1. Add Task 2. View Tasks 3. Update Task 4. Delete Task 5. Mark Task as Complete 6. Exit 3. Add Task - Prompt user for task title - Title must be non-empty - Assign unique incremental integer ID starting from 1 - Task is incomplete by default - Store task in memory 4. View Tasks - If no tasks exist, show empty message - Display each task with ID, title, and completion status 5. Update Task - Prompt for task ID - If ID not found, show error - Prompt for new title - Update title only 6. Delete Task - Prompt for task ID - If ID not found, show error - Remove task from memory - Do not reuse deleted IDs 7. Mark Task as Complete - Prompt for task ID - If ID not found, show error - Toggle completion status 8. Input Validation - Reject invalid menu input - Reject empty titles - Handle invalid IDs gracefully Non-Functional Requirements: - Python 3.x - Console-based - In-memory only - Standard library only - Single file implementation Data Model: - Task: id (int), title (str), completed (bool) Acceptance Criteria: - All Phase I features function correctly - No crashes on invalid input - Gemini-generated code runs without modification"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add and View Tasks (Priority: P1)
As a user, I want to add new tasks and see a list of all my tasks so that I can keep track of what I need to do.

**Why this priority**: This is the core functionality of a todo application. Without it, the application is useless.

**Independent Test**: The user can launch the application, add one or more tasks, and view them in a list. This journey delivers the fundamental value of capturing tasks.

**Acceptance Scenarios**:
1. **Given** the application is running and no tasks exist, **When** the user selects "View Tasks", **Then** a message "No tasks found." is displayed.
2. **Given** the application is running, **When** the user selects "Add Task" and enters a valid title, **Then** a new task is created with a unique ID and a status of "Incomplete".
3. **Given** a task has been added, **When** the user selects "View Tasks", **Then** the task is displayed with its ID, title, and completion status.

---

### User Story 2 - Modify Existing Tasks (Priority: P2)
As a user, I want to update the title of a task, or mark a task as complete, so I can reflect changes in my work.

**Why this priority**: Modifying tasks is a fundamental feature for managing a changing workload.

**Independent Test**: The user can add a task, then update its title. The user can also add a task and then mark it as complete.

**Acceptance Scenarios**:
1. **Given** a task exists, **When** the user selects "Update Task", provides the correct ID, and enters a new title, **Then** the task's title is updated.
2. **Given** a task exists with a status of "Incomplete", **When** the user selects "Mark Task as Complete", and provides the correct ID, **Then** the task's status changes to "Complete".
3. **Given** a task exists with a status of "Complete", **When** the user selects "Mark Task as Complete", and provides the correct ID, **Then** the task's status changes to "Incomplete".
4. **Given** the user tries to update a task with an ID that does not exist, **When** they enter the non-existent ID, **Then** an error message "Task not found." is displayed.

---

### User Story 3 - Delete Tasks (Priority: P3)
As a user, I want to delete a task that is no longer needed, so I can keep my task list clean and relevant.

**Why this priority**: Removing completed or irrelevant tasks is essential for maintaining a usable todo list.

**Independent Test**: The user can add a task and then immediately delete it.

**Acceptance Scenarios**:
1. **Given** a task exists, **When** the user selects "Delete Task" and provides the correct ID, **Then** the task is permanently removed from the application's memory.
2. **Given** a task is deleted, **When** the user views the task list, **Then** the deleted task is no longer displayed.
3. **Given** the user tries to delete a task with an ID that does not exist, **When** they enter the non-existent ID, **Then** an error message "Task not found." is displayed.

---
### Edge Cases
- What happens when the user enters non-integer input for a menu selection?
- What happens when the user enters a non-integer for a Task ID prompt?
- What happens if the user enters a very long string for a task title?
- How does the system handle an empty title submission (e.g., just pressing Enter)?

## Requirements *(mandatory)*

### Functional Requirements
- **FR-001**: The system MUST display a main menu with numbered options upon startup.
- **FR-002**: The main menu MUST repeat after each action until the user chooses to exit.
- **FR-003**: Users MUST be able to add a task with a non-empty title.
- **FR-004**: The system MUST assign a unique, positive, incremental integer ID to each new task, starting from 1.
- **FR-005**: All new tasks MUST default to a completion status of "Incomplete".
- **FR-006**: Users MUST be able to view a list of all tasks, including their ID, title, and completion status.
- **FR-007**: The system MUST display a message if the user tries to view tasks when none exist.
- **FR-008**: Users MUST be able to update the title of an existing task by providing its ID.
- **FR-009**: Users MUST be able to toggle the completion status of an existing task by providing its ID.
- **FR-010**: Users MUST be able to delete an existing task by providing its ID.
- **FR-011**: Deleted task IDs MUST NOT be reused.
- **FR-012**: The system MUST handle invalid user input gracefully (e.g., non-numeric menu choices, non-existent task IDs) by showing an error message and not crashing.

### Non-Functional Requirements
- **NFR-001**: The application MUST be a console-based application.
- **NFR-002**: The application MUST be written in Python 3.x.
- **NFR-003**: The application MUST NOT use any external libraries; only the Python standard library is permitted.
- **NFR-004**: All task data MUST be stored in-memory. The application state is lost when it exits.
- **NFR-005**: The entire application logic MUST be contained within a single Python file.

### Key Entities
- **Task**: Represents a single todo item.
  - **id** (integer): A unique identifier for the task.
  - **title** (string): A description of the task.
  - **completed** (boolean): The completion status of the task.

## Success Criteria *(mandatory)*

### Measurable Outcomes
- **SC-001**: 100% of the Phase I functional requirements are implemented and work correctly as per the acceptance scenarios.
- **SC-002**: The application demonstrates 0 crashes or unhandled exceptions during a standard testing session covering all features and common invalid inputs.
- **SC-003**: The final, AI-generated Python script runs without any manual modifications.
- **SC-004**: A user can successfully add, view, update, complete, and delete a task in under 60 seconds.