from abc import ABC, abstractmethod
from typing import Dict

class PersonPjListControllerInterface(ABC):
    @abstractmethod
    def list_person_pj(self) -> Dict:
        pass