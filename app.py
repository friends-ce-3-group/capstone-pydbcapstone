# app.py
from flask import Flask

import statuscodes

app = Flask(__name__)
app.config.from_pyfile("config.py") # run this before any of the other imports to set up the configuration data



#------------------------------------------------

import healthcheck

import cardsCatalog

import getCard

import getMessages

import createCard

import signCard

import sendCard

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')