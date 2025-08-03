from src.models.sqlite.entites.person_pj import PersonPj
from typing import List
from sqlalchemy.orm.exc import NoResultFound

class PersonPjRepository:
    LIMITE_SAQUE_PJ = 1000.00  # Limite de saque para Pessoa Jurídica
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
        if valor <= 0:
            print("Valor para saque deve ser positivo.")
            return False
    
        if valor > self.LIMITE_SAQUE_PJ:
            print(f"Saque de R${valor:.2f} excede o limite permitido para PJ.")
            return False
    
        with self.__db_connection as database:
            try:
                person = database.session.query(PersonPj).filter(PersonPj.id == cliente_id).first()
                
                if not person:
                    print(f"Cliente PJ com ID {cliente_id} não encontrado.")
                    return False

                if person.saldo < valor:
                    print("Saldo insuficiente para saque.")
                    return False
                
                person.saldo -= valor
                database.session.commit()
                print(f"Saque de R${valor:.2f} realizado para cliente ID {cliente_id}. Novo saldo: R${person.saldo:.2f}")
                return True
            except Exception as e:
                database.session.rollback()
                print(f"Erro ao sacar: {e}")
                return False

                
             
    def realizar_extrato(self, cliente_id: int) -> str:
        with self.__db_connection as database:
            try:
                person = database.session.query(PersonPj).filter(PersonPj.id == cliente_id).first()

                if not person:
                    return f"Cliente PJ com ID {cliente_id} não encontrado."

                extrato = (
                    f"Extrato do Cliente PJ:\n"
                    f"ID: {person.id}\n"
                    f"Nome Fantasia: {person.nome_fantasia}\n"
                    f"Faturamento: R${person.faturamento:.2f}\n"
                    f"Idade: {person.idade} anos\n"
                    f"Celular: {person.celular}\n"
                    f"E-mail Corporativo: {person.email_corporativo}\n"
                    f"Categoria: {person.categoria}\n"
                    f"Saldo Atual: R${person.saldo:.2f}\n"
                )
                return extrato
            except Exception as e:
                print(f"Erro ao realizar extrato: {e}")
                return "Erro ao realizar extrato."
