from extensions import db

class auth(db.Model):
    __tablename__ = 'auth'
    
    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(100), nullable = True)

    last_name = db.Column(db.String(100), nullable = True)

    user_name = db.Column(db.String(50), nullable = True)

    email = db.Column(db.String(100), nullable = True)

    password = db.Column(db.String(100), nullable = True)