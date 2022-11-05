from flask import jsonify, request, Blueprint

from controllers.mesa import MesaController
from models.mesa import MesaDoesNotExist

mesas_controller = MesaController()

mesas_bp = Blueprint("mesas_blueprint", __name__)

@mesas_bp.route("/", methods=["GET"])
def mesas():
    list_mesas = []
    for mesa in mesas_controller.get_all():
        list_mesas.append(mesa.__dict__)
    return jsonify({
        "mesas": list_mesas,
        "count": mesas_controller.count()
    })

@mesas_bp.route("/<string:mesa_id>", methods=["GET"])
def mesa(mesa_id):
    try:
        mesa = mesas_controller.get_by_id()
        return jsonify({ "mesa": mesa.__dict__ }), 200
    except MesaDoesNotExist:
        return jsonify({
            "error": "Mesa de votación no existe"
        }), 404

@mesas_bp.route("/", methods=["POST"])
def create_mesa():
    mesa = mesas_controller.create(request.get_json())
    return jsonify({
        "message": "Mesa de votación creada exitosamente",
        "mesa": mesa.__dict__
    }), 201