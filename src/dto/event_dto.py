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
        """
        AWS CloudWatch alram消息中的Subject

        :return: Subject字符串
        """
        return self.__subject

    @property
    def message(self) -> dict:
        """
        AWS CloudWatch alram消息中的Message
        :return: Message
        """
        return self._message

    @property
    def alarm_name(self):
        """
        AWS CloudWatch alram消息中的AlarmName
        :return: AlarmName
        """
        return self._alarm_name

    @property
    def alarm_description(self):
        """
        AWS CloudWatch alram消息中的 AlarmDescription
        :return: AlarmDescription
        """
        return self._alarm_description

    @property
    def aws_account_id(self):
        """
        AWS CloudWatch alram消息中的 AWSAccountId
        :return: AWSAccountId
        """
        return self._aws_account_id

    @property
    def new_state_reason(self):
        """
        AWS CloudWatch alram消息中的 NewStateReason
        :return: NewStateReason
        """
        return self._new_state_reason

    @property
    def state_change_time(self):
        """
        AWS CloudWatch alram消息中的 StateChangeTime
        :return: StateChangeTime
        """
        return self._state_change_time

    @property
    def region(self):
        """
        AWS CloudWatch alram消息中的 Region
        :return: Region
        """
        return self._region

    @property
    def metric_name(self):
        """
        AWS CloudWatch alram消息中的 MetricName
        :return: MetricName
        """
        return self._metric_name

    @property
    def namespace(self):
        """
        AWS CloudWatch alram消息中的 Namespace
        :return: Namespace
        """
        return self._namespace

    @property
    def alarm_arn(self):
        """
        AWS CloudWatch alram消息中的 AlarmArn
        :return: AlarmArn
        """
        return self._alarm_arn
