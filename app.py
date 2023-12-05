# app.py
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
app.config.from_pyfile("config.py") # run this before any of the other imports to set up the configuration data
metrics = PrometheusMetrics(app)

#------------------------------------------------

import healthcheck  # /api/healthcheck

import cardsCatalog # /api/cardsCatalog

import getCard      # /api/getCard?cardId=XXXX

import getMessages  # /api/getMessages?cardId=XXXX

import createCard   # curl -d '{"id" : "", "imageKey" : "", "imageCategory" : "", "imagePath" : "", "imageBackgroundColor" : "", "recipientName" : "", "recipientEmail" : "", "senderName" : "", "senderEmail" : "", "sendDate" : "", "sendTime" : "", "sendTimezone" : "", "createdDataTime" : ""}' -X POST /api/createCard

import signCard     # curl -d '{"id" : "", "cardId" : "", "name" : "", "message" : "", "wordCount" : "", "createdDateTime" : ""}' -X POST /api/signCard

# import sendCard     # /api/sendCard?cardId=XXXX

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')