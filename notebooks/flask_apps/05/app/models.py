from app import db
from datetime import datetime

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120), index=True, unique=True)
    counts = db.relationship('Counts', backref='source', lazy='dynamic')

    def __repr__(self):
        return '<Data {}>'.format(self.text)

class Counts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    counts = db.Column(db.Integer, index=True, unique=True)
    count_id = db.Column(db.Integer, db.ForeignKey('data.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Counts {}>'.format(self.counts)

