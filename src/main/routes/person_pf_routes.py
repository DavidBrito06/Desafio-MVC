from flask import Blueprint, jsonify, request
from src.view.http_types.http_request import HttpRequest

from src.main.composer.person_pf_list_composer import person_pf_list_composer
from src.main.composer.person_pf_creator_composer import person_pf_creator_composer
from src.main.composer.person_pf_extrato_composer import person_pf_extrato_composer
from src.main.composer.person_pf_saque_composer import person_pf_saque_composer

person_pf_route_bp = Blueprint('person_pf_route', __name__)

@person_pf_route_bp.route('/personpf', methods=['POST'])
def creator_pf_person():
    try:
        http_request = HttpRequest(body = request.json)
        view = person_pf_creator_composer()
        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@person_pf_route_bp.route('/personpf', methods=['GET'])
def list_pf_person():
    try:
        http_request = HttpRequest()
        view = person_pf_list_composer()
        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    
    except Exception as e:
        return jsonify({"error": str(e)}), 404
    
@person_pf_route_bp.route('/personpf/<int:cliente_id>', methods=['GET'])
def extrato_pf_person(cliente_id):
    try:
        http_request = HttpRequest(param={'cliente_id': cliente_id})
        view = person_pf_extrato_composer()
        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    
    except Exception as e:
        return jsonify({"error": str(e)}), 404
    
@person_pf_route_bp.route('/saquepf/<int:cliente_id>', methods=['PATCH'])
def saque_person_pf(cliente_id):
    try:
        http_request = HttpRequest(param={"cliente_id": cliente_id}, body=request.json)
        view = person_pf_saque_composer()
        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500



        