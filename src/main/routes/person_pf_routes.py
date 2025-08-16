from flask import Blueprint, jsonify, request
from src.view.http_types.http_request import HttpRequest

from src.main.composer.person_pf_creator_composer import person_pf_creator_composer

persor_pf_route_bp = Blueprint('persor_pf_route', __name__)

@persor_pf_route_bp.route('/personpf', methods=['POST'])
def creator_pf_person():
    try:
        http_request = HttpRequest(body = request.json)
        view = person_pf_creator_composer()
        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        