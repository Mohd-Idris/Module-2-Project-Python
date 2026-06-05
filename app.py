from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "MySecretKey123789"


# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Skills Data
my_skills = [
    {
        "name": "HTML",
        "image": "html.png",
        "percentage": 70
    },
    {
        "name": "CSS",
        "image": "css.png",
        "percentage": 50
    },
    {
        "name": "JavaScript",
        "image": "js.png",
        "percentage": 0
    },
    {
        "name": "C#",
        "image": "csharp.png",
        "percentage": 20
    },
    {
        "name": "Python",
        "image": "python.png",
        "percentage": 85
    },
    {
        "name": "GitHub",
        "image": "github.png",
        "percentage": 40
    }
    # {
    #     "name": "SQL",
    #     "image": "sql.png",
    #     "percentage": 10
    # },
    # {
    #     "name": "Bootstrap",
    #     "image": "bootstrap.png",
    #     "percentage": 30
    # },
    # {
    #     "name": "Java",
    #     "image": "java.png",
    #     "percentage": 55
    # }
    
]

# Portfolio Data
my_portfolio = [
    {
        "title": "HTML Project",
        "description": "This is a simple HTML project that demonstrates my ability to create a basic webpage using HTML.",
        "image": "html.png",
        "link": "https://mohd-idris.github.io/Personal-Website---Project-1/",
        "status": "Completed",
        "class": "Done"
        
    },
    {
        "title": "Python Project",
        "description": "This is a simple Python project that demonstrates my ability to write efficient code.",
        "image": "python.png",
        "link": "#",
        "status": "In Progress",
        "class": "working-on"
    },
    {
        "title": "JavaScript Project",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias veniam.",
        "image": "coming-soon-3.png",
        "link": "#",
        "status": "Not Started Yet",
        "class": "None"
    }
    # {
    #     "title": "C# Project",
    #     "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias veniam.",
    #     "image": "coming-soon-3.png",
    #     "link": "#",
    #     "status": "Not Started"
    #     "class": "None"
    # },
    # {
    #     "title": "GitHub Project",
    #     "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias veniam.",
    #     "image": "coming-soon-1.png",
    #     "link": "#",
    #     "status": "Not Started"
    #     "class": "None"
    # },
    # {
    #     "title": "SQL Project",
    #     "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestias veniam.",
    #     "image": "coming-soon-2.png",
    #     "link": "#",
    #     "status": "Not Started"
    #     "class": "None"
    # }
]


# Project Routes

@app.route('/')
def home():
    return render_template('index.html', title ='Home Page')

@app.route('/about')
def about():
    return render_template('about.html', title ='About Page')

@app.route('/skills')
def skills():
    return render_template('skills.html', title ='Skills Page', skills=my_skills)

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title ='Portfolio Page', portfolios=my_portfolio)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        error_messages = []
        if not name:
            error_messages.append("Name is required.")
        if not email:
            error_messages.append("Email is required.")
        if not message:
            error_messages.append("Message is required.")       

        if error_messages:
            return render_template(
                "contact.html", title="Contact Us Page", errors=error_messages, name=name, email=email, message=message
                )


        flash('Your message has been sent successfully!')
        return redirect('/contact')

    return render_template(
        'contact.html', title='Contact Us Page', error_messages =[], name="", email="", message=""
    )

if __name__ == '__main__':
    app.run(debug = True)