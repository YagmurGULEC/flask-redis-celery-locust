from flask import Flask
from .views import main
from .utils import make_celery


def create_app():
    app = Flask(__name__)

    app.config['CELERY_CONFIG'] ={"broker_url": "redis://redis", "result_backend": "redis://redis"}
    app.config['UPLOAD_PATH'] = 'uploads'

    celery=make_celery(app)
    celery.set_default()
    app.register_blueprint(main)
    return app,celery