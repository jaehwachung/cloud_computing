from sqlalchemy import create_engine, URL
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
import os

VALUT_HOST = os.environ.get("VALUT_HOST")
DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_NAME = os.environ.get("DB_NAME")

credential = DefaultAzureCredential()
client = SecretClient(vault_url=f"https://{VALUT_HOST}.vault.azure.net", credential=credential)

url_object = URL.create(
    "postgresql+psycopg",
    username=DB_USER,
    password=client.get_secret('MALL-DB-PASSWORD'),
    host=DB_HOST,
    database=DB_NAME,
)

engine = create_engine(url_object, convert_unicode=True, echo=False)
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
