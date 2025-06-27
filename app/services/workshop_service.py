from app.models.workshop import Workshop
from app.extensions import db
from app.schemas import workshop_schema

def get_all():
    return Workshop.query.all()

def get_by_id(id_workshop):
    workshop = Workshop.query.get(id_workshop)
    if not workshop:
        abort(404, 'Workshop não encontrado')
    return workshop

def create(data):
    workshop = workshop_schema.load(data)
    db.session.add(workshop)
    db.session.commit()
    return workshop

def update(id_workshop, data):
    workshop = get_by_id(id_workshop)
    for field in ['title', 'event_description', 'lecturer', 
                    'location', 'lenght_time', 'cover_photo', 
                    'registration_link', 'data_occurrence', 
                    'time_occurrence']:
        if field in data:
            setattr(workshop, field, data[field])
    db.session.commit()
    return workshop

def delete(id_workshop):
    workshop = get_by_id(id_workshop)
    db.session.delete(workshop)
    db.session.commit()
