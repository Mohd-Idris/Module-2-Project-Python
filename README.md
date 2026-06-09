# Mohamed Idris - Personal Portfolio Website – Flask Project

A complete personal portfolio website built with Flask, using Jinja2 templating for consistent layout across all pages.

# 🎯 Project Overview

The goal of this project is to design and develop a responsive, accessible, and professional website. By using semantic HTML and custom CSS, Python, and Flask as backend framework.

# ✨ Features

• Standard Flask project structure

• Reusable layout via Jinja2 template inheritance

• Organized static assets

• Exact dependency versions for consistency

• Git-ready configuration

• Easy to customize and extend

# 🛠️ Technologies & Dependencies

• Python 3

• Flask 3.1.3 – Web framework

• Jinja2 3.1.6 – Templating engine

• HTML5 & CSS3 – Frontend structure and styling

• Other required packages: blinker, click, itsdangerous, MarkupSafe, Werkzeug

# Design Resources

I utilized these professional tools to enhance the UI/UX:

• Google Font: For all textual contents in the website (Poppins Font).

• Font Awesome: For scalable vector icons.

• Flaticon: For high-quality graphic assets.

• Color Hunt: For selecting the professional color palette.

📱 Responsive Design (Breakpoints)

The website is optimized for different screen sizes using the following CSS strategy:
• Tablet View: Optimized for screens with a max-width: 768px.
• Mobile View: Optimized for screens with a max-width: 528px.

# 📁 Project Structure

```text
FLASK-PROJECT/
├── static/ # Static assets
│ ├── css/
│ │ └── style.css # Main stylesheet
│ └── images/ # Website images
├── templates/ # HTML templates
│ ├── base.html # Base template (shared header/footer/nav)
│ ├── index.html # Home page
│ ├── about.html # About Me page
│ ├── skills.html # Skills page
│ ├── portfolio.html # Portfolio/Projects page
│ └── contact.html # Contact page
├── venv/ # Python virtual environment
├── .gitignore # Git ignored files/folders
├── app.py # Main Flask application
└── requirements.txt # Exact package versions
```

# 📄 Pages

• index.html – Homepage / introduction

• about.html – Personal background and bio

• skills.html – List of technical and professional skills

• portfolio.html – Showcase of work and projects

• contact.html – Contact information

• base.html – Reusable layout using Jinja2 inheritance

# 📦 Requirements (requirements.txt)

• blinker==1.9.0

• click==8.4.1

• Flask==3.1.3

• itsdangerous==2.2.0

• Jinja2==3.1.6

• MarkupSafe==3.0.3

• Werkzeug==3.1.8

# 🚀 How to Run

1. Activate Virtual Environment

## For Windows

1. venv\Scripts\activate
2. Install Dependencies : pip install -r requirements.txt
3. Run the App by writing python app.py
4. View in Browser : http://localhost:5000

## For macOS / Linux

1. source venv/bin/activate
2. Install Dependencies : pip install -r requirements.txt
3. Run the App by writing python app.py
4. View in Browser : Go to: http://localhost:5000

# 🚫 .gitignore Contents

• venv

• .idea/

• .vscode/

• **pycache**/

• dist/

• .coverage\*

• htmlcov/

• .tox/

• docs/\_build/

• .DS_Store
