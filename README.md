
# 🎓 College Management System

A web-based College Management System built with **Django** to manage departments, staff, courses, exams, and results efficiently.

---

## 🚀 Features

- Staff registration and management
- Course creation and assignment
- Exam scheduling
- Result management (including grades)
- Unique IDs for Staff, Courses, and Exams
- Admin-friendly backend interface
- Clean relational models with Django ORM

---

## 🧱 Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite (default)
- **Frontend**: HTML, CSS, Bootstrap (optional)
- **Hosting**: GitHub (manually uploaded)

---

## 🗂️ Models Overview

### `Staff`
- `staff_id` (Auto-generated like `STAf-0001`)
- `username`, `email`
- `department`, `course`

### `Course`
- `course_id` (Auto-generated like `CR-0001`)
- `department`, `course`
- `staff_name`, `staff_email`

### `Exam`
- `exam_id` (Auto-generated like `EX-0001`)
- `exam_name`, `course`, `date`, `duration`

### `Result`
- `student_id`, `student_name`
- Linked to `Course` and `Exam`
- `score`, `grade`

---

## 🛠️ Setup Instructions

1. **Download or Clone the repository**
   ```bash
   git clone https://github.com/Usmantech125/College-Management-System.git
   cd College-Management-System
   ```
   Or download the ZIP and extract it.

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies manually**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (admin panel)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server**
   ```bash
   python manage.py runserver
   ```

7. Visit:  
   - App: `http://127.0.0.1:8000/`  
   - Admin: `http://127.0.0.1:8000/admin`

---

## 📂 Project Structure

```
College-Management-System/
│
├── staff/                  # App handling staff, course, exam, result
├── templates/              # HTML templates
├── db.sqlite3              # Default database
├── manage.py
└── README.md
```

---

## 🙌 Contribution

Pull requests and suggestions are welcome! Feel free to fork the project and improve it.

---

## 📄 License

This project is licensed under the MIT License.
