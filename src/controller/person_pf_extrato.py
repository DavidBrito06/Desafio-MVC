from typing import Dict
from src.models.sqlite.interfaces.personpf_interface import PersonPfInterfaceRepository
from src.models.sqlite.entites.person_pf import PersonPf
from src.controller.interface.person_pf_extrato_controller import PersonPfExtratoControllerInterface


class PersonPfExtratoController(PersonPfExtratoControllerInterface):
    def __init__(self, person_pf_interface: PersonPfInterfaceRepository):
        self.person_pf_interface = person_pf_interface

    def extrato(self, cliente_id: int) -> Dict:
        """Obtém o extrato de uma conta PF"""

        cliente = self.__get_cliente(cliente_id)

        if not cliente:
            return self.__formated_error("Conta PF não encontrada")

        return self.__formated_response(cliente)

    # 🔹 Métodos privados
    def __get_cliente(self, cliente_id: int) -> PersonPf:
        """Chama o repositório para buscar o cliente"""
        return self.person_pf_interface.extrato(cliente_id)

    def __formated_response(self, cliente: PersonPf) -> Dict:
        return {
            "data": {
                "type": "personpf",
                "id": cliente.id,
                "attributes": {
                    "nome_completo": cliente.nome_completo,
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
