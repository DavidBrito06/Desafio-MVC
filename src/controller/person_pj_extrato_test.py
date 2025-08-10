from src.models.sqlite.entites.person_pj import PersonPj
from .person_pj_extrato import PersonPjExtratoController

class MockPersonPj:
    def __init__(self):
        self.person = PersonPj(
            id=1,
            faturamento=50000.0,
            idade=30,
            nome_fantasia="Empresa Teste",
            celular="11999999999",
            email_corporativo="empresa@teste.com",
            categoria="Tecnologia",
            saldo=20000.0
        )

    def extrato(self, cliente_id: int):
        if cliente_id == 1:
            return self.person
        return None

def test_extrato_pj_sucesso():
    mock_repo = MockPersonPj()
    controller = PersonPjExtratoController(mock_repo)

    response = controller.extrato(1)

    assert "data" in response
    assert response["data"]["attributes"]["nome_fantasia"] == "Empresa Teste"
    assert response["data"]["attributes"]["saldo"] == 20000.0
    assert response["data"]["message"] == "Extrato obtido com sucesso"


def test_extrato_pj_conta_nao_encontrada():
    mock_repo = MockPersonPj()
    controller = PersonPjExtratoController(mock_repo)

    response = controller.extrato(99)

    assert "errors" in response
    assert response["errors"]["message"] == "Conta PJ não encontrada"