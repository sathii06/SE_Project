from turtle import clear
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import hashlib 
import logging

app = Flask(__name__, template_folder="Login_page_for_sttudent")
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql3655181:aqKjlbdgb8@sql3.freesqldatabase.com/sql3655181'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ABCabcDEFdef123'

db = SQLAlchemy(app)

class User_Registration(db.Model):
    __tablename__ = 'User_Registration'  # Specify the exact table name
    First_name= db.Column(db.String(255), nullable=False)
    Last_name= db.Column(db.String(255), nullable=False)
    Email = db.Column(db.String(255), primary_key=True) 
    Clark_ID = db.Column(db.String(9), nullable=False)
    Intake_year = db.Column(db.Integer, nullable=False)
    Intake_term=db.Column(db.String(6), nullable=False)
    Pronouns= db.Column(db.String(255), nullable=False)
    Phone = db.Column(db.Integer, nullable=False)
    Password = db.Column(db.String(255), nullable=False)



@app.route('/profile')
def profile():
    user = User_Registration.query.filter_by(Email="test@clarku.edu").first()
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

if __name__ == '__main__':
    app.run(debug=True)


