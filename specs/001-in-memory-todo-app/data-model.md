# Data Model: Todo Application

## Entities

### Task
Represents a single todo item.

| Attribute | Type | Description | Constraints |
|---|---|---|---|
| `id` | integer | A unique identifier for the task. | Required, Unique, Positive |
| `title` | string | A description of the task. | Required, Non-empty |
| `completed`| boolean | The completion status of the task. | Required, Defaults to `False` |

## In-Memory Representation
The collection of tasks will be stored in a `list` of `dictionaries`.

**Example**:
```python
tasks = [
    {
        "id": 1,
        "title": "Buy milk",
        "completed": False
    },
    {
        "id": 2,
        "title": "Walk the dog",
        "completed": True
    }
]
```
