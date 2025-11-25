# Task Manager

A Flask web application for managing daily tasks with due dates, search functionality, and task completion tracking.

## Features

- ✅ Create tasks with titles and due dates
- ✅ Mark tasks as complete/incomplete
- ✅ Delete tasks
- ✅ Search and filter tasks
- ✅ Due date tracking
- ✅ Persistent data storage (JSON)

## Tech Stack

- Python 3
- Flask
- HTML/CSS
- JSON (data storage)

## Live Demo

[Task Manager Live](https://task-manager-xxxxx.onrender.com)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/drewdavis816/TaskManager.git
cd TaskManager
```

2. Create a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
python3 main.py
```

5. Open your browser and go to `http://127.0.0.1:5000`

## How to Use

1. Add a task by entering a title and optional due date
2. Click "Complete" to mark a task done
3. Use the search bar to filter tasks
4. Click "Delete" to remove a task
5. Refresh the page - your tasks persist!

## Project Structure
```
TaskManager/
├── main.py              # Flask app and routes
├── templates/
│   └── index.html       # Task manager UI
├── static/
│   └── style.css        # Styling
├── tasks.json           # Data storage
└── requirements.txt     # Dependencies
```

## What I Learned

- Flask routing and request handling
- HTML forms and template rendering
- JSON file storage
- CSS styling and responsive design
- Search and filter functionality

## Future Improvements

- Add task categories
- User authentication
- Database integration (SQL)
- Task priority levels