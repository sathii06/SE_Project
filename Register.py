from turtle import clear
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask import session
from datetime import datetime

import hashlib 
import logging
current_utc_time = datetime.utcnow()

app = Flask(__name__, template_folder="Login_page_for_sttudent")
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql9657372:WhwX8ETu5i@sql9.freesqldatabase.com/sql9657372'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ABCabcDEFdef123'

db = SQLAlchemy(app)

# Define the User_Credentials model without an id column
class User_Registration(db.Model):
    __tablename__ = 'User_Registration'  # Specify the exact table name
    First_name= db.Column(db.String(255), nullable=False)
    Last_name= db.Column(db.String(255), nullable=False)
    Email = db.Column(db.String(255), primary_key=True) 
    Clark_ID = db.Column(db.String(9), nullable=False)
    Intake_year = db.Column(db.Integer, nullable=False)
    Intake_term=db.Column(db.String(6), nullable=False)
    Pronouns= db.Column(db.String(255), nullable=False)
    Phone = db.Column(db.String(10), nullable=False)
    Password = db.Column(db.String(255), nullable=False)

class Course_Details(db.Model):
     __tablename__ = 'Course_Details'
     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
     Email=db.Column(db.String(255), nullable=False)
     Course_Name= db.Column(db.String(255), nullable=False)
     Course_Code= db.Column(db.String(255), nullable=False)
     Faculty_Email = db.Column(db.String(255), nullable=False) 
     Enrollment_Year = db.Column(db.Integer, nullable=False)
     Enrollment_Term = db.Column(db.String(6), nullable=False)
     Grade=db.Column(db.String(2), nullable=False)

class TA_Applications(db.Model):
    __tablename__ = 'TA_Applications'
    A_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    A_Email = db.Column(db.String(255), nullable=False)
    A_Course_name = db.Column(db.String(255), nullable=False)
    A_Course_code = db.Column(db.String(255), nullable=False)
    A_Prev_taken = db.Column(db.String(255), nullable=False)
    A_Total_hours = db.Column(db.Integer, nullable=False)
    A_Experience = db.Column(db.String(255), nullable=False)
    A_Grade = db.Column(db.String(255), nullable=False)
    A_Availability = db.Column(db.String(255), nullable=False)
    A_Status = db.Column(db.String(10), nullable=False)
    A_Submission_date = db.Column(db.DateTime, default=datetime.utcnow)


def hash_password(password):
    salt = "SEPROJECT2023"  # Replace with a secure random salt
    password = password + salt
    return hashlib.sha256(password.encode()).hexdigest()


@app.route('/')
def index():
    return render_template('Student_login.html')



@app.route('/Registration_page.html')
def registration_page1():
    return render_template('Registration_page.html')

@app.route('/Next_page.html')
def registration_page2():
    return render_template('Next_page.html')

@app.route('/Student_login.html')
def login_page():
    return render_template('Student_login.html')

@app.route('/ta.html')
def student_home():
    username = session.get('username')
    return render_template('ta.html', username=username)

@app.route('/TA_Apply.html')
def apply_TA():
    username = session.get('username')
    return render_template('TA_Apply.html', username=username)

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['Username']
        pwd = request.form['Password']
        hash_pwd = hash_password(pwd)

        user = User_Registration.query.filter_by(Email=email).first()

        if user:
            if hash_pwd == user.Password:
                flash("User validated, Login Successful")
                session['username'] = user.Email
                return redirect(url_for('student_home'))
            else:
                flash("User validated, Login Failed - Invalid Password")

        else:
            flash("User not found")

        return redirect(url_for('index'))


@app.route('/register1', methods=['GET', 'POST'])
def register1():

    First_name = None
    Last_name = None
    Pronouns = None
    Email = None
    Clark_ID = None
    Intake_year = None
    Intake_term = None
    Phone = None
    Password = None

    if request.method == 'POST':
        First_name = request.form.get('First_name')
        Last_name = request.form.get('Last_name')
        Pronouns = request.form.get('Pronouns')
        Email = request.form.get('Email')
        Clark_ID = request.form.get('Clark_ID')
        Intake_year = request.form.get('Intake_year')
        Intake_term = request.form.get('Intake_term')
        Phone = request.form.get('Phone')
        Pwd = request.form.get('Password')
        Password = hash_password(Pwd)

        return redirect(url_for('register2', First_name=First_name, Last_name=Last_name, Pronouns=Pronouns, Email=Email, Clark_ID=Clark_ID, Intake_year=Intake_year, Intake_term=Intake_term, Phone=Phone, Password=Password))
        

