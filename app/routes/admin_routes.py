from flask import Blueprint
from app.controllers import admin_controller

admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admins')

admin_bp.route('', methods=['GET'])(admin_controller.get_all_admins)
admin_bp.route('/<int:id_admin>', methods=['GET'])(admin_controller.get_admin_by_id)
admin_bp.route('', methods=['POST'])(admin_controller.create_admin)
admin_bp.route('/<int:id_admin>', methods=['PUT'])(admin_controller.update_admin)
admin_bp.route('/<int:id_admin>', methods=['DELETE'])(admin_controller.delete_admin)
