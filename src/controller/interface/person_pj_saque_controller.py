from abc import ABC, abstractmethod
from typing import Dict

class PersonPjSaqueControllerInterface(ABC):
    @abstractmethod
    def saque(self, person_id: int, valor: float) -> Dict:
        pass