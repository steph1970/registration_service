# MODELE

# Contient s informations de modélisation des concepts (persistance), de la manière de les utiliser (logique métier)

from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from . import db 

class Submission(db.Model):
    __tablename__ = 'sumbission'  
    id = db.Column(db.Integer, primary_key=True) 
    dtg_created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    dtg_submit = db.Column(db.DateTime)
    postulant_firstname = db.Column(db.String, nullable=False)
    postulant_lastname = db.Column(db.String, nullable=False)
    postulant_middlename = db.Column(db.String)
    postulant_birthday = db.Column(db.Date)
    postulant_email = db.Column(db.String, nullable=False)
    is_validated = db.Column(db.Boolean, default=False)

    def json(self):
        return {
            'postulant_firstname': self.postulant_firstname,
            'postulant_lastname': self.postulant_lastname,
            'postulant_middlename': self.postulant_middlename,
            'postulant_birthday': self.postulant_birthday,
            'postulant_email': self.postulant_email,
            'id': self.id,
            'is_validated': self.is_validated,
            }

    def add_submission(postulant_email, postulant_firstname, postulant_lastname, postulant_middlename, postulant_birthday):
        submission = Submission(
            postulant_email=postulant_email,
            postulant_firstname=postulant_firstname,
            postulant_lastname=postulant_lastname,
            postulant_middlename=postulant_middlename,
            postulant_birthday=postulant_birthday,
            )
        db.session.add(submission)
        db.session.commit() 

    def validate(id_int):
        subm = Submission.query.filter(Submission.id==id_int).first()
        print(subm.__dict__)
        print(type(subm))
        print(subm.is_validated)
        is_already_validated = subm.is_validated
        subm.is_validated = not is_already_validated
        db.session.commit()

    def find_sumbission_by_postulant_email(postulant_email):
        sub = Submission.query.filter(Submission.postulant_email == postulant_email)
        if sub is not None:
            return Submission.json(sub)
        return {}

    def get_all_submissions():
        return [Submission.json(submission) for submission in Submission.query.all()]

    def get_submission(id):
        try:
            id_int = int(id)
        except ValueError as e:
            id_int = 0
        try :
            sub =  Submission.query.filter(Submission.id==id_int).first()
            if sub is not None:
                return Submission.json(sub)
            return {}
        except Exception as e:
            return {}
