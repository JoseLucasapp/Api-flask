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

    def to_dict(self, columns=[]):
        if not columns:
            return {"id": self.id, "name": self.name, "classRoom": self.classRoom, "age": self.age}
        else:
            return {"col": getattr(self, col) for col in columns}
