from app.models.member import Member
from app.extensions import db
from app.schemas.member_schema import member_schema

def get_all():
    return Member.query.all()

def get_by_id(id_member):
    member = Member.query.get(id_member)
    if not member:
        abort(404, 'Membro não encontrado')
    return member

def create(data):
    member = member_schema.load(data)
    db.session.add(member)
    db.session.commit()
    return member

def update(id_member, data):
    member = get_by_id(id_member)
    for field in ['name', 'photo', 'biography', 
                    'contact_email', 'class_name', 
                    'lattes', 'linkedin']:
        if field in data:
            setattr(member, field, data[field])
    db.session.commit()
    return member

def delete(id_member):
    member = get_by_id(id_member)
    db.session.delete(member)
    db.session.commit()