from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    deadline = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password", "danger")
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists. Please choose another.", "warning")
            return redirect(url_for("register"))

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/dashboard")
@login_required
def dashboard():
    goals = Goal.query.filter_by(user_id=current_user.id).all()
    return render_template("dashboard.html", goals=goals)

@app.route("/add_goal", methods=["POST"])
@login_required
def add_goal():
    title = request.form.get("title")
    deadline = request.form.get("deadline")
    new_goal = Goal(title=title, deadline=deadline, user_id=current_user.id)
    db.session.add(new_goal)
    db.session.commit()
    return redirect(url_for("dashboard"))



@app.route("/toggle_goal", methods=["POST"])
@login_required
def toggle_goal():
    goal_id = request.form.get("goal_id")
    goal = Goal.query.filter_by(id=goal_id, user_id=current_user.id).first()

    if goal:
        goal.completed = not goal.completed  # Toggle True/False
        db.session.commit()

    return redirect(url_for("dashboard"))



@app.route("/remove_goal", methods=["POST"])
def remove_goal():
    title = request.form.get("title")
    deadline = request.form.get("deadline")
    # Find the goal matching title, deadline, and current user
    goal_to_remove = Goal.query.filter_by(  #goal represents goals table in your database
        title=title,                        #.query start builiding query using sqlachemy(hey database i want to search in goal table)
        deadline=deadline,
        user_id=current_user.id
    ).first() #.first() return the first matching goal

    if goal_to_remove:
        db.session.delete(goal_to_remove)
        db.session.commit()

    return redirect(url_for("dashboard"))


#  THIS IS THE KEY PART!
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create site.db if it doesn’t exist
    app.run(debug=True)
