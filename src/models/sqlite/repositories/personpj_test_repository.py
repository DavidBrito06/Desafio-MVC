from unittest import mock
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entites.person_pj import PersonPj
from .personpj_repository import PersonPjRepository


class MockConnection:
    def __init__(self):
        self.session = mock.Mock()

        # Dados mockados
        self.person_list = [
            PersonPj(
                faturamento=100000,
                idade=5,
                nome_fantasia="Empresa Teste",
                celular="123456789",
                email_corporativo="teste@empresa.com",
                categoria="Categoria Teste",
                saldo=50000
            ),
            PersonPj(
                faturamento=200000,
                idade=10,
                nome_fantasia="Empresa Teste 2",
                celular="987654321",
                email_corporativo="teste2@empresa.com",
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


def test_list_person_pj():
    mock_conection = MockConnection()
    repo = PersonPjRepository(mock_conection)

    response = repo.list_person_pj()

    mock_conection.session.query.assert_called_once_with(PersonPj)
    query_mock = mock_conection.session.query(PersonPj)
    query_mock.all.assert_called_once()

    assert isinstance(response, list)
    assert len(response) == 2
    assert response[0].nome_fantasia == "Empresa Teste"
