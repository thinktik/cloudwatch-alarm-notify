import json


class EventDto:
    def __init__(self, record: dict):
        self.__subject = record['Sns']['Subject']
        self._message = json.loads(record['Sns']['Message'])
        self._alarm_name = self._message['AlarmName']
        self._alarm_description = self._message['AlarmDescription']
        self._aws_account_id = self._message['AWSAccountId']
        self._new_state_reason = self._message['NewStateReason']
        self._state_change_time = self._message['StateChangeTime']
        self._region = self._message['Region']
        self._metric_name = self._message['Trigger']['MetricName']
        self._namespace = self._message['Trigger']['Namespace']
        self._alarm_arn = self._message['AlarmArn']

    @property
    def subject(self) -> str:
        return self.__subject

    @property
    def message(self):
        return self._message

    @property
    def alarm_name(self):
        return self._alarm_name

    @property
    def alarm_description(self):
        return self._alarm_description

    @property
    def aws_account_id(self):
        return self._aws_account_id

    @property
    def new_state_reason(self):
        return self._new_state_reason

    @property
    def state_change_time(self):
        return self._state_change_time

    @property
    def region(self):
        return self._region

    @property
    def metric_name(self):
        return self._metric_name

    @property
    def namespace(self):
        return self._namespace

    @property
    def alarm_arn(self):
        return self._alarm_arn
