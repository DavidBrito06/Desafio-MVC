from src.models.sqlite.entites.person_pf import PersonPf

class MockPersonPf:
    def __init__(self):
        self.person = PersonPf(
            id=1,
            renda_mensal=50000.0,
            idade=30,
            nome_completo="David Silva",
            celular="123456789",
            email="David@example.com",
            categoria="Tecnologia",
            saldo=10000.0
        )

    def list_person_pf(self):
        return [self.person]

    def get_person_pf_by_id(self, person_id: int):
        """Simula busca pelo ID"""
        return self.person if person_id == 1 else None

    def update_saldo(self, person_id: int, novo_saldo: float):
        """Simula atualização de saldo"""
        if person_id == 1:
            self.person.saldo = novo_saldo
            return True
        return False

    def saque_person_pf(self, person_id: int, valor: float):
        """Simula saque diretamente, se necessário"""
        if person_id != 1:
            return {"errors": {"message": "Conta PF não encontrada"}}
        if self.person.saldo < valor:
            return {"errors": {"message": "Saldo insuficiente"}}
        self.person.saldo -= valor
        return {
            "data": {
                "id": self.person.id,
                "attributes": {
                    "nome_completo": self.person.nome_completo,
                    "saldo_atual": self.person.saldo
                },
                "message": "Saque realizado com sucesso!"
            }
        }

