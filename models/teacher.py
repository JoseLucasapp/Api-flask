from ..database.database import db


class Teacher(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150))
    subject = db.Column(db.String(150))

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
