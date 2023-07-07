from extensions import db, login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False, unique=True)
    password = db.Column(db.String(255), nullable = False)
    

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


    def check_password(self, password):
        return check_password_hash(self.password, password)


    def __repr__(self):
        return self.name


    def save(self):
        db.session.add(self)
        db.session.commit()



