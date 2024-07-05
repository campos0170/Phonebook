import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir,'.env'))

class Config():
    """

    Set config variables for the flask app
    using Environment variables where available.
    Otherwise, create th configuration variable if not done already.
    
    """

    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'On the way to a PhD'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite://' + os.path.join(basedir,'app.bd')
    SQLALCHEMY_TRACK_NOTIFICATIONS = False