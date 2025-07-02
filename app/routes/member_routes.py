from flask import Blueprint
from app.controllers import member_controller

member_bp = Blueprint('member_bp', __name__, url_prefix='/members')

member_bp.route('', methods=['GET'])(member_controller.get_all_members)
member_bp.route('/<int:id_member>', methods=['GET'])(member_controller.get_member_by_id)
member_bp.route('', methods=['POST'])(member_controller.create_member)
member_bp.route('/<int:id_member>', methods=['PUT'])(member_controller.update_member)
member_bp.route('/<int:id_member>', methods=['DELETE'])(member_controller.delete_member)
