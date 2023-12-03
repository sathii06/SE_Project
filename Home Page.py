from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql9649250:SFNkbWKz6t@sql9.freesqldatabase.com/sql9649250'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mail = db.Column(db.String(255), nullable=False)
    A = db.Column(db.String(255), nullable=False)
    B = db.Column(db.String(255), nullable=False)
    C = db.Column(db.String(255), nullable=False)

@app.route('/')
def index():
    # Query the database to retrieve data
    data = test.query.with_entities(test.mail, test.A, test.B, test.C).all()
    return render_template('Update Profile.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
