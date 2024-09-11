from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask import url_for
db = SQLAlchemy()


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    num_of_pages = db.Column(db.Integer, nullable=True)
    image = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(5000), nullable=True)
    
    
    def __str__(self):
        return self.name
    
    
    @property
    def image_url(self):
        return url_for('static', filename=f"books/images/{self.image}")
    