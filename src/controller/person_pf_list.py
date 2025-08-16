from src.models.sqlite.interfaces.personpf_interface import PersonPfInterfaceRepository
from typing import Dict, List
from src.models.sqlite.entites.person_pf import PersonPf
from src.controller.interface.person_pf_list_controller import PersonPfListControllerInterface

class PersonPfListController(PersonPfListControllerInterface):
    def __init__(self, person_pf_interface: PersonPfInterfaceRepository):
        self.person_pf_interface = person_pf_interface

    def list_person_pf(self) -> Dict:
        personpf = self.__get_person_in_bd()
        response = self.__formated_response(personpf)
        return response

    
    def __get_person_in_bd(self) -> List[PersonPf]:
        personpf = self.person_pf_interface.list_person_pf()
        return personpf
    
    def __formated_response(self, personpf: List[PersonPf]) -> Dict:
        formatted_personpf = []
        for person in personpf:
            formatted_personpf.append({
                "renda_mensal": person.renda_mensal,
                "idade": person.idade,
                "nome_completo": person.nome_completo,
                "celular": person.celular,
                "email": person.email,
                "categoria": person.categoria,
                "saldo": person.saldo
            })
        return{
                "data":{
                    "type":"personpf",
                    "attributes": formatted_personpf,
                    "count": len(formatted_personpf)
                }
            }