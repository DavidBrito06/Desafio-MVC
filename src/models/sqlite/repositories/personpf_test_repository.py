from unittest import mock
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entites.person_pf import PersonPf
from .personpf_repository import PersonPfRepository

class MockConnection:
    def __init__(self):
        self.session = mock.Mock()

        # Dados mockados
        self.person_list = [
            PersonPf(
                renda_mensal=2000.00,
                idade=30,
                nome_completo="João da Silva",
                celular="123456789",
                email="teste@empresa.com",
                categoria="Categoria Teste",
                saldo=50000
            ),
            PersonPf(
                renda_mensal=1500.00,
                idade=10,
                nome_completo="Maria da Silva",
                celular="987654321",
                email="teste2@empresa.com",
                categoria="Categoria Teste 2",
                saldo=100000
            )
        ]

        # Mock para query().all()
        query_mock = mock.Mock()
        query_mock.all.return_value = self.person_list

        # Configura session.query(PersonPj) para retornar query_mock
        self.session.query.return_value = query_mock

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class MockConnectionNoResult:
    def __init__(self):
        self.session = mock.Mock()
        self.session.query.side_effect = self._raise_no_result_found

    def _raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def test_list_person_pf():
    mock_connection = MockConnection()
    repository = PersonPfRepository(mock_connection)

    response = repository.list_person_pf()

    assert isinstance(response, list)
    assert len(response) == 2
    assert response[0].nome_completo == "João da Silva"

