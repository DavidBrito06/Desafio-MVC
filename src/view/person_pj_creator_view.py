from src.controller.interface.person_pj_creator_controller import PersonPjCreatorControllerInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.view.interfaces.view_interface import ViewInterface

class PersonPjCreatorView(ViewInterface):
    def __init__(self, controller: PersonPjCreatorControllerInterface) -> None:
        self.__controller = controller
    
    def handle(self, http_request: HttpRequest)-> HttpResponse:
        personpf_data = http_request.body
        body_response = self.__controller.create_personpj(personpf_data)

        return HttpResponse(status_code=201, body=body_response)