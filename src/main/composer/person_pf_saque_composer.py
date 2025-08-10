from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.personpf_repository import PersonPfRepository
from src.controller.person_pf_saque import PersonPfSaqueController
from src.view.person_pf_saque_view import PersonPfSaqueView

def person_pf_creator_composer():
    model = PersonPfRepository(db_connection_handler)
    controller = PersonPfSaqueController(model)
    view = PersonPfSaqueView(controller) 

    return view