import json

import requests
from requests import Response

from src.dto.event_dto import EventDto
from src.dto.ms_teams_dto import MsTeamsMessage

ms_teams_hook_url = 'https://outlook.office.com/webhook/xxxxx'


class MicrosoftTeams:
    def __init__(self, event_dto: EventDto):
        self._web_hook = ms_teams_hook_url
        self._event_dto = event_dto

    def send_message(self) -> Response:
        message = MsTeamsMessage(self._event_dto).gen_message()
        response = requests.post(self._web_hook, data=json.dumps(message))
        return response
