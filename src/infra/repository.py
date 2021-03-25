from conf import settings
from domain import (
    entities,
    valueobjects
)

from pymongo import (
    GEOSPHERE,
    MongoClient
)


DB_NAME = 'delivery'
COL_EMPLOYERS = 'employers'

db_client = MongoClient(**settings['db'])

db = db_client[DB_NAME]


def setup_database():
    db[COL_EMPLOYERS].create_index([("coverageArea", GEOSPHERE)])
    db[COL_EMPLOYERS].create_index([("address", GEOSPHERE)])


def get_employer(field: dict) -> entities.Employer:
    obj = db[COL_EMPLOYERS].find_one(field)
    return entities.Employer(**obj)


def create_employer(employer: entities.Employer) -> entities.Employer:
    obj = db[COL_EMPLOYERS].insert_one(employer.dict(exclude={'id'}))
    return entities.Employer(**obj)


def get_nearest_employer_in_coverage_area(address: valueobjects.Address) -> entities.Employer:
    ...
