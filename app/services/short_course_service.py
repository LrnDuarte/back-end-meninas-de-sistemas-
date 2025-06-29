from app.models.short_course import ShortCourse
from app.extensions import db
from app.schemas.short_course_schema import ShortCourseSchema

def get_all():
    return ShortCourse.query.all()

def get_by_id(id_short_course):
    short_course = ShortCourse.query.get(id_short_course)
    if not short_course:
        abort(404, 'Minicurso não encontrado')
    return short_course

def create(data):
    short_course = ShortCourseSchema.load(data)
    db.session.add(short_course)
    db.session.commit()
    return short_course

def update(id_short_course, data):
    short_course = get_by_id(id_short_course)
    for field in ['title', 'event_description', 
                'lecturer', 'location', 'lenght_time', 
                'cover_photo', 'registration_link', 
                'data_occurrence', 'time_occurrence']:
        if field in data:
            setattr(short_course, field, data[field])
    db.session.commit()
    return short_course

def delete(id_short_course):
    short_course = get_by_id(id_short_course)
    db.session.delete(short_course)
    db.session.commit()