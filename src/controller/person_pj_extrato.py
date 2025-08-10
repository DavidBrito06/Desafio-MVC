from typing import Dict
from src.models.sqlite.interfaces.personpj_interface import PersonPjInterfaceRepository
from src.models.sqlite.entites.person_pj import PersonPj
from src.controller.interface.person_pj_extrato_controller import PersonPjExtratoControllerInterface


class PersonPjExtratoController(PersonPjExtratoControllerInterface):
    def __init__(self, person_pj_interface: PersonPjInterfaceRepository):
        self.person_pj_interface = person_pj_interface

    def extrato(self, cliente_id: int) -> Dict:
        """Obtém o extrato de uma conta PJ"""

        cliente = self.__get_cliente(cliente_id)

        if not cliente:
            return self.__formated_error("Conta PJ não encontrada")

        return self.__formated_response(cliente)

    # 🔹 Métodos privados
    def __get_cliente(self, cliente_id: int) -> PersonPj:
        """Chama o repositório para buscar o cliente"""
        return self.person_pj_interface.extrato(cliente_id)

    def __formated_response(self, cliente: PersonPj) -> Dict:
        return {
            "data": {
                "type": "personpj",
                "id": cliente.id,
                "attributes": {
                    "nome_fantasia": cliente.nome_fantasia,
                    "idade": cliente.idade,
                    "saldo": cliente.saldo
                },
                "message": "Extrato obtido com sucesso"
            }
        }

    def __formated_error(self, mensagem: str) -> Dict:
        return {
            "errors": {
                "message": mensagem
            }
        }
