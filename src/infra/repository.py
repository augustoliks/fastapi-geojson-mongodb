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

db[COL_EMPLOYERS].create_index([("coverageArea", GEOSPHERE)])
db[COL_EMPLOYERS].create_index([("address", GEOSPHERE)])


def get_employer(field: dict) -> entities.Employer:
    obj = db[COL_EMPLOYERS].find_one(field)
    return entities.Employer(**obj)


def create_employer(employer: entities.Employer):
    db[COL_EMPLOYERS].insert_one(employer.dict(exclude={'id'}))


def get_nearest_employer_in_coverage_area(address: valueobjects.Point) -> entities.Employer:
    return db[COL_EMPLOYERS].find({
        "$and": [
            {
                "coverageArea": {
                    "$geoIntersects": {
                        "$geometry": address.dict()
                    }
                }
            },
            {
                "address": {
                    "$nearSphere": {
                        "$geometry": address.dict()
                    }
                }
            }
        ]
    })[0]