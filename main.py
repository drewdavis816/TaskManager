

from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)
TASKS_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)


@app.route('/search', methods=['GET'])
def search_tasks():
    search_term = request.args.get('search_term', '').lower()
    tasks = load_tasks()

    if search_term:
        filtered = [task for task in tasks if search_term in task['name'].lower()]
    else:
        filtered = tasks

    return render_template('index.html', tasks=filtered)


@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task_name').strip()
    due_date = request.form.get('due_date')

    if not task_name:
        return redirect('/')

    tasks = load_tasks()

    # Check if task already exists
    for task in tasks:
        if task["name"].lower() == task_name.lower():
            return redirect('/')

    tasks.append({"name": task_name, "done": False, "due_date": due_date})
    save_tasks(tasks)

    return redirect('/')


@app.route('/complete/<int:index>', methods=['POST'])
def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = not tasks[index]["done"]
        save_tasks(tasks)
    return redirect('/')


@app.route('/delete/<int:index>', methods=['POST'])
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)