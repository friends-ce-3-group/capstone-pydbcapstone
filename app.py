# app.py
from flask import Flask, Request

app = Flask(__name__)
app.config.from_pyfile("config.py") # run this before any of the other imports to set up the configuration data

import DBConnect # run this to initialize the DB

import cardsCatalog

import createCard

import getCard

import getMessages

import healthcheck

import signCard

import testDBconnect

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')