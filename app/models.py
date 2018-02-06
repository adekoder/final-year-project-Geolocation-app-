from datetime import datetime
from . import db

class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.String(20), unique=True, nullable=False, index=True)
    location_name = db.Column(db.String(255), nullable=False)
    location_alias = db.Column(db.String(30), nullable=True)
    coordinate = db.Column(db.String(255), nullable=False, unique=True)
    category_id = db.Column(db.String(50), db.ForeignKey('categories.category_id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return "<Location : %s (%s) >" % self.location_id,self.coordinate

    

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.String(50), unique=True, nullable=False)
    category_name = db.Column(db.String(255), nullable=False)
    locations = db.relationship('Location', backref='categories', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return "<Category : %s (%s)>" % self.category_id, self.category_name