from flask import Flask
from backend.app.extensions import db, migrate
from backend.app.models import Goal

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///studyrescue.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/")
    def home():
        return "StudyRescue Backend is running!"

    return app