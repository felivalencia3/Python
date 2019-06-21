from flask import Blueprint, render_template
from flask_login import login_required, current_user

app = Blueprint('routes', __name__)


@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@app.route('/profile')
@login_required
def profile():
    return render_template("pages/profile.html", name=current_user.name)
