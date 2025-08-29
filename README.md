# Water Intake Tracker 

A simple Django web application to help users track their daily water intake, set personalized hydration goals, and monitor their weekly progress.

---

## Features

-  Add daily water intake entries
-  Set and update personalized daily water intake goals
-  View water intake history for the past week
-  User registration and login
-  Notifications when daily goals are met
-  User-specific data and secure access

---

## Tech Stack

- Python 3
- Django
- SQLite (default development database)

---

## Getting Started

### Prerequisites

- Python 3.x installed
- Virtual environment tool like `venv` or `virtualenv`

### Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/VaishnaviPoudel/WaterIntakeTracker.git
   cd WaterIntakeTracker
   ```

2. **Create and activate a virtual environment:**
   ```bash
    python -m venv env
    source env/bin/activate      # On Windows: env\Scripts\activate
    ```
3. **Install dependencies:**
   ```bash
    pip install -r requirements.txt
    ```
4. **Apply Migrations**
   ```bash
    python manage.py migrate
    ```
5. **Run the Development Server** 
   ```bash
    python manage.py runserver
    ```
6. **Open your browser and visit:** `http://127.0.0.1:8000/`

## Usage

- Register a new account or log in.
- Set your daily water intake goal.
- Add water intake throughout the day.
- View your progress and weekly history on the home page.
