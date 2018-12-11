from model.main_enitiy import MainEntity, MainEntitySchema
from flask import jsonify, Blueprint, make_response, request
from model.base import db

# Initialize blueprint
electric_fences_api = Blueprint('electric_fences_api', __name__)


@electric_fences_api.route("/electric_fences", methods=["GET"])
def get_electric_fences():
    mainEntities = db.session.query(MainEntity).all()
    schema = MainEntitySchema(many=True)
    return jsonify(schema.dump(mainEntities).data)


@electric_fences_api.route("/electric_fences", methods=["POST"])
def create_electric_fence():
    if request.content_type == 'application/json':
        data = request.get_json()

        customer_contact = data.get('customer_contact')
        customer_name = data.get('customer_name')
        electric_fence_uid = data.get('electric_fence_uid')

        if customer_contact and customer_name and electric_fence_uid:
            new_entity = MainEntity(customer_name, customer_contact, electric_fence_uid)
            new_entity.save()
            schema = MainEntitySchema()
            return response('success', schema.dump(new_entity).data, 201)
        return response('failed', 'Missing some attribute', 400)
    return response('failed', 'Content-type must be json', 202)


@electric_fences_api.route("/electric_fences/<entity_id>", methods=["PUT"])
def update_electric_fence(entity_id):
    if request.content_type == 'application/json':
        data = request.get_json()
        electric_fence = db.session.query(MainEntity).get(int(entity_id))

        electric_fence.customer_contact = data.get('customer_contact')
        electric_fence.customer_name = data.get('customer_name')
        electric_fence.electric_fence_uid = data.get('electric_fence_uid')

        electric_fence.save()
        schema = MainEntitySchema()
        return response('success', schema.dump(electric_fence).data, 201)
    return response('failed', 'Content-type must be json', 202)


@electric_fences_api.route("/electric_fences/<entity_id>", methods=["DELETE"])
def delete_electric_fence(entity_id):
    # Check item id is an integer
    try:
        int(entity_id)
    except ValueError:
        return response('failed', 'Provide a valid item Id', 202)

    electric_fence = db.session.query(MainEntity).get(int(entity_id))
    if electric_fence is None:
        return response('failed', 'electric fence doesnt exist', 202)

    electric_fence.delete()

    return response('success', "Deleting was successful", 200)


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
