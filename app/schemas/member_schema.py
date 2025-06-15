from app.extensions import ma
from app.models.member import Member

class MemberSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Member
        load_instance = True
