from flask import Blueprint, render_template, request, redirect, url_for

app = Blueprint('app', __name__)

from models import Post, Category
from app import db


@app.route('/')
def index():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)


@app.route('/addpost', methods=['POST', 'GET'])
def add():
    content = request.form['content']
    category = Category(request.form['category'])

    post = Post(content, category)
    db.session.add(post)
    db.session.commit()

    return redirect(url_for('app.index'))