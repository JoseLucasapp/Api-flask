from flask import Blueprint, Response, request
from models.teacher import db, Teacher
import json

app = Blueprint('teacher', __name__)


@app.route('/add', methods=['POST'])
def create():
    teacher = Teacher(request.form['name'], request.form['subject'])
    db.session.add(teacher)
    db.session.commit()
    return Response(response=json.dumps(teacher.to_dict()), status=200, content_type='application/json')


@app.route('/get')
@app.route('/get/<int:id>')
def get(id=-1):
    if id <= 0:
        rows = db.session.execute('select * from teacher').fetchall()
        result = [dict(r) for r in rows]
        return Response(response=json.dumps(result), status=200, content_type='application/json')

    row = db.session.execute(
        'select * from teacher WHERE id = {}'.format(id)).fetchone()
    return Response(response=json.dumps(dict(row)), status=200, content_type='application/json')


@app.route('/edit/<int:id>')
def edit(id):
    teacher = Teacher.query.get(id)
    if request.form['name'] is not None:
        teacher.name = request.form['name']
    if request.form['subject'] is not None:
        teacher.subject = request.form['subject']
    db.session.commit()
    return Response(response=json.dumps(teacher.to_dict()), status=200, content_type='application/json')


@app.route('/delete/<int:id>')
def delete(id):
    teacher = Teacher.query.get(id)
    db.session.delete(teacher)
    db.session.commit()
    return Response(response=json.dumps(teacher.to_dict()), status=200, content_type='application/json')
