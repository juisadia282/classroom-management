from flask import Flask, render_template, request

app = Flask(__name__)

SCHOOL = "ABC Model School"
CLASS_NAME = "Class 8"
TEACHER = "Sadia Sultana"
PASS_MARK = 70

DEFAULT_STUDENTS = [
    {"name": "Rahim", "attendance": "Present", "marks": 85},
    {"name": "Karim", "attendance": "Absent", "marks": 60},
    {"name": "Sumaiya", "attendance": "Present", "marks": 92},
    {"name": "Nila", "attendance": "Present", "marks": 65},
    {"name": "Jui", "attendance": "Absent", "marks": 75},
    {"name": "Rafi", "attendance": "Present", "marks": 78},
    {"name": "Mim", "attendance": "Present", "marks": 88},
    {"name": "Hasan", "attendance": "Present", "marks": 55},
    {"name": "Tania", "attendance": "Absent", "marks": 82},
    {"name": "Sakib", "attendance": "Present", "marks": 69},
]

def make_report(students):
    present = 0
    absent = 0
    group_a = 0
    group_b = 0
    total_marks = 0

    for student in students:
        if student["attendance"] == "Present":
            present += 1
        else:
            absent += 1

        if student["marks"] >= PASS_MARK:
            student["group"] = "A"
            student["group_label"] = "Good Student"
            group_a += 1
        else:
            student["group"] = "B"
            student["group_label"] = "Weak Student"
            group_b += 1

        total_marks += student["marks"]

    average = round(total_marks / len(students), 1) if students else 0
    return {
        "total": len(students),
        "present": present,
        "absent": absent,
        "group_a": group_a,
        "group_b": group_b,
        "average": average,
    }

@app.route("/", methods=["GET", "POST"])
def home():
    students = [dict(s) for s in DEFAULT_STUDENTS]
    message = ""

    if request.method == "POST":
        names = request.form.getlist("name")
        attendance_values = request.form.getlist("attendance")
        mark_values = request.form.getlist("marks")
        updated = []

        for name, attendance, mark_text in zip(names, attendance_values, mark_values):
            name = name.strip()
            if not name:
                continue
            try:
                marks = int(mark_text)
            except (TypeError, ValueError):
                marks = 0
            marks = max(0, min(100, marks))
            if attendance not in ("Present", "Absent"):
                attendance = "Absent"
            updated.append({
                "name": name.title(),
                "attendance": attendance,
                "marks": marks
            })

        if updated:
            students = updated
            message = "Class report updated successfully."
        else:
            message = "No student information was submitted."

    summary = make_report(students)
    return render_template(
        "index.html",
        school=SCHOOL,
        class_name=CLASS_NAME,
        teacher=TEACHER,
        pass_mark=PASS_MARK,
        students=students,
        summary=summary,
        message=message,
    )

if __name__ == "__main__":
    app.run(debug=True)
