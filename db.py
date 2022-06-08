import databases
import sqlalchemy

metadata = sqlalchemy.MetaData()
database = databases.Database("sqlite:///db.sqlite3")
engine = sqlalchemy.create_engine("sqlite:///db.sqlite3")
