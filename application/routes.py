# SERVICE

# Capture les appels aux API
# Ne renvoie JAMAIS de vues mais du JSON

import json
from flask import current_app as app, request, Response, jsonify
from .submission import Submission
import time

@app.route('/')
def hello_world():
    return 'Hello world !'

@app.route('/dashboard', methods=['GET'])
def dashboard():
    # Sur base de l'email, retrouver la soumission et la renvoyer
    request_data = request.get_json()
    print(request_data)
    if request_data is not None:
        email = request_data.get('postulant_email', None)
        if email is not None:
            sub =  Submission.find_sumbission_by_postulant_email(email)
            if sub is not None:
                return Submission.json(sub)
    return {}

@app.route('/submissions', methods=['POST'])
def add_submission():
    request_data = request.get_json() 
    Submission.add_submission(
        request_data["postulant_email"],
        request_data["postulant_firstname"],
        request_data["postulant_lastname"],
        request_data["postulant_middlename"],
        request_data.get("postulant_birthday", None)
        )
    response = Response("Sumbmission added", 201, mimetype='application/json')
    return response


@app.route('/submissions', methods=['GET'])
def get_movies():
    return jsonify({'Submissions': Submission.get_all_submissions()})

@app.route('/submissions/<subm_id>', methods=['GET'])
def get_submission(subm_id=0):
    subm = Submission.get_submission(subm_id)
    return jsonify(subm)

@app.route('/submissions/<subm_id>/validate', methods=['POST'])
def validate_submission(subm_id=0):
    Submission.validate(subm_id)
    time.sleep(3)
    return Response("Registration validated", 201, mimetype="application/json")
