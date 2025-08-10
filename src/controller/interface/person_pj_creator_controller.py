from abc import ABC, abstractmethod
from typing import Dict

class PersonPjCreatorControllerInterface(ABC):
    @abstractmethod
    def create_personpj(self, personpf_data: Dict) -> Dict:
        pass
