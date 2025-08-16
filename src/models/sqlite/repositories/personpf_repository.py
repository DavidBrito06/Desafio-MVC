from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entites.person_pf import PersonPf
from src.models.sqlite.interfaces.personpf_interface import PersonPfInterfaceRepository

class PersonPfRepository(PersonPfInterfaceRepository):
    LIMITE_DE_SAQUE = 5000.00  # Limite de saque para Pessoa Física

    def __init__(self, db_connection):
        self.__db_connection = db_connection

    # Implementa o método abstrato de saque
    def sacar_dinheiro(self, cliente_id: int, valor: float) -> bool:
        person = self.get_person_pf_by_id(cliente_id)
        if not person:
            return False
        if valor > self.LIMITE_DE_SAQUE or person.saldo < valor:
            return False

        novo_saldo = person.saldo - valor
        self.update_saldo(cliente_id, novo_saldo)
        return True

    # Busca PF pelo ID
    def get_person_pf_by_id(self, person_id: int) -> PersonPf:
        with self.__db_connection as db:
            return db.session.query(PersonPf).filter_by(id=person_id).one_or_none()

    # Atualiza saldo
    def update_saldo(self, person_id: int, novo_saldo: float) -> None:
        with self.__db_connection as db:
            person = db.session.query(PersonPf).filter_by(id=person_id).one_or_none()
            if person:
                person.saldo = novo_saldo
                db.session.commit()

    # Retorna extrato
    def extrato(self, cliente_id: int) -> PersonPf:
        return self.get_person_pf_by_id(cliente_id)

    # Insere nova pessoa física
    def insert_person_pf(self, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float, renda_mensal: float) -> None:
        with self.__db_connection as db:
            person_data = PersonPf(
                idade=idade,
                nome_completo=nome_completo,
                celular=celular,
                email=email,
                categoria=categoria,
                saldo=saldo,
                renda_mensal=renda_mensal
            )
            db.session.add(person_data)
            db.session.commit()

    # Lista todos os PF
    def list_person_pf(self) -> List[PersonPf]:
        with self.__db_connection as db:
            return db.session.query(PersonPf).all()
