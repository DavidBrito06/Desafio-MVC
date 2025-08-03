from src.models.sqlite.entites.person_pf import PersonPf
class PersonPfRepository:
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
