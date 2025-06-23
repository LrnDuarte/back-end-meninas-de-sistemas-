from app.extensions import ma
from app.models import Event
class EventSchema(ma.SQLAlchemyAutoSchema):


    class Meta:
        model = Event
        load_instance = True

event_schema = EventSchema()
events_schema = EventSchema(many=True)