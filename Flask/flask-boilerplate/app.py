import logging
from functools import wraps
from logging import Formatter, FileHandler
from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_login import LoginManager, UserMixin, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from forms import *

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
from models import User
from auth import auth
from routes import app as views


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


db_session = db.session
app.register_blueprint(views)
app.register_blueprint(auth)


@app.errorhandler(500)
def internal_error(error):
    db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')
if __name__ == '__main__':
    app.run()
