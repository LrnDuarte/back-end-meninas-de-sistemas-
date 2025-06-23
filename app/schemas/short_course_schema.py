from app.models.short_course import ShortCourse
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

class ShortCourseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ShortCourse
        load_instance = True
        include_fk = True

    id_workshop = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    event_description = fields.Str(required=True)
    lecturer = fields.Str(required=True)
    location = fields.Str(required=True)
    lenght_time = fields.Int(required=True)
    cover_photo = fields.Raw(allow_none=True)
    registration_link = fields.Str(required=True)
    data_occurrence = fields.Date(required=True)
    time_occurrence = fields.Time(required=True)
    admin_id_admin = fields.Int(required=True)
