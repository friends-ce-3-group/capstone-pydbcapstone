from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

ENDPOINT = environ.get("ENDPOINT")
DBUSER =  environ.get("DBUSER")
DBPASS =  environ.get("DBPASS")
DBNAME = environ.get("DBNAME")