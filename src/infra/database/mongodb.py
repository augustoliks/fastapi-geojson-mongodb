from domain import entities
from pymongo import (
    GEO2D,
    MongoClient
)

DATABASE_NAME = 'augustoliksdb'
COLLECTION_REGIONS = 'regions'
COLLECTIONS_EMPLOYERS = 'employers'


def make_database(database_properties) -> MongoClient:
    return MongoClient(**database_properties)


def setup_database(db: MongoClient):
    database = db[DATABASE_NAME]
    database[COLLECTION_REGIONS].create_index([("address", GEO2D)])
    database[COLLECTIONS_EMPLOYERS].create_index([("coverageAddress", GEO2D)])


def create_employer(db: MongoClient, employer: dict) -> str:
    identifier = db[COLLECTIONS_EMPLOYERS].insert(employer)
    return identifier


def get_nearest_employer_in_coverage_area(db: MongoClient, employer: entities.Employer) -> str:
    identifier = db[COLLECTIONS_EMPLOYERS].get(employer)
    return identifier
