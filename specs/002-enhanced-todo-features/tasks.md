# Tasks: In-Memory Python Console Todo Application (Intermediate Level)

**Input**: Design documents from `specs/002-enhanced-todo-features/`
**Prerequisites**: plan.md, spec.md, data-model.md, research.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`
- **[P]**: Can run in parallel
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions
- **Single project**: `src/main.py`

---
## Phase 1: Setup

**Purpose**: Update global state and menu for new features.

- [X] T001 In `src/main.py`, update `display_menu()` to include "Search / Filter Tasks" (6) and "Sort Tasks" (7) options, shifting "Exit" to (8).
- [X] T002 In `src/main.py`, modify the `tasks` global list to ensure each new task dictionary includes default `priority` ("Medium") and `tags` (empty list) fields.

---
## Phase 2: Foundational (Helper Functions & Data Structure Updates)

**Purpose**: Implement helper functions and update core logic to support new data fields before integrating into main workflow.

- [X] T003 In `src/main.py`, implement a helper function `get_task_by_id(task_id)` to reliably retrieve a task dictionary by its ID, returning `None` if not found.
- [X] T004 In `src/main.py`, implement a helper function `validate_priority(priority_str)` that checks if a string is "High", "Medium", or "Low", returning a canonical form or `None`.
- [X] T005 In `src/main.py`, implement a helper function `parse_tags(tags_str)` that takes a comma-separated string of tags and returns a list of cleaned-up tag strings.
- [X] T006 In `src/main.py`, update `add_task()` to prompt for optional `priority` and `tags` and use `validate_priority` and `parse_tags` for input processing.

---
## Phase 3: User Story 1 - Add, View, and Manage Tasks with Enhanced Details (Priority: P1)

**Goal**: Allow users to add tasks with optional priority and tags, view them with these details, and modify these details later.
**Independent Test**: A user can add a task with priority and tags, view these details in the task list, and then update them.

### Implementation for User Story 1
- [X] T007 [US1] In `src/main.py`, update `view_tasks()` to display the `priority` and `tags` for each task.
- [X] T008 [US1] In `src/main.py`, update `update_task()` to prompt for new `priority` and `tags` (using helper validation) in addition to the title.
- [X] T009 [US1] In `src/main.py`, update `main()` loop to handle the new menu option numbers for `update_task` and `mark_task_complete` (now 3 and 5 respectively).

**Checkpoint**: User Story 1 (with enhanced details) should be fully functional and testable independently.

---
## Phase 4: User Story 2 - Search and Filter Tasks (Priority: P2)

**Goal**: Allow users to search for tasks by keywords and filter them by various criteria.
**Independent Test**: A user can add multiple tasks, then successfully search for them by title keyword or filter them by status, priority, or tags.

### Implementation for User Story 2
- [X] T010 [US2] In `src/main.py`, implement `search_filter_tasks()` function. This function should:
    - Present a sub-menu for search/filter options (keyword, status, priority, tag).
    - Prompt for search/filter criteria.
    - Apply criteria to the `tasks` list and display matching tasks using `view_tasks` logic.
    - Handle edge cases like no results or invalid filter input.
- [X] T011 [US2] In `src/main.py`, integrate `search_filter_tasks()` into the `main()` loop (menu option 6).

**Checkpoint**: User Stories 1 and 2 should both work independently.

---
## Phase 5: User Story 3 - Sort Tasks (Priority: P3)

**Goal**: Allow users to sort their tasks by priority or alphabetically by title.
**Independent Test**: A user can add multiple tasks with varying priorities and titles, then successfully sort them by priority (High to Low) and alphabetically by title.

### Implementation for User Story 3
- [X] T012 [US3] In `src/main.py`, implement `sort_tasks()` function. This function should:
    - Present a sub-menu for sorting options (priority, title).
    - Sort the `tasks` list (or a copy for display) using Python's `sorted()` with a custom key for priority.
    - Display the sorted tasks using `view_tasks` logic.
    - Ensure stable sorting.
- [X] T013 [US3] In `src/main.py`, integrate `sort_tasks()` into the `main()` loop (menu option 7).

**Checkpoint**: All user stories should now be independently functional.

---
## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories.

- [X] T014 In `src/main.py`, refactor existing input validation within `add_task`, `update_task`, `mark_task_complete`, `delete_task` functions to use `get_task_by_id` helper.
- [X] T015 In `src/main.py`, ensure all new input prompts (for priority, tags, search keywords, filter criteria, sort options) have robust validation and clear error messages, consistent with existing validation.
- [X] T016 In `src/main.py`, review `main()` loop's input handling to ensure it correctly maps all new menu choices (1-8) to their respective functions.
- [X] T017 Review the entire `src/main.py` file for clarity, comments on complex logic (if any), and adherence to the plan. Ensure Phase-1 functionality is fully preserved.

---
## Dependencies & Execution Order

### Phase Dependencies
- **Setup (Phase 1)** -> **Foundational (Phase 2)** -> **User Story 1 (Phase 3)** -> **User Story 2 (Phase 4)** -> **User Story 3 (Phase 5)** -> **Polish (Phase 6)**
- Each phase depends on the completion of the previous one.

### Implementation Strategy

### MVP First (User Story 1 with Enhanced Details)
1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test adding, viewing, and modifying tasks with new details independently. This is the minimum viable product for Phase-I Intermediate.

### Incremental Delivery
1. Complete Setup + Foundational -> Foundation ready.
2. Add User Story 1 -> Test independently -> MVP ready.
3. Add User Story 2 -> Test independently.
4. Add User Story 3 -> Test independently.
5. Complete Polish -> Final product for Phase-I Intermediate ready.

This phased approach ensures that a working, testable application is available at each stage of development.
