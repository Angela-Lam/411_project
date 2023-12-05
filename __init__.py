"""Setup at app startup"""
import sys
import os
import sqlalchemy
from flask import Flask, jsonify
from yaml import load, Loader
#from app import app
#from app import databases as db_help

def init_connection_engine():
    """ initialize database setup
    Takes in os variables from environment if on GCP
    Reads in local variables that will be ignored in public repository.
    Returns:
        pool -- a connection to GCP MySQL
    """

    # detect env local or gcp
    if os.environ.get('GAE_ENV') != 'standard':
        try:
            variables = load(open("app.yaml"), Loader=Loader)
        except OSError as e:
            print("Make sure you have the app.yaml file setup")
            os.exit()

        env_variables = variables['env_variables']
        for var in env_variables:
            os.environ[var] = env_variables[var]

    return sqlalchemy.create_engine(
        "mysql+pymysql://root:NickHazelAngela105@35.238.52.242:3306/stage3relations"
    )

app = Flask(__name__)

db = init_connection_engine()
# conn= db.connect()
# conn.close()

# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
