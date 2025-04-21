
Personal Learning Dashboard
Video Demo:https://youtu.be/iCaUQidTtBI
Name: Hamza Nawaz
GitHub: Hamzanawazwato
clone repository:(https://github.com/hamzanawazwatoo/personal-learning-dashboard.git)
edX Username: Hamzanawazwato
Location: Lahore, Punjab, Pakistan
Date of Submission: April 20, 2025

# Personal Learning Dashboard

# Introduction

For my CS50x 2025 final project, I created a web-based application called the Personal Learning Dashboard. It is a goal-tracking and productivity tool aimed at helping students or self-learners set, manage, and monitor their educational objectives. The inspiration came from my own journey as a student who juggles multiple learning goals, such as programming, data science, and competitive exams. I wanted a tool that could centralize these goals and give visual feedback on my progress.

This dashboard allows users to register, log in, set learning goals, update their progress, and visualize their progress using interactive bars. The interface is clean, responsive, and designed for ease of use. I built this project using Flask for the backend, SQLite for the database, HTML/CSS (with Bootstrap) for the frontend, and JavaScript for interactivity.

# Features

- **User Authentication**: Users can register and log in securely. The session persists during use, and each user sees only their own goals.
- **Goal Management**: Users can add new goals with a title, description, deadline, and progress percentage. They can update or delete goals as needed.
- **Visual Feedback**: Each goal is displayed with a progress bar indicating how close the user is to completion.
- **Responsive Design**: The site is usable on both desktop and mobile thanks to Bootstrap.
- **Data Persistence**: All user data is stored in an SQLite database and is retrieved dynamically.

# Design Decisions

One of the major design decisions I had to make was whether to use a full JavaScript frontend framework like React or stick with server-side rendering using Flask. Since this is my first web app and I wanted to keep it simple yet functional, I chose Flask. This allowed me to focus more on logic and database integration without overcomplicating the frontend.

I also debated storing goals as JSON strings inside a single database column vs. using normalized SQL tables. I chose the normalized SQL table method for scalability and better query support.

For styling, I considered using custom CSS throughout but decided to use Bootstrap for faster development and guaranteed responsiveness.

## File Descriptions

### `app.py`
This is the main Python file that runs the Flask application. It defines all the routes (e.g., `/`, `/login`, `/register`, `/dashboard`, `/add_goal`, `/edit_goal`, etc.). It handles logic for user authentication, adding/editing/deleting goals, and rendering the appropriate templates with context variables.

### `templates/`
This folder contains all the HTML templates for the app, rendered by Flask using Jinja2.

- `layout.html`: Base HTML layout used across all pages. Contains the navbar and links to CSS and JS files.
- `index.html`: The homepage that introduces the app and links to login/register.
- `login.html`: The user login form.
- `register.html`: The user registration form.
- `dashboard.html`: The main interface where users can see their goals, add new ones, update progress, and delete them.
- `add_goal.html`: A form where users can input a new learning goal.
- `edit_goal.html`: A form pre-filled with an existing goal's details for updating.

### `static/`
Contains all the static assets (CSS and JavaScript) used by the app.

- `style.css`: Custom styling applied on top of Bootstrap. It defines specific styles for goal cards, progress bars, and dashboard layout.
- `script.js`: Contains JavaScript code for progress bar animations and client-side interactivity. It could also be extended to support AJAX updates in future versions.

## `goals.db`
The SQLite database file. It contains two tables:
- `users`: Stores user credentials (id, username, hashed password).
- `goals`: Stores individual learning goals linked to user ID.

### `README.md`
This document — a detailed explanation of the project.

### `requirements.txt`
Lists Python dependencies. Currently includes:
- `Flask`
- `Flask-Session`
- `Werkzeug`
- `sqlite3` (built-in)

## How to Run the Project

1. Clone the repository or download the ZIP.
2. Navigate to the project directory.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
Run the app:

bash
Copy
Edit
flask run
Visit http://127.0.0.1:5000 in your browser.
And the webpage fully fuctional shows login page

Limitations
The project currently lacks password recovery and email verification.

Progress is entered manually; it doesn't auto-track learning.

No notifications or reminders are implemented yet.

Sessions are cleared once the browser is closed (unless persistent sessions are added).

Future Plans
Add support for goal categories and tags (e.g., "Programming", "Math").

Add email reminders and a calendar integration.

Improve the frontend using a JavaScript framework like Vue or React.

Add export functionality (PDF or CSV reports of goals).

Conclusion
This project represents the culmination of everything I’ve learned in CS50x: from Python and Flask to HTML, CSS, and databases. It’s functional, personalized, and something I’ll continue to build on. I’ve gained hands-on experience in full-stack development, and this project gave me the confidence to continue pursuing web and AI-based solutions.

Author
Hamzanawazwato
Email
hamzawatoo5152@gmail.com