@app.route('/register2', methods=['GET', 'POST'])
def register2():
    #if request.method == 'POST':
    First_name = request.args.get('First_name')
    Last_name = request.args.get('Last_name')
    Pronouns = request.args.get('Pronouns')
    Email = request.args.get('Email')
    Clark_ID = request.args.get('Clark_ID')
    Intake_year = request.args.get('Intake_year')
    Intake_term = request.args.get('Intake_term')
    Phone = request.args.get('Phone')
    Password= request.args.get('Password')

    return render_template('Next_page.html', First_name=First_name, Last_name=Last_name, Pronouns=Pronouns, Email=Email, Clark_ID=Clark_ID, Intake_year=Intake_year, Intake_term=Intake_term, Phone=Phone, Password=Password)

@app.route('/final', methods=['GET', 'POST'])
def final():
    
    First_name = request.form.get('First_name')
    Last_name = request.form.get('Last_name')
    Pronouns = request.form.get('Pronouns')
    Email = request.form.get('Email')
    Clark_ID = request.form.get('Clark_ID')
    Intake_year = request.form.get('Intake_year')
    Intake_term = request.form.get('Intake_term')
    Phone = request.form.get('Phone')
    Password= request.form.get('Password')

    user=User_Registration(First_name=First_name, Last_name=Last_name, Pronouns=Pronouns, Email=Email, Clark_ID=Clark_ID, Intake_year=Intake_year, Intake_term=Intake_term, Phone=Phone, Password=Password)
    
    try:
            db.session.add(user)
            db.session.commit()
            #flash('User registered successfully', 'success')
    except Exception as e:
            flash(f'Error: {str(e)}', 'error')
            db.session.rollback()
    
    if request.method == 'POST':
        course_names = request.form.getlist('A[]')
        course_codes = request.form.getlist('B[]')
        faculty_emails = request.form.getlist('C[]')
        enroll_years = request.form.getlist('D[]')
        terms = request.form.getlist('E[]')
        grades = request.form.getlist('F[]')

    for i in range(len(course_names)):
            Email = request.form.get('Email')
            add=Course_Details(Email=Email, Course_Name=course_names[i], Course_Code=course_codes[i], Faculty_Email=faculty_emails[i], Enrollment_Year=enroll_years[i], Enrollment_Term=terms[i], Grade=grades[i])
            db.session.add(add)
            db.session.commit()

    return redirect(url_for('index'))


@app.route('/profile')
def profile():
    username = session.get('username')
    user = User_Registration.query.filter_by(Email=username).first()
    print(user)  # Add this line for debugging
    if user:
        return render_template('profile.html', user=user)
    else:
        flash('User not found', 'error')
        return redirect(url_for('edit_profile'))


@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    user = User_Registration.query.first()
    if request.method == 'POST':
        user.First_name = request.form['First_name']
        user.Last_name = request.form['Last_name']
        user.Email = request.form['Email']
        user.Clark_ID = request.form['Clark_ID']
        user.Intake_year = request.form['Intake_year']
        user.Intake_term = request.form['Intake_term']
        user.Pronouns = request.form['Pronouns']
        user.Phone = request.form['Phone']
        db.session.commit()
        return redirect(url_for('profile'))
    return render_template('edit_profile.html', user=user)

@app.route('/applyTA', methods=['GET', 'POST'])
def applyTA():
    A_Email = session.get('username')
    if request.method == 'POST':
       
        A_Course_name = request.form.get('A_Course_name')
        A_Course_code = request.form.get('A_Course_code')
        A_Prev_taken = request.form.get('A_Prev_taken')
        A_Total_hours = request.form.get('A_Total_hours')
        A_Experience = request.form.get('A_Experience')
        A_Grade = request.form.get('A_Grade')
        A_Availability = request.form.get('A_Availability')
        TA=TA_Applications(A_Email=A_Email, A_Course_name = A_Course_name, A_Course_code = A_Course_code, A_Prev_taken = A_Prev_taken, A_Total_hours = A_Total_hours, A_Experience = A_Experience, A_Grade = A_Grade, A_Availability = A_Availability, A_Status="Submitted")
        db.session.add(TA)
        db.session.commit()
    return redirect(url_for('student_home'))

@app.route('/display_data')
def display_data():
    email = session.get('username')
    # Fetch data from the database table based on the user's email
    data = TA_Applications.query.filter_by(A_Email=email).all()
    return render_template('Application_status.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)