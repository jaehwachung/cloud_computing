from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json
from pathlib import Path

json_base_path = Path(__file__).resolve().parent
db_config_path = json.load(open(json_base_path / "database.json"))

engine = create_engine('mssql+pyodbc://{user}:{password}@{host}}/{database}?driver=ODBC+Driver+17+for+SQL+Server'.format(**db_config_path), convert_unicode=True, echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine)
