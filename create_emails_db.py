from email_models import Base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///emails.sqlite', echo=True)
Base.metadata.create_all(engine)


