from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.personpj_repository import PersonPjRepository
from src.controller.person_pj_list import PersonPjListController
from src.view.person_pj_list_view import PersonPjListView

def person_pf_creator_composer():
    model = PersonPjRepository(db_connection_handler)
    controller = PersonPjListController(model)
    view = PersonPjListView(controller) 

    return view