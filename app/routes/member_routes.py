from flask import Blueprint

member_bp = Blueprint('member', __name__)

@member_bp.route('/members')
def get_members():
    return {"msg": "Lista de membros"}
