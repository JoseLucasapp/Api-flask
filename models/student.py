from ..database.database import db


class Student(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150))
    classRoom = db.Column(db.String(150))
    age = db.Column(db.Integer)

    def __init__(self, name, classRoom, age):
        self.name = name
        self.classRoom = classRoom
        self.age = age
