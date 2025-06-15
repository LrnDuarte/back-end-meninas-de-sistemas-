from flask import request, jsonify
from app.services import admin_service
from app.schemas.admin_schema import admin_schema, admins_schema

def get_all_admins():
    admins = admin_service.get_all()
    return admins_schema.jsonify(admins)

def get_admin_by_id(id_admin):
    admin = admin_service.get_by_id(id_admin)
    return admin_schema.jsonify(admin)

def create_admin():
    data = request.get_json()
    admin = admin_service.create(data)
    return admin_schema.jsonify(admin), 200

def update_admin(id_admin):
    data = request.get_json()
    admin = admin_service.update(id_admin, data)
    return admin_schema.jsonify(admin)

def delete_admin(id_admin):
    admin = admin_service.delete(id_admin)
    return '', 200
    