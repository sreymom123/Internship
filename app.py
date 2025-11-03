import os
import threading
import webbrowser
from flask import Flask, render_template, request, redirect, url_for

BASE_DIR = os.path.dirname(__file__)

# កំណត់ path សម្រាប់ templates និង static files
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
if not os.path.isdir(TEMPLATE_DIR):
    alt = os.path.join(BASE_DIR, 'Internship', 'templates')
    if os.path.isdir(alt):
        TEMPLATE_DIR = alt

STATIC_DIR = os.path.join(BASE_DIR, 'static')
if not os.path.isdir(STATIC_DIR):
    alt_static = os.path.join(BASE_DIR, 'Internship', 'static')
    if os.path.isdir(alt_static):
        STATIC_DIR = alt_static

# បង្កើត Flask app
app = Flask(__name__, static_folder=STATIC_DIR, template_folder=TEMPLATE_DIR)

# កំណត់ routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/student_dashboard')
def student_dashboard():
    return render_template('student_dashboard.html')

@app.route('/admin')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route('/mentor')
def mentor_dashboard():
    return render_template('mentor_dashboard.html')

if __name__ == '__main__':
    url = 'http://127.0.0.1:5000'
    print(f'កំពុងចាប់ផ្តើម server នៅ: {url}')
    threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    app.run(debug=True, use_reloader=False)