from src.models.sqlite.entites.person_pf import PersonPf
from .person_pf_list import PersonPfListController

class MockPersonPf:
    def list_person_pf(self):
        return [
            PersonPf(
                renda_mensal=5000.0,
                idade=30,
                nome_completo="John Doe",
                celular="123456789",
                email="john.doe@example.com",
                categoria="A",
                saldo=1000.0
            )
        ]
    
def test_list_person_pf():
    controller = PersonPfListController(MockPersonPf())
    response = controller.list_person_pf()

    assert response["data"]["count"] == 1
    assert response["data"]["attributes"][0]["nome_completo"] == "John Doe"
    assert response["data"]["attributes"][0]["renda_mensal"] == 5000.0
    assert response["data"]["attributes"][0]["idade"] == 30
    assert response["data"]["attributes"][0]["celular"] == "123456789"
    assert response["data"]["attributes"][0]["email"] == "john.doe@example.com"
    assert response["data"]["attributes"][0]["categoria"] == "A"
    assert response["data"]["attributes"][0]["saldo"] == 1000.0
