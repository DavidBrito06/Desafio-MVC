from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.personpj_repository import PersonPjRepository
from src.controller.person_pj_creator import PersonPjCreator
from src.view.person_pj_creator_view import PersonPjCreatorView

def person_pj_creator_composer():
    model = PersonPjRepository(db_connection_handler)
    controller = PersonPjCreator(model)
    view = PersonPjCreatorView(controller) 

    return view