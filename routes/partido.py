from flask import jsonify, request, Blueprint, make_response

from controllers.partido import PartidoController
from models.partido import PartidoDoesNotExist

partidos_controller = PartidoController()

partidos_bp = Blueprint("partidos_blueprint", __name__)

@partidos_bp.route("/", methods=["GET"])
def partidos():
    list_partidos = []
    for partido in partidos_controller.get_all():
        list_partidos.append(party.__dict__)
    return jsonify({
        "partidos": list_partidos,
        "count": partidos_controller.count()
    })

@partidos_bp.route("/<string:party_id>", methods=["GET"])
def partido(partido_id):
    try:
        partido = partidos_controller.get_by_id(partido_id)
        return make_response({ "partido": partido.__dict__ }, 200)
    except PartidoDoesNotExist:
        return jsonify({
            "error": "Partido político no existe"
        }), 404

@partidos_bp.route("/", methods=["POST"])
def create_partido():
    partido = partidos_controller.create(request.get_json())
    return jsonify({
        "message": "Partido político creado exitosamente",
        "partido": partido.__dict__
    }), 201