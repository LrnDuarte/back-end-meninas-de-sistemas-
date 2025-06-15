from flask import Blueprint

short_course_bp = Blueprint('short_course', __name__)

@short_course_bp.route('/short-courses')
def list_short_courses():
    return {"msg": "Lista de cursos rápidos"}
