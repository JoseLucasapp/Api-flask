import json
from flask import Blueprint, Response, request
from models.student import db, Student

app = Blueprint('student', __name__)


@app.route('/add', methods=['POST'])
def add():
    student = Student(
        request.form['name'], request.form['classRoom'], request.form['age']
    )
    db.session.add(student)
    db.session.commit()
    return Response(response=json.dumps(student.to_dict()), status=200, content_type='application/json')


@app.route('/get', methods=['GET'])
@app.route('/get/<int:id>', methods=['GET'])
def get(id=-1):
    if (id <= 0):
        rows = db.session.execute('select * from student').fetchall()
        result = [dict(r) for r in rows]
        return Response(response=json.dumps(result), status=200, content_type='application/json')

    row = db.session.execute('select * from student where id = {}'.format(id))
    return Response(response=json.dumps(dict(row)), status=200, content_type='application/json')


@app.route('/edit/<int:id>')
def edit(id):
    student = Student.query.get(id)
    if request.form['name'] is not None:
        student.name = request.form['name']
    if request.form['age'] is not None:
        student.age = request.form['age']
    if request.form['classRoom'] is not None:
        student.classRoom = request.form['classRoom']
    db.session.commit()
    return Response(response=json.dumps(student.to_dict()), status=200, content_type='application/json')


@app.route('/delete/<int:id>')
def delete(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return Response(response=json.dumps(student.to_dict()), status=200, content_type='application/json')
