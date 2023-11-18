# capstone-pydbcapstone
REST APIs for interacting with RDS. Made with Flask.


healthcheck:

```/api/healthcheck```


cardsCatalog:

```/api/cardsCatalog```


getCard:

```/api/getCard?cardId=XXXX```


getMessages:

```/api/getMessages?cardId=XXXX```


createCard:

```curl -d '{"id" : "", "imageKey" : "", "imageCategory" : "", "imagePath" : "", "imageBackgroundColor" : "", "recipientName" : "", "recipientEmail" : "", "senderName" : "", "senderEmail" : "", "sendDate" : "", "sendTime" : "", "sendTimezone" : "", "createdDataTime" : ""}' -X POST /api/createCard```


signCard:

```curl -d '{"id" : "", "cardId" : "", "name" : "", "message" : "", "wordCount" : "", "createdDateTime" : ""}' -X POST /api/signCard```