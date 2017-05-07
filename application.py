from flask import Flask
from flask_orator import Orator, jsonify
import os

app = Flask(__name__)
ORATOR_DATABASES = {
    'default': 'twittor',
    'twittor': {
        'driver': 'sqlite',
        'database': os.path.join(os.path.dirname(__file__), 'twittor.db'),
        'log_queries': True
    }
}
SECRET_KEY = '4K5UA6+BMeyNPgYxhjFU03dYA1NlDGrf3wRr8uOcIHU='

# Creating Flask application
app = Flask(__name__)
app.config.from_object(__name__)
db = Orator(app)

def create_app(**config_overrides):

    #db.init_app(app)

    from user.views import user_app
    app.register_blueprint(user_app)

    from message.views import message_app
    app.register_blueprint(message_app)

    return app