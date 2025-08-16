from typing import Dict
from src.models.sqlite.interfaces.personpf_interface import PersonPfInterfaceRepository
from src.models.sqlite.entites.person_pf import PersonPf
from src.controller.interface.person_pf_saque_controller import PersonPfSaqueControllerInterface

class PersonPfSaqueController(PersonPfSaqueControllerInterface):
    def __init__(self, person_pf_interface: PersonPfInterfaceRepository):
        self.person_pf_interface = person_pf_interface

    def saque(self, person_id: int, valor: float) -> Dict:
        person = self.person_pf_interface.get_person_pf_by_id(person_id)

        if not person:
            return {"errors": {"message": "Conta PF não encontrada"}}

        if person.saldo < valor:
            return {"errors": {"message": "Saldo insuficiente"}}

        novo_saldo = person.saldo - valor
        self.person_pf_interface.update_saldo(person_id, novo_saldo)

        return {
            "data": {
                "type": "personpf",
                "id": person.id,
                "attributes": {
                    "nome_completo": person.nome_completo,
                    "valor_sacado": valor,
                    "saldo_atual": novo_saldo
                },
                "message": "Saque realizado com sucesso!"
            }
        }

