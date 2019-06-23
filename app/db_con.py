import psycopg2
import os

# url = "dbname='store_manager'
#  host='localhost' port='5432' user='postgres' password='postgres'"

db_url = os.getenv('DATABASE_URL')


def connection():
    conn = psycopg2.connect(db_url)
    conn.autocommit = True
    return conn


def create_tables():
    curr = connection().cursor()
    queries = tables()
    for query in queries:
        curr.execute(query)


def destroy_tables():
    pass


def tables():
    db1 = """CREATE TABLE IF NOT EXISTS projects (
        project_id serial PRIMARY KEY NOT NULL,
        projectName character varying(1000) NOT NULL,
        status TEXT,
        budget numeric NOT NULL,
        duration numeric NOT NULL
        );"""

    db2 = """CREATE TABLE IF NOT EXISTS users (
        id serial PRIMARY KEY,
        email  VARCHAR NOT NULL,
        password VARCHAR NOT NULL,
        admin BOOLEAN NOT NULL
        );"""

    queries = [db1, db2]
    return queries
