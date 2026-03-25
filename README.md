# CLI-To-Do-List-Manager
CLI To-Do List Manager (Python Project)

## Features
Add a new task
View all tasks
Mark a task as completed
Delete a task
Store tasks in a JSON file (`tasks.json`)

## Storage (`tasks.json`)
Tasks are persisted to `tasks.json` as JSON data.

Expected shape (`tasks.json`):
- Top-level JSON value is an array (list) of tasks.
- Each task item looks like:
  - `id`: integer (unique per task)
  - `description`: string (task text)
  - `completed`: boolean

## How to run
1. Make sure you have Python 3 installed.
2. From the project folder, run:
   - `python main.py`

## Project Structure
- `main.py`: CLI entry point
- `tasks.json`: persisted task storage (read/write)
- `README.md`: project documentation