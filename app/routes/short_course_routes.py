from flask import Blueprint
from app.controllers import short_course_controller

short_course_bp = Blueprint('short_course_bp', __name__, url_prefix='/short_course')

short_course_bp.route('', methods=['GET'])(short_course_controller.get_all_short_course)
short_course_bp.route('/<int:id_short_course>', methods=['GET'])(short_course_controller.get_short_course_by_id)
short_course_bp.route('', methods=['POST'])(short_course_controller.create_short_course)
short_course_bp.route('/<int:id_short_course>', methods=['PUT'])(short_course_controller.update_short_course)
short_course_bp.route('/<int:id_short_course>', methods=['DELETE'])(short_course_controller.delete_short_course)
