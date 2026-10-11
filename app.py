# app.py
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# --- Data from Resume ---
RESUME_DATA = {
    "name": "Sankula Ashok",
    "title": "B.Com Computers Student | Aspiring Tech Professional",
    "contact": {
        "phone": "+91 81215 34763",
        "email": "syerriswami5@gmail.com",
        "linkedin": "linkedin.com/in/s-ashok-9753a2440",
        "location": "Tadipatri, India"
    },
    "summary": "Motivated B.Com Computers student currently pursuing the second year, with basic knowledge of C programming, prompt engineering, computer operations, and online research. A quick learner with patience, communication skills, and a responsible approach to teamwork. Seeking an entry-level or part-time opportunity to gain practical experience, learn new skills, and contribute reliably.",
    "education": [
        {
            "degree": "B.Com - Computers",
            "institution": "Currently pursuing 2nd year",
            "year": "Pursuing",
            "marks": "—"
        },
        {
            "degree": "Intermediate",
            "institution": "Government Degree College, Tadipatri",
            "year": "Completed",
            "marks": "765"
        },
        {
            "degree": "SSC",
            "institution": "Prakasam Municipal High School, Tadipatri",
            "year": "Completed",
            "marks": "323"
        }
    ],
    "skills": {
        "technical": [
            "Prompt engineering and AI-assisted information gathering",
            "C programming fundamentals",
            "Basic computer, smartphone, and internet skills",
            "Online research, information collection, and analysis",
            "Basic electrical components and hands-on mini project work",
            "Basic communication and customer-handling skills"
        ],
        "soft": [
            "Communication", "Leadership", "Patience", "Teamwork",
            "Time management", "Punctuality", "Responsibility",
            "Adaptability", "Willingness to learn"
        ]
    },
    "projects": [
        {
            "title": "Personal Portfolio",
            "description": "Created a portfolio to present personal details, skills, interests, and project work.",
            "icon": "fa-user-circle"
        },
        {
            "title": "Mini Remote-Controlled Car",
            "description": "Worked on a mini car project involving remote control and basic electrical components.",
            "icon": "fa-car"
        },
        {
            "title": "Waste Segregation Project",
            "description": "Participated in a project focused on separating waste materials to support better waste management.",
            "icon": "fa-recycle"
        }
    ],
    "additional": {
        "languages": ["Telugu", "English"],
        "interests": ["Learning new things", "Exploring technology", "Researching information", "Analyzing ideas"],
        "experience": "Fresher - no formal work experience",
        "dob": "15 July 2008",
        "gender": "Male"
    }
}

# --- Routes ---
@app.route('/')
def index():
    return render_template('index.html', data=RESUME_DATA)

@app.route('/api/contact', methods=['POST'])
def contact():
    """Simulated contact endpoint"""
    data = request.get_json()
    name = data.get('name', 'Anonymous')
    email = data.get('email', 'No email')
    message = data.get('message', 'No message')
    # In a real app, you would send an email or store in DB
    print(f"📩 Contact from {name} ({email}): {message}")
    return jsonify({"status": "success", "message": f"Thanks {name}! Your message has been received."})

@app.route('/api/skills')
def api_skills():
    """Return skills as JSON"""
    return jsonify(RESUME_DATA["skills"])

@app.route('/api/projects')
def api_projects():
    """Return projects as JSON"""
    return jsonify(RESUME_DATA["projects"])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)