from flask import jsonify, request, Blueprint

from controllers.candidato import CandidatoController
from models.candidato import CandidatoDoesNotExist

candidato_controller = CandidatoController()

candidatos_bp = Blueprint("candidatos_blueprint", __name__)

@candidatos_bp.route("/", methods=["POST"])
def create_candidato():
    candidato = candidato_controller.create(request.get_json())
    return jsonify({
        "message": "Candidato creado exitosamente",
        "mesa": candidato.__dict__
    }), 201

@candidatos_bp.route("/", methods=["GET"])
def candidatos():
    return jsonify({
        "candidatos": [candidatos.to_json() for candidate in candidato_controller.get_all()],
        "count": candidato_controller.count()
    })

@candidatos_bp.route("/<string:candidato_id>", methods=["GET"])
def candidato(candidato_id):
    try:
        candidato = candidato_controller.get_by_id(candidato_id)
        return jsonify({ "candidato": candidato.to_json() }), 200
    except CandidatoDoesNotExist:
        return jsonify({
            "error": "Candidato no existe"
        }), 404