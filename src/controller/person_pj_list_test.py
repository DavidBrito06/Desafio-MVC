from src.models.sqlite.entites.person_pj import PersonPj
from .person_pj_list import PersonPjListController

class MockPersonPj:
    def list_person_pj(self):
        return [
            PersonPj(
                faturamento=50000.0,
                idade=30,
                nome_fantasia="Empresa teste",
                celular="123456789",
                email_corporativo="empresa@example.com",
                categoria="Tecnologia",
                saldo=10000.0
            )
        ]

def test_list_person_pj():
    controller = PersonPjListController(MockPersonPj())
    response = controller.list_person_pj()

    assert response["data"]["count"] == 1
    assert response["data"]["attributes"][0]["nome_fantasia"] == "Empresa teste"
    assert response["data"]["attributes"][0]["faturamento"] == 50000.0
    assert response["data"]["attributes"][0]["idade"] == 30
    assert response["data"]["attributes"][0]["celular"] == "123456789"
    assert response["data"]["attributes"][0]["email_corporativo"] == "empresa@example.com"
    assert response["data"]["attributes"][0]["categoria"] == "Tecnologia"
    assert response["data"]["attributes"][0]["saldo"] == 10000.0