from app.extensions import db

class Admin(db.Model):
    __tablename__ = 'admin'

    id_admin = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(45), nullable=False)
    created_time = db.Column(db.TIMESTAMP, nullable=False)

# Definir os relacionamentos depois
from app.models.event import Event
from app.models.member import Member
from app.models.workshop import Workshop
from app.models.short_course import ShortCourse

Admin.members = db.relationship('Member', backref='admin', lazy=True)
Admin.events = db.relationship('Event', backref='admin', lazy=True)
Admin.workshops = db.relationship('Workshop', backref='admin', lazy=True)
Admin.short_courses = db.relationship('ShortCourse', backref='admin', lazy=True)