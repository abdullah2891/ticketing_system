from flask_sqlalchemy import SQLAlchemy 


db = SQLAlchemy()

class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title =db.Column(db.String(100))
    description = db.Column(db.String(255))
    def __init__(self, title, description):
        self.title = title
        self.description = description


