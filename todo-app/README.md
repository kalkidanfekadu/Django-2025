# Simple Todo App

## Description
A command-line todo app that saves tasks in a JSON file.

## How to Run
1. Save the code as `todo_app.py`
2. Run: `python todo_app.py`
3. Choose options from the menu

## Features
- Add tasks
- View all tasks
- Update tasks
- Delete tasks
- Saves automatically to `todos.json`

## JSON Storage
Tasks are saved in `todos.json` file in this format:
```json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "completed": false
  }
]