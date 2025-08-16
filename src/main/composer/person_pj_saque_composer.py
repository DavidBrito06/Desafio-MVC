from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.personpj_repository import PersonPjRepository
from src.controller.person_pj_saque import PersonPjSaqueController
from src.view.person_pj_saque_view import PersonPjSaqueView

def person_pj_saque_composer():
    model = PersonPjRepository(db_connection_handler)
    controller = PersonPjSaqueController(model)
    view = PersonPjSaqueView(controller) 

    return view