from abc import ABC, abstractmethod
from typing import Dict

class PersonPfExtratoControllerInterface(ABC):
    @abstractmethod
    def extrato(self, cliente_id: int) -> Dict:
        pass