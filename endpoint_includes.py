from app import app
from flask import request
from DBConnect import DBConnector
from cors import cors_preflight_response, cors_response
import json
import statuscodes
import tablenames