from flask import Blueprint

event_bp = Blueprint('event', __name__)

@event_bp.route('/events')
def list_events():
    return "Lista de eventos"
