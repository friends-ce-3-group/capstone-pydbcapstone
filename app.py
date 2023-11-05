# app.py
from flask import Flask, request

app = Flask(__name__)

@app.route('/api/healthcheck', methods=['GET'])
def healthcheck():
    return "healthcheck"

@app.route('/api/cardsCatalog', methods=['GET'])
def cardsCatalog():
    return "cardsCatalog"

@app.route('/api/createCard', methods=['POST'])
def createCard():
    return "createCard"

@app.route('/api/signCard', methods=['POST'])
def signCard():
    return "signCard"

@app.route('/api/getCard', methods=['GET'])
def getCard():
    cardId = request.args.get('cardId')
    return "getCard; cardId = {0}".format(cardId)

@app.route('/api/getMessages', methods=['GET'])
def getMessages():
    cardId = request.args.get('cardId')
    return "getMessages; cardId = {0}".format(cardId)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')