from abc import ABC, abstractmethod
from typing import Dict

class PersonPfListControllerInterface(ABC):
    @abstractmethod
    def list_person_pf(self) -> Dict:
        pass
