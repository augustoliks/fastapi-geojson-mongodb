from domain import entities
from pymongo import (
    GEO2D,
    MongoClient
)

DATABASE_NAME = 'augustoliksdb'
COLLECTION_REGIONS = 'regions'
COLLECTIONS_EMPLOYERS = 'employers'

db_driver: MongoClient


def make_database(database_properties):
    global db_driver
    db_driver = MongoClient(**database_properties)


def setup_database(db: MongoClient):
    database = db[DATABASE_NAME]
    database[COLLECTION_REGIONS].create_index([("address", GEO2D)])
    database[COLLECTIONS_EMPLOYERS].create_index([("coverageAddress", GEO2D)])


def create_employer(employer: entities.Employer) -> str:
    database = db_driver[DATABASE_NAME]
    identifier = database[COLLECTIONS_EMPLOYERS].insert_one(employer.dict()).inserted_id
    return str(identifier)


def get_nearest_employer_in_coverage_area(employer: entities.Employer) -> str:
    ...
