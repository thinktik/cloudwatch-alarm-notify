import json

import requests
from requests import Response

from src.dto.event_dto import EventDto
from src.dto.ms_teams_dto import MsTeamsMessage

# Microsoft Teasm WebHook 链接,你需要自行更改为有效的链接
# 下面的链接我移除了公司真实的私有部分
ms_teams_hook_url = 'https://outlook.office.com/webhook/xxxxx'


class MicrosoftTeams:
    """
    Microsoft Teams 类
    """

    def __init__(self, event_dto: EventDto):
        """
        初始化

        :param event_dto: EventDto对象
        """
        self._web_hook = ms_teams_hook_url
        self._event_dto = event_dto

    def send_message(self) -> Response:
        """
        发送消息到Microsoft Teams

        :return: HTTP Response对象
        """
        message = MsTeamsMessage(self._event_dto).gen_message()
        response = requests.post(self._web_hook, data=json.dumps(message))
        return response
