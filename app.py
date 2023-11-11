# app.py
from flask import Flask, request, json

app = Flask(__name__)
app.config.from_pyfile("config.py") # run this before any of the other imports

import cardsCatalog

import createCard

import getCard

import getMessages

import healthcheck

import signCard

import testDBconnect

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')