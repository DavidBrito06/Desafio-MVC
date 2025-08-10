from src.models.sqlite.interfaces.personpj_interface import PersonPjInterfaceRepository
from typing import Dict
from src.controller.interface.person_pj_creator_controller import PersonPjCreatorControllerInterface

class PersonPjCreator(PersonPjCreatorControllerInterface):
    def __init__(self, personpj_repository: PersonPjInterfaceRepository):
        self.personpj_repository = personpj_repository

    def create_personpj(self, personpj_data: Dict) -> Dict:
        faturamento = personpj_data['faturamento']
        idade = personpj_data['idade']
        nome_fantasia = personpj_data['nome_fantasia']
        celular = personpj_data['celular']
        email_corporativo = personpj_data['email_corporativo']
        categoria = personpj_data['categoria']
        saldo = personpj_data['saldo']

        self.__insert_person_pj_in_db(faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)
        personpj_data = self.__format_response(personpj_data)

        return personpj_data

    def __insert_person_pj_in_db(self, faturamento: float, idade: int, nome_fantasia: str, celular: str, email_corporativo: str, categoria: str, saldo: float) -> None:
        self.personpj_repository.insert_person_pj(
            faturamento=faturamento,
            idade=idade,
            nome_fantasia=nome_fantasia,
            celular=celular,
            email_corporativo=email_corporativo,
            categoria=categoria,
            saldo=saldo
        )
    
    def __format_response(self, personpj_data: Dict) -> Dict:
        return {
            'faturamento': personpj_data['faturamento'],
            'idade': personpj_data['idade'],
            'nome_fantasia': personpj_data['nome_fantasia'],
            'celular': personpj_data['celular'],
            'email_corporativo': personpj_data['email_corporativo'],
            'categoria': personpj_data['categoria'],
            'saldo': personpj_data['saldo']
        }
