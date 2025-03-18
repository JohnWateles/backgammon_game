from sqlalchemy import create_engine
import json

from .db_models import Base


db_config = {
    "host": "localhost",
    "database": "mydb",
    "user": "postgres",
    "password": "03022005",
    "port": "5432"
}

user = db_config["user"]
password = db_config["password"]
host = db_config["host"]
port = db_config["port"]
db_name = db_config["database"]

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base.metadata.create_all(bind=engine)
