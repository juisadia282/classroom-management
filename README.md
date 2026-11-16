# ABC Model School — Classroom Management System

A small Python Flask web app for Class 8 attendance and class-test result reporting.

## Features
- Student list with attendance and marks
- Present / absent totals
- Group A (70–100) and Group B (below 70)
- Average marks
- Edit attendance and marks, then update the report

## Run locally
1. Install Python.
2. Run `pip install -r requirements.txt`
3. Run `python app.py`
4. Open `http://127.0.0.1:5000`

## Deploy to Vercel
1. Upload `app.py`, `requirements.txt`, and the `templates` folder to a GitHub repository.
2. Sign in at https://vercel.com and choose Add New → Project.
3. Import the GitHub repository and deploy. Vercel detects Flask applications.
4. Open the deployment URL to test the app.

Note: This first version uses sample data in the Python file and does not save edits permanently in a database. On a new page visit, the original sample data loads again. It is a classroom demonstration project, not a production school records system.
