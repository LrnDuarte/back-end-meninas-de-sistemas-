from app.models.event import Event
from app.extensions import db
from app.schemas.event_schema import event_schema

def get_all():
    return Event.query.all()

def get_by_id(id_event):
    event = Event.query.get(id_event)
    if not event:
        abort(404, 'Evento não encontrado')
    return event

def create(data):
    event = event_schema.load(data)
    db.session.add(admin)
    db.session.commit()
    return event

def update(id_event, data):
    event = get_by_id(id_event)
    for field in ['title', 'event_description', 'organizer', 'location', 'lenght_time', 'cover_photo', 'registration_link', 'data_occurrence', 'time_occurrence']:
        if field in data:
            setattr(event, field, data[field])
    db.session.commit()
    return event

def delete(id_event):
    event = get_by_id(id_event)
    db.session.delete(event)
    db.session.commit()