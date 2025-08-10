from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.personpj_repository import PersonPjRepository
from src.controller.person_pj_extrato import PersonPjExtratoController
from src.view.person_pj_extrato_view import PersonPjExtratoView

def person_pf_creator_composer():
    model = PersonPjRepository(db_connection_handler)
    controller = PersonPjExtratoController(model)
    view = PersonPjExtratoView(controller) 

    return view