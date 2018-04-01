from app import db
import sqlalchemy.orm

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(140))

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = sqlalchemy.orm.relationship("Category", back_populates="post")

    def __init__(self, content, category):
        self.content = content
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.content


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    post = sqlalchemy.orm.relationship("Post", uselist=False, back_populates="category")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name