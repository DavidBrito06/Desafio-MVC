from src.controller.interface.person_pf_list_controller import PersonPfListControllerInterface
from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.view.interfaces.view_interface import ViewInterface

class PersonPfListView(ViewInterface):
    def __init__(self, controller: PersonPfListControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest):
        body_response = self.__controller.list_person_pf()

        return HttpResponse(status_code=200, body= body_response)
    

