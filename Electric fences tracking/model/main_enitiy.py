from model.base import db
from model.base import ma, Base
from sqlalchemy import Column, String, Integer


# class Serializer(object):
#
#     def serialize(self):
#         return {c: getattr(self, c) for c in inspect(self).attrs.keys()}
#
#     @staticmethod
#     def serialize_list(l):
#         return [m.serialize() for m in l]

class MainEntity(Base):
    __tablename__ = 'main_entities'

    id = Column(Integer, primary_key=True)
    customer_name = Column(String(16))
    customer_contact = Column(String(16))
    electric_fence_uid = Column(String(16))
    services = db.relationship("Service", backref="MainEntity", lazy='dynamic')

    def __init__(self, customer_name, customer_contact, electric_fence_uid):
        self.customer_name = customer_name
        self.customer_contact = customer_contact
        self.electric_fence_uid = electric_fence_uid


class MainEntitySchema(ma.Schema):
    class Meta:
        fields = ('id', 'customer_name', 'electric_fence_uid', 'customer_contact')

