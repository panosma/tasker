#!/usr/bin/env python3
import json
import os
import sys

BASE = os.path.dirname(os.path.realpath(__file__))
FILE = os.path.join(BASE, "tasks.json")

# Decorations
DIVIDER = "-" * 50
DOUBLE_DIVIDER = "=" * 50

def load_tasks():
    """Open/load the JSON file (create empty structure if missing or invalid)"""
    if not os.path.exists(FILE):
        return {"tasks": []}
    try:
        with open(FILE, "r") as f:
            # Handle empty file
            content = f.read()
            if not content:
                return {"tasks": []}
            return json.loads(content)
    except json.JSONDecodeError:
        return {"tasks": []}

def save_tasks(data):
    """Saves the current tasklist to the JSON file"""
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def clear_screen():
    """Clears the terminal screen"""
    os.system("cls" if os.name == "nt" else "clear")

def print_tasks(tasks, title=""):
    """Prints a list of tasks with a title"""
    clear_screen()
    print("\n")
    print(DOUBLE_DIVIDER)
    count = len(tasks)
    if title:
        header = title.upper()
    else:
        header = f"There are {count} tasks".upper()
    print(header.center(50))
    print(DOUBLE_DIVIDER)
    if not tasks:
        print("No tasks to show.".center(50))
        print(DOUBLE_DIVIDER)
    else:
        for task in tasks:
            print(f" {task['id']:>3}    {task['title']:<25}   {task['status']:>14}")
            print(DIVIDER)
    print("\n")

def add_task(tasklist, title):
    """Adds a new task"""
    new_id = max((t["id"] for t in tasklist), default=0) + 1
    new_task = {
        "id": new_id,
        "title": title,
        "status": "todo",
    }
    tasklist.append(new_task)
    print(f"Added #{new_id}: {title}")
    return True # indicates success

def delete_task(tasklist, task_id):
    """Deletes a task by id"""
    target = None
    for t in tasklist:
        if t["id"] == task_id:
            target = t
            break
    if target is None:
        print(f"No task with id {task_id}")
        return False
    tasklist.remove(target)
    print(f"Deleted task #{task_id}")
    return True

def update_task(tasklist, task_id, new_status):
    """Updates the status of a task"""
    new_status = new_status.lower()
    valid_status = {"todo", "started", "done"}
    if new_status not in valid_status:
        print("Invalid status. Use: todo, started, done")
        return False
    for t in tasklist:
        if t["id"] == task_id:
            if t["status"] == new_status:
                print("Same status, no changes made")
                return False # No change is not a success in terms of modification
            t["status"] = new_status
            print(f"Status of task # {task_id} updated to {new_status}")
            return True
    print(f"No task with id {task_id}")
    return False

def delete_done(tasklist):
    """Deletes all tasks with status 'done'"""
    original_count = len(tasklist)
    tasks_to_keep = [t for t in tasklist if t["status"] != "done"]
    tasklist[:] = tasks_to_keep # Modify the list in place
    total_deleted = original_count - len(tasklist)
    print(f"Deleted {total_deleted} completed tasks")
    return total_deleted > 0

def show_done(tasklist):
    """Shows all tasks with status 'done'"""
    done_tasks = [task for task in tasklist if task["status"] == "done"]
    print_tasks(done_tasks, title=f"Completed tasks: {len(done_tasks)}")

def main():
    """Main function to run the task manager"""
    data = load_tasks()
    tasklist = data["tasks"]
    args = sys.argv[1:]

    clear_screen()
    print("\n")

    if not args:
        print_tasks(tasklist)
        return

    command = args[0]
    modified = False

    if command == "add" and len(args) >= 2:
        modified = add_task(tasklist, " ".join(args[1:]).strip())
    elif command == "delete" and len(args) == 2:
        try:
            modified = delete_task(tasklist, int(args[1]))
        except ValueError:
            print("ID must be an integer")
    elif command == "update" and len(args) == 3:
        try:
            tid = int(args[1])
            modified = update_task(tasklist, tid, args[2])
        except ValueError:
            print("ID must be an integer")
    elif command == "cleardone" and len(args) == 1:
        modified = delete_done(tasklist)
    elif command == "show_done" and len(args) == 1:
        show_done(tasklist)
    else:
        print_tasks(tasklist)

    if modified:
        save_tasks(data)
        if command not in ["show_done", "add"]: # show_done prints its own list, add just confirms
             print_tasks(tasklist)


if __name__ == "__main__":
    main()