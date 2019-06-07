from werkzeug.exceptions import abort
from flask import Blueprint, render_template, flash, url_for, redirect, request, g
from flaskr.auth import login_required
from flaskr.db import get_db


def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user ON p.author_id = user.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()
    if post is None:
        abort(404, 'Post id {} does not exist'.format(id))
    if check_author and post['author_id'] != g.user['id']:
        abort(403)
    return post


app = Blueprint('blog', __name__)


@app.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id ORDER by created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)


@app.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None
        if not title:
            error = 'Title is Required'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?,?,?)', (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('index'))
    return render_template('blog/create.html')
