from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("RENDER_DATABASE_URI")
        # app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        #     "SQLALCHEMY_DATABASE_URI")

    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")

    # Import models here for Alembic setup
    # from app.models.ExampleModel import ExampleModel
    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.board import Board
    from app.models.card import Card

    # Register Blueprints here
    # from .routes import example_bp
    from .cards_routes import cards_bp
    from .boards_routes import boards_bp

    # app.register_blueprint(example_bp)
    app.register_blueprint(cards_bp)
    app.register_blueprint(boards_bp)



    CORS(app)
    return app
