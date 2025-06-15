from app.extensions import ma
from app.models.admin import Admin
from app.schemas.member_schema import MemberSchema

class AdminSchema(ma.SQLAlchemyAutoSchema):
    members = ma.Nested(MemberSchema, many=True)

    class Meta:
        model = Admin
        load_instance = True

admin_schema = AdminSchema()
admins_schema = AdminSchema(many=True)
