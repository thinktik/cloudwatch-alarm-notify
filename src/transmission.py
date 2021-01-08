# lambda event事件处理器
from src.dto.event_dto import EventDto
from src.ms_teams import MicrosoftTeams


def lambda_handler(event, context):
    records = event['Records']
    for record in records:
        event_dto = EventDto(record)
        microsoft_teams = MicrosoftTeams(event_dto)
        microsoft_teams.send_message()
    return None
