from app.extensions import db

class ShortCourse(db.Model):
    __tablename__ = 'short_course'

    id_workshop = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    event_description = db.Column(db.Text)
    lecturer = db.Column(db.String(45))
    location = db.Column(db.String(45))
    lenght_time = db.Column(db.Integer)
    cover_photo = db.Column(db.LargeBinary)
    registration_link = db.Column(db.Text)
    data_occurrence = db.Column(db.Date)
    time_occurrence = db.Column(db.Time)

    admin_id_admin = db.Column(db.Integer, db.ForeignKey('admin.id_admin'), nullable=False)
