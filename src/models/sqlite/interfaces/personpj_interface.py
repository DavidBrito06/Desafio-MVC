from abc import ABC, abstractmethod
from typing import List
from src.models.sqlite.entites.person_pj import PersonPj

class PersonPjInterfaceRepository(ABC):

    @abstractmethod
    def sacar_dinheiro(self, cliente_id: int, valor: float) -> bool:
        """Realiza o saque de dinheiro da conta do cliente."""
        pass

    @abstractmethod
    def extrato(self, cliente_id: int) -> PersonPj:
        """Retorna o extrato da conta do cliente."""
        pass

    @abstractmethod
    def insert_person_pj(self, faturamento: int, idade: int, nome_fantasia: str, celular: str, email_corporativo: str, categoria: str, saldo: float) -> None:
        """Insere um novo cliente pessoa jurídica no banco de dados."""
        pass

    def list_person_pj(self) -> List[PersonPj]:
        """Lista todos os clientes pessoa jurídica."""
        pass