# xxx平台监控系统-消息通知服务

这个项目是DevOps体系中,服务监控系统的一个组件,用于向developer及时发布服务相关的警告提醒developer排除问题.

详细设计请看: [AWS CloudWatch 发送警告到Microsoft Teams,微信以及钉钉](https://www.omoz.cc/15809114b12031215384534e2c6995e2/)

注意: 这是一个使用[serverless](https://www.serverless.com)编排的`AWS Lambda`项目,全部的敏感信息已经被移除,所以你需要了解serverless和AWS Lambda才能正确的运行这个项目.

不过由于逻辑相对很简单,直接借鉴逻辑也能使用其他语言轻易的实现.

## 参考链接

- [What are webhooks and connectors?](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/what-are-webhooks-and-connectors)
- [Sending messages to connectors and webhooks](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/connectors-using)
- [cloudwatch-alarm-to-microsoft-teams](https://marbot.io/blog/cloudwatch-alarm-to-microsoft-teams.html)
- [企业微信、钉钉接收 Amazon CloudWatch 告警](https://amazonaws-china.com/cn/blogs/china/enterprise-wechat-and-dingtalk-receiving-amazon-cloudwatch-alarms/)

## 本地调试

你可以在UNIX命令行中执行下面的语句验证是否可以发送消息到Microsoft Teams

```
curl -H 'Content-Type: application/json' -d '{"text": "Hello World"}' https://outlook.office.com/webhook/xxxx
```

如果你要发送有格式的富文本这个例子也不错

```
curl -H 'Content-Type: application/json' -d '{
    "@type": "MessageCard",
    "@context": "http://schema.org/extensions",
    "themeColor": "eb3937",
    "summary": "注意: xxx平台出现了服务告警事件",
    "sections": [{
        "activityTitle": "注意: xx云平台出现了服务告警事件",
        "activitySubtitle": "xx云平台",
        "activityImage": "https://teamsnodesample.azurewebsites.net/static/img/image5.png",
        "facts": [{
            "name": "Assigned to",
            "value": "Unassigned"
        }, {
            "name": "Due date",
            "value": "Mon May 01 2017 17:07:18 GMT-0700 (Pacific Daylight Time)"
        }, {
            "name": "Status",
            "value": "Not started"
        }],
        "markdown": true
    }],
    "potentialAction": [{
        "@type": "ActionCard",
        "name": "Add a comment",
        "inputs": [{
            "@type": "TextInput",
            "id": "comment",
            "isMultiline": false,
            "title": "Add a comment here for this task"
        }],
        "actions": [{
            "@type": "HttpPOST",
            "name": "Add comment",
            "target": "http://..."
        }]
    }, {
        "@type": "ActionCard",
        "name": "Set due date",
        "inputs": [{
            "@type": "DateInput",
            "id": "dueDate",
            "title": "Enter a due date for this task"
        }],
        "actions": [{
            "@type": "HttpPOST",
            "name": "Save",
            "target": "http://..."
        }]
    }, {
        "@type": "ActionCard",
        "name": "Change status",
        "inputs": [{
            "@type": "MultichoiceInput",
            "id": "list",
            "title": "Select a status",
            "isMultiSelect": "false",
            "choices": [{
                "display": "In Progress",
                "value": "1"
            }, {
                "display": "Active",
                "value": "2"
            }, {
                "display": "Closed",
                "value": "3"
            }]
        }],
        "actions": [{
            "@type": "HttpPOST",
            "name": "Save",
            "target": "http://..."
        }]
    }]
}' https://outlook.office.com/webhook/xxxxx
```