from src.controller.interface.person_pf_saque_controller import PersonPfSaqueControllerInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.view.interfaces.view_interface import ViewInterface

class PersonPfSaqueView(ViewInterface):
    def __init__(self, controller: PersonPfSaqueControllerInterface):
        self.__controller = controller
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        # Pega dados do corpo da requisição
        cliente_id = http_request.body.get("cliente_id")
        valor = http_request.body.get("valor")

        # Validação simples
        if cliente_id is None or valor is None:
            return HttpResponse(
                status_code=400,
                body={"error": "Parâmetros 'cliente_id' e 'valor' são obrigatórios"}
            )

        # Chama o controller para processar o saque
        sucesso = self.__controller.saque(cliente_id, valor)

        # Retorna resposta
        if sucesso:
            return HttpResponse(
                status_code=200,
                body={"message": "Saque realizado com sucesso"}
            )
        else:
            return HttpResponse(
                status_code=400,
                body={"error": "Saldo insuficiente ou operação inválida"}
            )
