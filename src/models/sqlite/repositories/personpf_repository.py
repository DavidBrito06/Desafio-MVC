from src.models.sqlite.entites.person_pf import PersonPf
from sqlalchemy.orm.exc import NoResultFound
from typing import List
from src.models.sqlite.interfaces.personpf_interface import PersonPfInterfaceRepository


class PersonPfRepository(PersonPfInterfaceRepository):
    LIMITE_DE_SAQUE = 1000.00
    def __init__(self, db_connection):
        self.__db_connection = db_connection
    
    def insert_person_pf(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float) -> None:
        with self.__db_connection as database:
            try:
                data = PersonPf(
                    renda_mensal=renda_mensal,
                    idade=idade,
                    nome_completo=nome_completo,
                    celular=celular,
                    email=email,
                    categoria=categoria,
                    saldo=saldo
                )
                database.session.add(data)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                print(f"Error inserting PersonPf: {e}")
            

    def list_person_pf(self) -> List[PersonPf]:
        with self.__db_connection as database:
            try:
                person = database.session.query(PersonPf).all()
                return person
            except NoResultFound:
                return []
    
    def sacar_dinheiro(self, cliente_id: int, valor: float) -> bool:
        with self.__db_connection as database:
            if valor > self.LIMITE_DE_SAQUE:
                print("❌ Saque negado: valor excede o limite para pessoa física.")
                return False
            try:
                cliente = database.session.query(PersonPf).filter_by(id=cliente_id).one()
                if cliente.saldo >= valor:
                    cliente.saldo -= valor
                    database.session.commit()
                    return True
                return False
            except NoResultFound:
                return False
            
    
    def extrato(self, cliente_id: int) -> PersonPf:
        with self.__db_connection as database:
            try:
                cliente = database.session.query(PersonPf).filter_by(id=cliente_id).one()
                return cliente
            except NoResultFound:
                return None
