from ..database.database import db


class Worker(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150))
    role = db.Column(db.String(150))

    def __init__(self, name, role):
        self.name = name
        self.role = role
