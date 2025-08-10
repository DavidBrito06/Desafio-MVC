from src.controller.interface.person_pj_extrato_controller import PersonPjExtratoControllerInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.view.interfaces.view_interface import ViewInterface

class PersonPjExtratoView(ViewInterface):
    def __init__(self, controller: PersonPjExtratoControllerInterface):
        self.__controller = controller
    
    def handle(self, http_request: HttpRequest):
        cliente_id = http_request.param("cliente_id")
        extrato = self.__controller.extrato(cliente_id)

        return HttpResponse(status_code=200, body=extrato)