from src.dto.event_dto import EventDto


class MsTeamsMessage:
    def __init__(self, event_dto: EventDto):
        self._event_dto = event_dto

    def gen_message(self) -> dict:
        # 消息详情
        section = {
            "activityTitle": f"注意: xxx云平台出现了服务告警事件",
            "activitySubtitle": self._event_dto.subject,
            "activityImage": "https://teamsnodesample.azurewebsites.net/static/img/image5.png",
            "facts": [
                {
                    "name": "aws_account_id",
                    "value": self._event_dto.aws_account_id
                },
                {
                    "name": "region",
                    "value": self._event_dto.region
                },
                {
                    "name": "date",
                    "value": self._event_dto.state_change_time
                },
                {
                    "name": "namespace",
                    "value": self._event_dto.namespace
                },
                {
                    "name": "metric_name",
                    "value": self._event_dto.metric_name
                },
                {
                    "name": "alarm_description",
                    "value": self._event_dto.alarm_description
                },
                {
                    "name": "alarm_name",
                    "value": self._event_dto.alarm_name
                },
                {
                    "name": "alarm_arn",
                    "value": self._event_dto.alarm_arn
                },
                {
                    "name": "new_state_reason",
                    "value": self._event_dto.new_state_reason
                }],
            "markdown": True
        }

        message = {
            "@type": "MessageCard",
            "@context": "http://schema.org/extensions",
            # 颜色
            "themeColor": "eb3937",
            "summary": self._event_dto.subject,
            "sections": [section]
        }

        return message
