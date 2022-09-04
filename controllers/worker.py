from flask import Blueprint, Response, request
from models.worker import db, Worker
import json

app = Blueprint('worker', __name__)


@app.route('/add', methods=['POST'])
def create():
    worker = Worker(request.form['name'], request.form['role'])
    db.session.add(worker)
    db.session.commit()
    return Response(response=json.dumps(worker.to_dict()), status=200, content_type='application/json')


@app.route('/get')
@app.route('/get/<int:id>')
def get(id=-1):
    if id <= 0:
        rows = db.session.execute('select * from worker').fetchall()
        result = [dict(r) for r in rows]
        return Response(response=json.dumps(result), status=200, content_type='application/json')

    row = db.session.execute(
        'select * from worker WHERE id = {}'.format(id)).fetchone()
    return Response(response=json.dumps(dict(row)), status=200, content_type='application/json')


@app.route('/edit/<int:id>')
def edit(id):
    worker = Worker.query.get(id)
    if request.form['name'] is not None:
        worker.name = request.form['name']
    if request.form['role'] is not None:
        worker.subject = request.form['role']
    db.session.commit()
    return Response(response=json.dumps(worker.to_dict()), status=200, content_type='application/json')


@app.route('/delete/<int:id>')
def delete(id):
    worker = Worker.query.get(id)
    db.session.delete(worker)
    db.session.commit()
    return Response(response=json.dumps(worker.to_dict()), status=200, content_type='application/json')
