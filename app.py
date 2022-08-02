from flask import Flask
from apps.core.database import db
from flask_migrate import Migrate
from apps.posts import posts


class Config:
    DEBUG = True


def get_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    app.config.from_object(Config)
    app.register_blueprint(posts)
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)
    return app


application = get_app()

if __name__ == "__main__":

    application.run(host="0.0.0.0", port=5000,debug=True)
