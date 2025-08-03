from src.models.sqlite.entites.person_pj import PersonPj
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.interfaces.personpj_interface import PersonPjInterface

class PersonPjRepository(PersonPjInterface):
    LIMITE_DE_SAQUE = 10000.00  # Limite de saque para Pessoa Jurídica
    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def insert_person_pj(self,faturamento: int, idade: int, nome_fantasia: str, celular: str, email_corporativo: str, categoria: str, saldo: float) -> None:
        with self.__db_connection as database:
            try:
                personpj_data  = PersonPj(
                    faturamento=faturamento,
                    idade=idade,
                    nome_fantasia=nome_fantasia,
                    celular=celular,
                    email_corporativo=email_corporativo,
                    categoria=categoria,
                    saldo=saldo
                )
                database.session.add(personpj_data)
                database.session.commit()

            except Exception as e:
                database.session.rollback()
                print(f"Error inserting PersonPj: {e}")
            
        
    def list_person_pj(self) -> List[PersonPj]:
        with self.__db_connection as database:
            try:
                person = database.session.query(PersonPj).all()
                return person
            except NoResultFound:
                return []

    def sacar_dinheiro(self, cliente_id: int, valor: float) -> bool:
        with self.__db_connection as database:
            if valor > self.LIMITE_DE_SAQUE:
                print("❌ Saque negado: valor excede o limite para pessoa física.")
                return False
            try:
                cliente = database.session.query(PersonPj).filter_by(id=cliente_id).one()
                if cliente.saldo >= valor:
                    cliente.saldo -= valor
                    database.session.commit()
                    return True
                return False
            except NoResultFound:
                return False
            
    
    def extrato(self, cliente_id: int) -> PersonPj:
        with self.__db_connection as database:
            try:
                cliente = database.session.query(PersonPj).filter_by(id=cliente_id).one()
                return cliente
            except NoResultFound:
                return None
