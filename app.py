# app.py
from flask import Flask, request, json

app = Flask(__name__)

import cardsCatalog

import createCard

import getCard

import getMessages

import healthcheck

import signCard


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')