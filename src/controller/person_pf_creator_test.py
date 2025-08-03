from .person_pf_creator import PersonPfCreator

class MockPersonPf:
    def insert_person_pf(self, renda_mensal, idade, nome_completo, celular, email, categoria, saldo):
        return True

def test_create_personpf():
    mock_repository = MockPersonPf()
    creator = PersonPfCreator(mock_repository)

    personpf_data = {
        'renda_mensal': 5000.00,
        'idade': 30,
        'nome_completo': 'David Silva',
        'celular': '11999999999',
        'email': 'contato@empresa.com',
        'categoria': 'Tecnologia',
        'saldo': 5000.00
    }

    created_personpf = creator.create_personpf(personpf_data)

    assert created_personpf == personpf_data