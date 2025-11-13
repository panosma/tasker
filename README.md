# Task Tracker CLI

A simple command-line task manager to keep track of your tasks.

## Features

*   Add, delete, and update tasks.
*   View all tasks or filter by status.
*   Tasks are stored in a `tasks.json` file.

## Installation

1.  Clone the repository or download the `tasker.py` script.
2.  Make sure you have Python 3 installed.

## Usage

To use the Task Tracker CLI, run the `tasker.py` script from your terminal with one of the following commands:

### View all tasks

To view all tasks, run the script without any arguments:

```bash
python3 tasker.py
```

### Add a task

To add a new task, use the `add` command followed by the task title:

```bash
python3 tasker.py add "My new task"
```

### Delete a task

To delete a task, use the `delete` command followed by the task ID:

```bash
python3 tasker.py delete 1
```

### Update a task

To update a task's status, use the `update` command followed by the task ID and the new status. The available statuses are `todo`, `started`, and `done`.

```bash
python3 tasker.py update 1 started
```

### Clear completed tasks

To delete all tasks with the status `done`, use the `cleardone` command:

```bash
python3 tasker.py cleardone
```

### Show completed tasks

To view all tasks with the status `done`, use the `show_done` command:

```bash
python3 tasker.py show_done
```
