from app.extensions import db

class Member(db.Model):
    __tablename__ = 'member'

    id_member = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    photo = db.Column(db.LargeBinary)
    biography = db.Column(db.Text)
    contact_email = db.Column(db.String(45))
    class_name = db.Column(db.String(45))
    lattes = db.Column(db.Text)
    linkedin = db.Column(db.Text)

    admin_id_admin = db.Column(db.Integer, db.ForeignKey('admin.id_admin'), nullable=False)
