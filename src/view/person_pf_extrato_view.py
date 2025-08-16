from src.controller.interface.person_pf_extrato_controller import PersonPfExtratoControllerInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.view.interfaces.view_interface import ViewInterface

class PersonPfExtratoView(ViewInterface):
    def __init__(self, controller: PersonPfExtratoControllerInterface):
        self.__controller = controller
    
    def handle(self, http_request: HttpRequest):
        cliente_id = http_request.param["cliente_id"]
        extrato = self.__controller.extrato(cliente_id)

        return HttpResponse(status_code=200, body=extrato)
        