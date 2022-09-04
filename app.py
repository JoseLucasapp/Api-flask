from database.database import db
from flask import Flask
import os
from dotenv import load_dotenv
from controllers.teacher import app as teacher_controller
from controllers.student import app as student_controller
from controllers.worker import app as worker_controller

config = load_dotenv(".env")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')

app.register_blueprint(teacher_controller, url_prefix='/teacher/')
app.register_blueprint(student_controller, url_prefix='/student/')
app.register_blueprint(worker_controller, url_prefix='/worker/')


@app.route('/')
def index():
    return '<h1>Home page</h1>'


if __name__ == '__main__':
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(debug=True)
