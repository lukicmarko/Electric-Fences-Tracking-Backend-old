from model.service import Service
from model.service import ServiceSchema
from flask import jsonify, Blueprint, make_response, request
from model.base import db

# Initialize blueprint
services_api = Blueprint('service_api', __name__)


@services_api.route("/services", methods=["GET"])
def get_services():
    services = db.session.query(Service).all()
    schema = ServiceSchema(many=True)
    return jsonify(schema.dump(services).data)


@services_api.route("/services", methods=["POST"])
def create_service():
    if request.content_type == 'application/json':
        data = request.get_json()

        customer_contact = data.get('customer_contact')
        customer_name = data.get('customer_name')
        electric_fence_uid = data.get('electric_fence_uid')

        if customer_contact and customer_name and electric_fence_uid:
            new_entity = Service(customer_name, customer_contact, electric_fence_uid)
            new_entity.save()
            schema = MainEntitySchema()
            return response('success', schema.dump(new_entity).data, 201)
        return response('failed', 'Missing some attribute', 400)
    return response('failed', 'Content-type must be json', 202)



def response(status, message, status_code):
    """
    Make an http response helper
    :param status: Status message
    :param message: Response Message
    :param status_code: Http response code
    :return:
    """
    return make_response(jsonify({
        'status': status,
        'message': message
    })), status_code
