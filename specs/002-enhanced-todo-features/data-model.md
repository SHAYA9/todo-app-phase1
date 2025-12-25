# Data Model: Todo Application (Intermediate Level)

## Entities

### Task
Represents a single todo item, extended with priority and tags.

| Attribute | Type | Description | Constraints |
|---|---|---|---|
| `id` | integer | A unique identifier for the task. | Required, Unique, Positive |
| `title` | string | A description of the task. | Required, Non-empty |
| `completed`| boolean | The completion status of the task. | Required, Defaults to `False` |
| `priority`| string | The urgency of the task. | Required, "High", "Medium", "Low", Defaults to "Medium" |
| `tags` | list of strings | A list of categories or keywords associated with the task. | Optional, Defaults to empty list |

## In-Memory Representation
The collection of tasks will be stored in a `list` of `dictionaries`.

**Example**:
```python
tasks = [
    {
        "id": 1,
        "title": "Buy groceries",
        "completed": False,
        "priority": "High",
        "tags": ["personal", "shopping"]
    },
    {
        "id": 2,
        "title": "Finish report",
        "completed": True,
        "priority": "Medium",
        "tags": ["work"]
    }
]
```
