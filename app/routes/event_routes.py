from flask import Blueprint
from app.controllers import event_controller

event_bp = Blueprint('event_bp', __name__, url_prefix='/events')

event_bp.route('', methods=['GET'])(event_controller.get_all_events)
event_bp.route('/<int:id_event>', methods=['GET'])(event_controller.get_event_by_id)
event_bp.route('', methods=['POST'])(event_controller.create_event)
event_bp.route('/<int:id_event>', methods=['PUT'])(event_controller.update_event)
event_bp.route('/<int:id_event>', methods=['DELETE'])(event_controller.delete_event)

