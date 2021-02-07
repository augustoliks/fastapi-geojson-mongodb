import pymongo
from domain import entities

COLLECTIONS_EMPLOYERS = 'employers'


def make_database(database_properties) -> pymongo.MongoClient:
    return pymongo.MongoClient(**database_properties)


def create_employer(db: pymongo.MongoClient, employer: dict) -> str:
    identifier = db[COLLECTIONS_EMPLOYERS].insert(employer)
    return identifier


def get_nearest_employer_in_coverage_area(db: pymongo.MongoClient, employer: entities.Employer) -> str:
    identifier = db[COLLECTIONS_EMPLOYERS].get(employer)
    return identifier
