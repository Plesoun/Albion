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
   __tablename__ = tablename
   id = Column(
       "id", Integer, primary_key=True, autoincrement=True
   )
   buy_price_max = Column("buy_price_max", Integer, unique=False)
   buy_price_min = Column("buy_price_min", Integer, unique=False)
   city = Column("city", String, unique=False)
   item_id = Column(
       "item_id", String, unique=False
   )
   quality = Column(
       "quality", Integer, unique=False
   )
   sell_price_max = Column(
       "sell_price_max", Integer, unique=False
   )
   sell_price_max_date = Column(
       "sell_price_max_date", Date, unique=False
   )
   sell_price_min = Column(
       "sell_price_min", Integer, unique=False
   )
   sell_price_min_date = Column(
       "sell_price_min_date", Date, unique=False
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
       tablename=None
   ):
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
       self.tablename = tablename

   def check_status(self):
       return self.engine.connect()

   def get_data(self, table_to_get):
       metadata = MetaData(self.engine)
       metadata.reflect()
       
       tablename = self.tablename
       
       table = Items(
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