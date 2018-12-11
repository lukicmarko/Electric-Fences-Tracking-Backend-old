from model.base import db
from model.base import ma
from sqlalchemy import Column, String, Integer, ForeignKey


class Service(db.Model):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    title = Column(String(16))
    service_date = Column(String(16))
    service_description = Column(String(255))
    main_entity_id = db.Column(Integer, ForeignKey('main_entities.id'))

    def __init__(self, title, service_date):
        self.title = title
        self.service_date = service_date


class ServiceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'service_date', 'service_description', 'main_entity_id')
