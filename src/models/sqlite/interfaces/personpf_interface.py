from abc import ABC, abstractmethod
from src.models.sqlite.entites.person_pf import PersonPf

class PersonPfInterface(ABC):

    @abstractmethod
    def sacar_dinheiro(self, cliente_id: int, valor: float) -> bool:
        """Realiza o saque de dinheiro da conta do cliente."""
        pass

    @abstractmethod
    def extrato(self, cliente_id: int) -> PersonPf:
        """Retorna o extrato da conta do cliente."""
        pass