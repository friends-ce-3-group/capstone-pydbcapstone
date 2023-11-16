from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"), override=True)

ENDPOINT = environ.get("ENDPOINT")
DBUSER =  environ.get("DBUSER")
DBPASS =  environ.get("DBPASS")
DBNAME = environ.get("DBNAME")
LAMBDAARN = environ.get("LAMBDAARN")
EVENTBRIDGEIAMROLEARN = environ.get("EVENTBRIDGEIAMROLEARN")
ACCESS_KEY_ID = environ.get("ACCESS_KEY_ID")
ACCESS_KEY = environ.get("ACCESS_KEY")