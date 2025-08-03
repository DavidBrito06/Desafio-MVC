from abc import ABC, abstractmethod

class ClienteInterface(ABC):

    @abstractmethod
    def sacar_dinheiro(self, valor: float) -> bool:
        """Realiza o saque de dinheiro da conta do cliente."""
        pass

    @abstractmethod
    def realizar_extrato(self) -> str:
        """Realiza o extrato da conta do cliente."""
        pass