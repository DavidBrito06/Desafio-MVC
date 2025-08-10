from abc import ABC, abstractmethod
from typing import Dict

class PersonPjExtratoControllerInterface(ABC):
    @abstractmethod
    def extrato(self, cliente_id: int) -> Dict:
        pass