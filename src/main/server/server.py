from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.connection import db_connection_handler

from src.main.routes.person_pj_routes import person_pj_route_bp
from src.main.routes.person_pf_routes import persor_pf_route_bp

db_connection_handler.connect_to_bd()
app =Flask(__name__)
CORS(app)

app.register_blueprint(person_pj_route_bp)
app.register_blueprint(persor_pf_route_bp)



