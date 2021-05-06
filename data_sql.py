
import pandas as pd 
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, Float, String, ForeignKey, MetaData

# # read in data and preparation

train = pd.read_csv("./data/train.csv")
fullfilment_info = pd.read_csv("./data/fulfilment_center_info.csv")
meal_info = pd.read_csv("./data/meal_info.csv")
test = pd.read_csv("./data/test.csv")

print("data were read in")

# # create empty sql relations

uri = f'postgres://localhost/food_company'
engine = create_engine(uri, echo=False)
metadata = MetaData()

fullfilment_info_empty = Table('fullfilment_info', metadata,
    Column('index', Integer),
    Column('center_id', Integer, primary_key=True),
    Column('city_code', Integer),
    Column('region_code', Integer),
    Column('center_type', String),
    Column('op_area', Float)
    )

meal_info_empty = Table('meal_info', metadata,
    Column('index', Integer),
    Column('meal_id', Integer, primary_key=True),
    Column('category', String),
    Column('cuisine', String)
    )

train_empty = Table('train', metadata,
    Column('index', Integer, primary_key=True),
    Column('week', Integer),
    Column('id', Integer),
    Column('center_id', Integer, ForeignKey('fullfilment_info.center_id')),
    Column('meal_id', Integer, ForeignKey('meal_info.meal_id')),
    Column('checkout_price', Float),
    Column('base_price', Float),
    Column('emailer_for_promotion', Integer),
    Column('homepage_featured', Integer),
    Column('num_orders', Integer)
    )

test_empty = Table('test', metadata,
    Column('index', Integer, primary_key=True),
    Column('week', Integer),
    Column('id', Integer),
    Column('center_id', Integer, ForeignKey('fullfilment_info.center_id')),
    Column('meal_id', Integer, ForeignKey('meal_info.meal_id')),
    Column('checkout_price', Float),
    Column('base_price', Float),
    Column('emailer_for_promotion', Integer),
    Column('homepage_featured', Integer)
    )

metadata.create_all(engine)

print("empty tables were created")

# # upload sql

fullfilment_info.to_sql('fullfilment_info', engine, if_exists='append')
meal_info.to_sql('meal_info', engine, if_exists='append')
train.to_sql('train', engine, if_exists='append')
test.to_sql('test', engine, if_exists='append')

print("data are uploaded to sql db <food_company>")

