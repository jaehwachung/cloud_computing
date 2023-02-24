from sqlalchemy import create_engine, URL
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
import json
import os

valut_host = os.environ.get("VALUT_HOST")

credential = DefaultAzureCredential()
client = SecretClient(vault_url=f"https://{valut_host}.vault.azure.net", credential=credential)

json_path = "knou_shop2/database.json"
db_config_path = json.load(open(json_path))

url_object = URL.create(
    "postgresql+psycopg",
    username=db_config_path['user'],
    password=client.get_secret('pgpasswd'),
    host=db_config_path['host'],
    database=db_config_path['database'],
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
    import models
    Base.metadata.create_all(bind=engine)
