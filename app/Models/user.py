from app.extension import db

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String,nullable=False)
    email=db.Column(db.String,nullable=False)
    password=db.Column(db.String,nullable=False)
    role=db.Column(db.String,nullable=False,default='user')

    def save(self):
        db.session.add(self)
        db.session.commit()