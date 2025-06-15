from flask import Blueprint

workshop_bp = Blueprint('workshop', __name__)

@workshop_bp.route('/workshops')
def list_workshops():
    return {"msg": "Lista de workshops"}
