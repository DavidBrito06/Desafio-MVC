from .person_pf_extrato import PersonPfExtratoController
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

    def extrato(self, cliente_id: int):
        if cliente_id == 1:
            return self.person
        return None


def test_extrato_pf_sucesso():
    mock_repo = MockPersonPf()
    controller = PersonPfExtratoController(mock_repo)

    response = controller.extrato(1)

    assert "data" in response
    assert response["data"]["attributes"]["nome_completo"] == "David Silva"
    assert response["data"]["attributes"]["saldo"] == 10000.00


def test_extrato_pf_conta_nao_encontrada():
    mock_repo = MockPersonPf()
    controller = PersonPfExtratoController(mock_repo)

    response = controller.extrato(99)

    assert "errors" in response
    assert response["errors"]["message"] == "Conta PF não encontrada"


