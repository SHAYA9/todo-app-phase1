# Tasks: In-Memory Python Console Todo Application

**Input**: Design documents from `specs/001-in-memory-todo-app/`
**Prerequisites**: plan.md, spec.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`
- **[P]**: Can run in parallel
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions
- **Single project**: `src/main.py`

---
## Phase 1: Setup

**Purpose**: Project initialization and basic structure.

- [X] T001 Create the `src` directory.
- [X] T002 Create the `src/main.py` file with initial scaffolding.
- [X] T003 In `src/main.py`, define the global state variables: `tasks` (list) and `task_id_counter` (int).

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented.

- [X] T004 In `src/main.py`, implement the main application loop that runs until the user chooses to exit.
- [X] T005 In `src/main.py`, implement the `display_menu` function to show the user the available options.
- [X] T006 In `src/main.py`, implement the logic to get and validate the user's menu choice.
- [X] T007 In `src/main.py`, set up the main `if __name__ == "__main__:"` block to start the application.

**Checkpoint**: Foundation ready - user story implementation can now begin.

---
## Phase 3: User Story 1 - Add and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Allow users to add tasks and view the full task list.
**Independent Test**: A user can start the app, add a task, and see it displayed in the task list.

### Implementation for User Story 1
- [X] T008 [US1] In `src/main.py`, implement the `view_tasks` function to display all tasks or a "no tasks" message.
- [X] T009 [US1] In `src/main.py`, implement the `add_task` function to prompt for a title and add a new task to the `tasks` list.
- [X] T010 [US1] In `src/main.py`, integrate the `view_tasks` and `add_task` functions into the main loop, calling them based on user input.

**Checkpoint**: User Story 1 should be fully functional and testable independently.

---
## Phase 4: User Story 2 - Modify Existing Tasks (Priority: P2)

**Goal**: Allow users to update a task's title or mark it as complete/incomplete.
**Independent Test**: A user can add a task, update its title, and then toggle its completion status.

### Implementation for User Story 2
- [X] T011 [US2] In `src/main.py`, implement the `update_task` function to prompt for a task ID and a new title.
- [X] T012 [US2] In `src/main.py`, implement the `mark_task_complete` function to prompt for a task ID and toggle the task's `completed` status.
- [X] T013 [US2] In `src/main.py`, integrate the `update_task` and `mark_task_complete` functions into the main loop.

**Checkpoint**: User Stories 1 AND 2 should both work independently.

---
## Phase 5: User Story 3 - Delete Tasks (Priority: P3)

**Goal**: Allow users to remove tasks from the list.
**Independent Test**: A user can add a task and then immediately delete it.

### Implementation for User Story 3
- [X] T014 [US3] In `src/main.py`, implement the `delete_task` function to prompt for a task ID and remove the corresponding task.
- [X] T015 [US3] In `src/main.py`, integrate the `delete_task` function into the main loop.

**Checkpoint**: All user stories should now be independently functional.

---
## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories, primarily error handling.

- [X] T016 In `src/main.py`, add robust input validation and error handling for all user inputs (menu selections, task IDs, and task titles) to prevent crashes.
- [X] T017 In `src/main.py`, ensure the exit mechanism works cleanly.
- [X] T018 Review the entire `src/main.py` file for clarity, comments on complex logic (if any), and adherence to the plan.

---
## Dependencies & Execution Order

### Phase Dependencies
- **Setup (Phase 1)** -> **Foundational (Phase 2)** -> **User Story 1 (Phase 3)** -> **User Story 2 (Phase 4)** -> **User Story 3 (Phase 5)** -> **Polish (Phase 6)**
- Each phase depends on the completion of the previous one.

### Implementation Strategy

### MVP First (User Story 1 Only)
1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test adding and viewing tasks independently. This is the minimum viable product.

### Incremental Delivery
1. Complete Setup + Foundational -> Foundation ready.
2. Add User Story 1 -> Test independently -> MVP is ready.
3. Add User Story 2 -> Test independently.
4. Add User Story 3 -> Test independently.
5. Complete Polish -> Final product is ready.

This phased approach ensures that a working, testable application is available at each stage of development.
