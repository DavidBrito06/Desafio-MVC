from src.models.sqlite.interfaces.personpj_interface import PersonPjInterfaceRepository
from typing import Dict, List
from src.models.sqlite.entites.person_pj import PersonPj
from src.controller.interface.person_pj_list_controller import PersonPjListControllerInterface

class PersonPjListController(PersonPjListControllerInterface):
    def __init__(self, person_pj_interface: PersonPjInterfaceRepository):
        self.person_pj_interface = person_pj_interface

    def list_person_pj(self) -> Dict:
        personpj = self.__get_person_in_bd()
        response = self.__formated_response(personpj)
        return response

    def __get_person_in_bd(self) -> List[PersonPj]:
        personpj = self.person_pj_interface.list_person_pj()
        return personpj

    def __formated_response(self, personpj: List[PersonPj]) -> Dict:
        formatted_personpj = []
        for person in personpj:
            formatted_personpj.append({
                "faturamento": person.faturamento,
                "idade": person.idade,
                "nome_fantasia": person.nome_fantasia,
                "celular": person.celular,
                "email_corporativo": person.email_corporativo,
                "categoria": person.categoria,
                "saldo": person.saldo
            })
            return {
                "data":{
                    "type":"personpj",
                    "attributes": formatted_personpj,
                    "count": len(formatted_personpj)
                }
            }

