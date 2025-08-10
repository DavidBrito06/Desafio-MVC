from src.models.sqlite.interfaces.personpf_interface import PersonPfInterfaceRepository
from src.controller.interface.person_pf_creator_controller import PersonPfCreatorControllerInterface
from typing import Dict

class PersonPfCreator(PersonPfCreatorControllerInterface):
    def __init__(self, personpf_repository: PersonPfInterfaceRepository):
        self.personpf_repository = personpf_repository

    def create_personpf(self, personpf_data: Dict) -> Dict:
        renda_mensal = personpf_data['renda_mensal']
        idade = personpf_data['idade']
        nome_completo = personpf_data['nome_completo']
        celular = personpf_data['celular']
        email = personpf_data['email']
        categoria = personpf_data['categoria']
        saldo = personpf_data['saldo']

        self.__insert_person_pf_in_db(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
        personpf_data = self.__format_response(personpf_data)

        return personpf_data

    def __insert_person_pf_in_db(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float) -> None:
        self.personpf_repository.insert_person_pf(
            renda_mensal=renda_mensal,
            idade=idade,
            nome_completo=nome_completo,
            celular=celular,
            email=email,
            categoria=categoria,
            saldo=saldo
        )

    def __format_response(self, personpf_data: Dict) -> Dict:
        return {
            'renda_mensal': personpf_data['renda_mensal'],
            'idade': personpf_data['idade'],
            'nome_completo': personpf_data['nome_completo'],
            'celular': personpf_data['celular'],
            'email': personpf_data['email'],
            'categoria': personpf_data['categoria'],
            'saldo': personpf_data['saldo']
        }
