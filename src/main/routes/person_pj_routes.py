from flask import Blueprint, jsonify, request
from src.view.http_types.http_request import HttpRequest

from src.main.composer.person_pj_creator_composer import person_pj_creator_composer
from src.main.composer.person_pj_list_composer import person_pj_list_composer

person_pj_route_bp = Blueprint('person_pj_route', __name__)

@person_pj_route_bp.route('/personpj', methods= ['POST'])
def creator_person_pf():
    try:
        http_request = HttpRequest(body= request.json)
        view = person_pj_creator_composer()
        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@person_pj_route_bp.route('/personpj', methods= ['GET'])
def list_person_pj():
    try:
        http_request = HttpRequest()
        view = person_pj_list_composer()
        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    
    except Exception as e:
        return jsonify({"error": str(e)}), 404
        

