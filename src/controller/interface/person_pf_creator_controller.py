from abc import ABC, abstractmethod
from typing import Dict

class PersonPfCreatorControllerInterface(ABC):
    @abstractmethod
    def create_personpf(self, personpf_data: Dict) -> Dict:
        pass





