from sqlalchemy import (
   create_engine,
   Column,
   Integer,
   String,
   Float,
   Boolean,
   Date,
)
from sqlalchemy.schema import Table, MetaData
from sqlalchemy.orm import sessionmaker
import pandas as pd
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Items(Base):
   __tablename__ = "customers_rfm"
   id = Column(
       "id", Integer, primary_key=True, autoincrement=True
   )
   email = Column("email", String, unique=False)
   recency = Column("recency", Integer, unique=False)
   frequency = Column("frequency", Integer, unique=False)
   monetary_value = Column(
       "monetary_value", Float, unique=False
   )
   last_purchase = Column(
       "last_purchase", Date, unique=False
   )
   first_purchase = Column(
       "first_purchase", Date, unique=False
   )



class PostgreSQL:
   def __init__(
       self,
       username,
       password,
       host,
       schema,
       my_dataframe=None,
       data_types=None,
   :disappointed:
       self.username = username
       self.password = password
       self.host = host
       self.schema = schema
       self.my_dataframe = my_dataframe
       self.data_types = data_types
       self.engine = create_engine(
           f"postgresql+psycopg2://{self.username}:{self.password}@{self.host}",
           connect_args={
               "options": f"-csearch_path={self.schema}"
           },
       )
       self.index_name = "id"

   def check_status(self):
       return self.engine.connect()

   def get_data(self, table_to_get):
       metadata = MetaData(self.engine)
       metadata.reflect()

       table = Table(
           f"{table_to_get}",
           metadata,
           autoload=True,
           autoload_with=self.engine,
       )

       Session = sessionmaker(bind=self.engine.connect())

       session = Session()

       dataframe = pd.read_sql(
           table.select(), session.bind
       )

       session.close()
       return dataframe

   def save_data(self, table_to_save=None, template=None):
       Session = sessionmaker(bind=self.engine.connect())

       session = Session()

       session.bulk_insert_mappings(
           template,
           table_to_save.to_dict(orient="records"),
       )

       session.commit()
       session.close()