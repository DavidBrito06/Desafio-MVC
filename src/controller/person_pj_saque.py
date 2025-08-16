from typing import Dict
from src.models.sqlite.entites.person_pj import PersonPj
from src.models.sqlite.interfaces.personpj_interface import PersonPjInterfaceRepository
from src.controller.interface.person_pj_saque_controller import PersonPjSaqueControllerInterface

class PersonPjSaqueController(PersonPjSaqueControllerInterface):
    def __init__(self, person_pj_interface: PersonPjInterfaceRepository):
        self.person_pj_interface = person_pj_interface

    def saque(self, person_id: int, valor: float) -> Dict:
        person = self.__get_person_by_id(person_id)
        if not person:
            return self.__formated_error("Conta PJ não encontrada")
        if person.saldo < valor:
            return self.__formated_error("Saldo insuficiente")

        novo_saldo = person.saldo - valor
        self.__update_saldo(person_id, novo_saldo)
        return self.__formated_success(person, valor, novo_saldo)

    def __get_person_by_id(self, person_id: int) -> PersonPj:
        return self.person_pj_interface.get_person_pj_by_id(person_id)

    def __update_saldo(self, person_id: int, novo_saldo: float) -> None:
        self.person_pj_interface.update_saldo(person_id, novo_saldo)

    def __formated_success(self, person: PersonPj, valor: float, novo_saldo: float) -> Dict:
        return {
            "data": {
                "type": "personpj",
                "id": person.id,
                "attributes": {
                    "nome_fantasia": person.nome_fantasia,
                    "valor_sacado": valor,
                    "saldo_atual": novo_saldo
                },
                "message": "Saque realizado com sucesso!"
            }
        }

    def __formated_error(self, mensagem: str) -> Dict:
        return {"errors": {"message": mensagem}}
