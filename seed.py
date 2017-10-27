#!/usr/bin/env python

import os
import time
import math

import pandas as pd

from sqlalchemy import *

from source.utils import map_values


def as_list_of_dicts(csv_path):
    def float_to_int(x):
        if isinstance(x, float):
            if math.isnan(x):
                return None
            return int(x)
        return x

    return [map_values(float_to_int, dict(row[1])) for row in pd.read_csv(csv_path).iterrows()]


print("connecting to database...")
psql = create_engine('postgresql://postgres:{}@db/postgres'.format(os.environ['POSTGRES_PASSWORD']))
# psql = create_engine('postgresql://postgres:inkitt@localhost/postgres')

while True:
    try:
        psql.execute('SELECT 1')
        break
    except Exception as exc:
        print("waiting for connection...")
        time.sleep(2)

print("ok.")

metadata = MetaData()

visits = Table('visits', metadata,
               Column('visitor_id', CHAR(36)),
               Column('user_id', INTEGER),
               Column('country', VARCHAR(60)),
               Column('timezone', VARCHAR(100)),
               Column('location_accuracy', INTEGER))

reading = Table('reading', metadata,
                Column('is_app_event', BOOLEAN),
                Column('visitor_id', CHAR(36)),
                Column('id', CHAR(36)),
                Column('visit_id', VARCHAR(100)),
                Column('tracking_time', TIMESTAMP),
                Column('created_at', TIMESTAMP),
                Column('story_id', INTEGER),
                Column('user_id', INTEGER))

stories = Table('stories', metadata,
                Column('id', INTEGER),
                Column('user_id', INTEGER),
                Column('teaser', VARCHAR(500)),
                Column('title', VARCHAR(100)),
                Column('cover', CHAR(36)),
                Column('category_one', VARCHAR(20)),
                Column('category_two', VARCHAR(20)))

print("creating tables...")
metadata.create_all(psql)
print("ok.")

print("inserting data...")
conn = psql.connect()
conn.execute(visits.insert(), as_list_of_dicts('data/visits.csv'))
conn.execute(reading.insert(), as_list_of_dicts('data/reading.csv'))
conn.execute(stories.insert(), as_list_of_dicts('data/stories.csv'))
print("ok.")
