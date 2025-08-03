from .person_pj_creator import PersonPjCreator

class MockPersonPj:
    def insert_person_pj(self, faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo):
        return True

def test_create_personpj():
    mock_repository = MockPersonPj()
    creator = PersonPjCreator(mock_repository)

    personpj_data = {
        'faturamento': 10000.00,
        'idade': 30,
        'nome_fantasia': 'Empresa Teste',
        'celular': '11999999999',
        'email_corporativo': 'contato@empresa.com',
        'categoria': 'Tecnologia',
        'saldo': 5000.0
    }

    created_personpj = creator.create_personpj(personpj_data)

    assert created_personpj == personpj_data