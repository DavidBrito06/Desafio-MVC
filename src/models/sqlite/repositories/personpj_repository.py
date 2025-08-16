from src.models.sqlite.entites.person_pj import PersonPj
from typing import List
from src.models.sqlite.interfaces.personpj_interface import PersonPjInterfaceRepository

class PersonPjRepository(PersonPjInterfaceRepository):
    LIMITE_DE_SAQUE = 10000.00

    def __init__(self, db_connection):
        self.__db_connection = db_connection

    # Implementa o método abstrato
    def sacar_dinheiro(self, cliente_id: int, valor: float) -> bool:
        person = self.get_person_pj_by_id(cliente_id)
        if not person:
            return False
        if valor > self.LIMITE_DE_SAQUE or person.saldo < valor:
            return False

        # Atualiza saldo
        novo_saldo = person.saldo - valor
        self.update_saldo(cliente_id, novo_saldo)
        return True

    # Outros métodos já existentes
    def get_person_pj_by_id(self, person_id: int) -> PersonPj:
        with self.__db_connection as db:
            return db.session.query(PersonPj).filter_by(id=person_id).one_or_none()

    def update_saldo(self, person_id: int, novo_saldo: float) -> None:
        with self.__db_connection as db:
            cliente = db.session.query(PersonPj).filter_by(id=person_id).one_or_none()
            if cliente:
                cliente.saldo = novo_saldo
                db.session.commit()

    def extrato(self, cliente_id: int) -> PersonPj:
        return self.get_person_pj_by_id(cliente_id)

    def insert_person_pj(self, faturamento: int, idade: int, nome_fantasia: str, celular: str, email_corporativo: str, categoria: str, saldo: float) -> None:
        with self.__db_connection as db:
            personpj_data = PersonPj(
                faturamento=faturamento,
                idade=idade,
                nome_fantasia=nome_fantasia,
                celular=celular,
                email_corporativo=email_corporativo,
                categoria=categoria,
                saldo=saldo
            )
            db.session.add(personpj_data)
            db.session.commit()

    def list_person_pj(self) -> List[PersonPj]:
        with self.__db_connection as db:
            return db.session.query(PersonPj).all()

