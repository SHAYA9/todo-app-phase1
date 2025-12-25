---
id: 1
title: Create Project Constitution
stage: constitution
date: 2025-12-25
surface: agent
model: gemini
feature: none
branch: main
user: unknown
command: /sp.constitution
labels: [constitution, project-setup]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
tests:
  - none
---

## Prompt

/sp.constitution 
Project: In-Memory Python Console Todo Application (Phase I)

Purpose:
Build a minimal, correct, and spec-driven Todo application that runs in the Python console and stores all data in memory only.

Core principles:
- Spec-driven development (spec is the single source of truth)
- Deterministic behavior (same input → same output)
- Simplicity over abstraction
- Explicit state management
- Zero manual coding by human (Gemini generates all code)

Technical standards:
- Language: Python 3.x
- Execution mode: Console / CLI application
- Storage: In-memory only (no files, no database, no persistence)
- Architecture: Single-file Python script unless spec requires otherwise
- Dependencies: Python standard library only

Feature scope (Phase I only):
- Add Task
- Delete Task
- Update Task
- View Task List
- Mark Task as Complete

Data model rules:
- Each task must have:
  - unique integer ID
  - title (string)
  - completion status (boolean)
- Tasks must be stored in an in-memory collection
- IDs must not change once assigned

Behavior rules:
- Application runs in a loop until user exits
- All actions are triggered via numeric menu options
- User input must be validated
- Invalid actions must not crash the app
- Clear console output for every action

Constraints:
- No external libraries
- No GUI
- No file I/O
- No async code
- No object-relational mapping
- No manual edits after Gemini generates code

Success criteria:
- All Phase I features work correctly
- App runs without errors
- Code strictly follows the written spec
- Claude-generated output is directly executable
- Spec refinements are used instead of manual code changes

Out of scope:
- Persistence
- User accounts
- Networking
- Web or mobile UI
- Advanced architecture patterns

## Response snapshot

I have created the project constitution and updated the relevant templates.

## Outcome

- ✅ Impact: Created the project constitution and updated related templates.
- 🧪 Tests: none
- 📁 Files: .specify/memory/constitution.md, .specify/templates/plan-template.md
- 🔁 Next prompts: /sp.specify
- 🧠 Reflection: The constitution provides a solid foundation for the project.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
