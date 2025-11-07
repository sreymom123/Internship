# ប្រព័ន្ធគ្រប់គ្រងកម្មសិក្សា (Internship Management System)

A web-based platform built with Flask to manage internship programs, connecting students with partner companies.

## Features

### For Students
- Submit internship applications
- Track application status
- Download internship-related documents  
- Submit weekly progress reports
- Communicate with mentors

### For Administrators
- Manage student and company accounts
- Post new internship opportunities
- Monitor all internship processes
- Generate reports and statistics
- Handle system issues

## Tech Stack

- **Backend:** Python/Flask
- **Frontend:** HTML, TailwindCSS
- **Icons:** Font Awesome
- **Fonts:** Kantumruy Pro (for Khmer language support)

## Project Structure


Internship/
├── static/
│ ├── css/
│ │ └── main.css
│ └── images/
├── templates/
│ ├── admin_dashboard.html
│ ├── index.html
│ ├── login.html
│ ├── mentor_dashboard.html
│ ├── student_dashboard.html
│ └── test_connection.html
├── requirements.txt
└── app.py



## Getting Started

1. Clone the repository
2. Create a virtual environment:
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate