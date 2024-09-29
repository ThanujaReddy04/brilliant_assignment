from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)
# Database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    bio = db.Column(db.String(500), nullable=False)
    def __repr__(self):
        return f"<User {self.name}>"
# Home page route
@app.route('/')
def home():
    return render_template('home.html')
# Form page route
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        bio = request.form['bio']
        
        # Error handling for invalid inputs
        if not name or not age or not bio:
            flash("All fields are required!")
            return redirect(url_for('form'))
        try:
            age = int(age)
        except ValueError:
            flash("Invalid age! Please enter a number.")
            return redirect(url_for('form'))
        new_user = User(name=name, age=age, bio=bio)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('display'))
    
    return render_template('form.html')
# Display page route
@app.route('/display')
def display():
    users = User.query.all()
    return render_template('display.html', users=users)
# API endpoint to get all users data as JSON
@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_data = [{"name": user.name, "age": user.age, "bio": user.bio} for user in users]
    return jsonify(user_data)
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
        
