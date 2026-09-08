# Task.Flow

A simple task management web application built with Flask and SQLite.

Task.Flow allows users to add, edit, complete, undo, and delete tasks through a clean web interface.

## Features

- Add new tasks
- Edit existing tasks
- Mark tasks as completed
- Undo completed tasks
- Delete tasks
- Empty-field validation
- Persistent data storage using SQLite
- Responsive dark-themed interface

## Tech Stack

- Python
- Flask
- SQLite
- HTML
- CSS
- Jinja2

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yagnagurram628/Task.Flow.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Task.Flow
   ```
   
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment on Windows:
   ```bash
   venv\Scripts\activate
   ```

5. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Run the application:
   ```bash
   python app.py
   ```

7. Open `http://127.0.0.1:5000` in your browser.