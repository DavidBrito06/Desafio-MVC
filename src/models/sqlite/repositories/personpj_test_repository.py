from unittest import mock
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entites.person_pj import PersonPj
from .personpj_repository import PersonPjRepository
from unittest.mock import MagicMock


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


def test_sacar_dinheiro():
    # Mock da conexão e da sessão
    mock_connection = MockConnection()
    repo = PersonPjRepository(mock_connection)

    # Configura o retorno do método query().filter_by().one() para um objeto mock com saldo real
    cliente_mock = MagicMock()
    cliente_mock.saldo = 150.0  # saldo maior que o valor para teste
    mock_connection.session.query.return_value.filter_by.return_value.one.return_value = cliente_mock

    resultado = repo.sacar_dinheiro(cliente_id=1, valor=100.0)
    assert resultado == True
    print(cliente_mock.saldo)  # Deve ser 50.0 após o saque

from unittest.mock import MagicMock

def test_extrato():
    mock_connection = MockConnection()
    repo = PersonPjRepository(mock_connection)

    # Criando um cliente mock com atributos reais
    cliente_mock = MagicMock()
    cliente_mock.nome_fantasia = "Empresa Teste"
    cliente_mock.saldo = 200.0

    # Configurando a cadeia de chamadas para retornar o cliente_mock
    mock_connection.session.query.return_value.filter_by.return_value.one.return_value = cliente_mock

    response = repo.extrato(cliente_id=1)

    assert response.nome_fantasia == "Empresa Teste"
    assert response.saldo == 200.0
