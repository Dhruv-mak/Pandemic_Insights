import click
from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import text
from db import db_obj
from scripts import cli_bp

from routes import api
app = Flask(__name__)
app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(cli_bp)


if __name__ == "__main__":
    app.run(debug=True)