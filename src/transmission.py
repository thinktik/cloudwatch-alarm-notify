from src.dto.event_dto import EventDto
from src.ms_teams import MicrosoftTeams


# aws lambda event事件处理器
def lambda_handler(event, context):
    # 获取AWS SNS传入的警告消息列表
    records = event['Records']
    # 对每个警告消息进行转发处理
    for record in records:
        # 提取警告消息的有效内容
        event_dto = EventDto(record)
        # 使用提取出的有效内容构造出MicrosoftTeams对象
        microsoft_teams = MicrosoftTeams(event_dto)
        # 发送到Microsoft Teams
        microsoft_teams.send_message()

    # 完成,由于这个Lambda不需要提供返回值给AWS SNS,所以直接返回None即可
    return None
