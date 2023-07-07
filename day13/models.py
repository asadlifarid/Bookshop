# butun databse elaqelerimiz burda bas verecek;

from extensions import db
from app import app
from datetime import datetime

# SQLAlchemy'ye uygun table'lar yaradiriq;

class Language(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    languages = db.Column(db.String(255))
    bookss = db.relationship('Book', backref = 'language')

    
    def __init__(self, languages):
        self.languages = languages
    

    def __repr__(self):
        return self.languages


    def save(self):
        db.session.add(self)
        db.session.commit()




class Genre(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    genre = db.Column(db.String(255))
    books = db.relationship('Book', backref = 'genre')


    def __init__(self, genre):
        self.genre = genre
    

    def __repr__(self):
        return self.genre


    def save(self):
        db.session.add(self)
        db.session.commit()


class Contact(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    message = db.Column(db.String(255))
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    book_id = db.Column(db.ForeignKey('book.id'))
    

    def __init__(self, name, email, message, book_id):
        self.name = name
        self.email = email
        self.message = message
        self.book_id = book_id
        


    def __repr__(self):
        return self.name


    def save(self):
        db.session.add(self)
        db.session.commit()





class Book(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    author = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float())
    img_url = db.Column(db.String(255), index=True)
    description = db.Column(db.String(255), nullable=False)
    stock = db.Column(db.Integer())
    publisher = db.Column(db.String(255))
    lang_id = db.Column(db.Integer(), db.ForeignKey('language.id'), nullable=False)
    genre_id = db.Column(db.Integer(), db.ForeignKey('genre.id'), nullable=False)
    

    
    def __init__(self, name, author, price, img_url, description, stock, publisher, lang_id, genre_id, contact_id):
        self.name = name
        self.author = author
        self.price = price
        self.img_url = img_url
        self.description = description
        self.stock = stock
        self.publisher = publisher
        self.lang_id = lang_id
        self.genre_id = genre_id
        self.contact_id = contact_id
        
        



    def __repr__(self):
        return self.name



    def save(self):
        db.session.add(self)
        db.session.commit()

