from src.controller.interface.person_pj_saque_controller import PersonPjSaqueControllerInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.view.interfaces.view_interface import ViewInterface

class PersonPjSaqueView(ViewInterface):
    def __init__(self, controller: PersonPjSaqueControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        cliente_id = http_request.param.get("cliente_id") or (http_request.body.get("cliente_id") if http_request.body else None)
        valor = http_request.body.get("valor") if http_request.body else None

        if cliente_id is None or valor is None:
            return HttpResponse(
                status_code=400,
                body={"errors": {"message": "Parâmetros 'cliente_id' e 'valor' são obrigatórios"}}
            )

        resultado = self.__controller.saque(cliente_id, valor)
        status_code = 400 if "errors" in resultado else 200

        return HttpResponse(status_code=status_code, body=resultado)


