from flask import Blueprint
from app.controllers import workshop_controller

workshop_bp = Blueprint('workshop_bp', __name__, url_prefix='/workshop')

workshop_bp.route('', methods=['GET'])(workshop_controller.get_all_workshop)
workshop_bp.route('/<int:id_workshop>', methods=['GET'])(workshop_controller.get_workshop_by_id)
workshop_bp.route('', methods=['POST'])(workshop_controller.create_worhshop)
workshop_bp.route('/<int:id_workshop>', methods=['PUT'])(workshop_controller.update_workshop)
workshop_bp.route('/<int:id_workshop>', methods=['DELETE'])(workshop_controller.delete_workshop)
