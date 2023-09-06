from sqlalchemy import create_engine, URL
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from yaml import load, Loader

application_settings = load(open("/opt/shop2.yml"), Loader)

DB_HOST = application_settings.get("DB_HOST")
DB_USER = application_settings.get("DB_USER")
DB_PASSWD = application_settings.get("DB_PASSWD")
DB_NAME = application_settings.get("DB_NAME")

url_object = URL.create("postgresql+pg8000",
    username=DB_USER,
    password=DB_PASSWD,
    host=DB_HOST,
    database=DB_NAME)

engine = create_engine(url_object, echo=False)
db_session = scoped_session(sessionmaker(autocommit=False,
                                        autoflush=False,
                                        bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import knou_shop2.models
    Base.metadata.create_all(bind=engine)
