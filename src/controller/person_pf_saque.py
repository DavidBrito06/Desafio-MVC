from typing import Dict
from src.models.sqlite.interfaces.personpf_interface import PersonPfInterfaceRepository
from src.models.sqlite.entites.person_pf import PersonPf
from src.controller.interface.person_pf_saque_controller import PersonPfSaqueControllerInterface


class PersonPfSaqueController(PersonPfSaqueControllerInterface):
    def __init__(self, person_pf_interface: PersonPfInterfaceRepository):
        self.person_pf_interface = person_pf_interface

    def saque(self, person_id: int, valor: float) -> Dict:
        """Realiza saque para uma conta de pessoa física"""

        person = self.__get_person_by_id(person_id)

        if not person:
            return self.__formated_error("Conta PF não encontrada")

        if person.saldo < valor:
            return self.__formated_error("Saldo insuficiente")

        novo_saldo = person.saldo - valor
        self.__update_saldo(person_id, novo_saldo)

        return self.__formated_response(person, valor, novo_saldo)

    # 🔹 Métodos privados
    def __get_person_by_id(self, person_id: int) -> PersonPf:
        return self.person_pf_interface.get_person_pf_by_id(person_id)

    def __update_saldo(self, person_id: int, novo_saldo: float) -> None:
        self.person_pf_interface.update_saldo(person_id, novo_saldo)

    def __formated_response(self, person: PersonPf, valor: float, novo_saldo: float) -> Dict:
        return {
            "data": {
                "type": "personpf",
                "id": person.id,
                "attributes": {
                    "nome": person.nome,
                    "valor_sacado": valor,
                    "saldo_atual": novo_saldo
                },
                "message": "Saque realizado com sucesso!"
            }
        }

    def __formated_error(self, mensagem: str) -> Dict:
        return {
            "errors": {
                "message": mensagem
            }
        }
