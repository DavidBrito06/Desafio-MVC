from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.personpf_repository import PersonPfRepository
from src.controller.person_pf_list import PersonPfListController
from src.view.person_pf_list_view import PersonPfListView

def person_pf_list_composer():
    model = PersonPfRepository(db_connection_handler)
    controller = PersonPfListController(model)
    view = PersonPfListView(controller) 

    return view