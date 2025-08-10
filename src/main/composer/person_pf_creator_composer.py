from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.personpf_repository import PersonPfRepository
from src.controller.person_pf_creator import PersonPfCreator
from src.view.person_pf_creator_view import PersonPfCreatorView

def person_pf_creator_composer():
    model = PersonPfRepository(db_connection_handler)
    controller = PersonPfCreator(model)
    view = PersonPfCreatorView(controller) 

    return view