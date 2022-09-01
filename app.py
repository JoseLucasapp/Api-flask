from database.database import db
from flask import Flask
import os
from dotenv import load_dotenv

config = load_dotenv(".env")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')


@app.route('/')
def index():
    return '<h1>Home page</h1>'


if __name__ == '__main__':
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(debug=True)
