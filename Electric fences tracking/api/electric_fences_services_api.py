from model.service import Service, ServiceSchema
from flask import jsonify, Blueprint, make_response
from model.base import db

# Initialize blueprint
electric_fences_services_api = Blueprint('electric_fences_services_api', __name__)


@electric_fences_services_api.route("/electric_fences/<entity_id>/services", methods=["GET"])
def get_electric_fences(entity_id):
    mainEntities = db.session.query(Service).filter(Service.main_entity_id == 1).all()
    schema = ServiceSchema(many=True)
    return jsonify(schema.dump(mainEntities).data)


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
