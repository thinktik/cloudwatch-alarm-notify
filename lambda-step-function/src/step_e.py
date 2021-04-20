import json
import os
from time import time


def lambda_handler(event, context):
    region = os.environ['AWS_REGION']

    # 构造返回体的数据
    body = {
        "developer": "ThinkTik",
        "echo": "Serverless Step Function 演练",
        "AWS accountId": event['requestContext']['accountId'],
        "AWS stage": event['requestContext']['stage'],
        "AWS region": region,
        "timestamp": int(time())
    }
    # 返回json内容
    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }
