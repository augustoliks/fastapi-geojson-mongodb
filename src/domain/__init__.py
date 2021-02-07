from infra.database import db
from . import (
    entities,
    valueobjects
)


def create_new_employer(employer: entities.Employer) -> dict:
    employer_id = db.create_employer(employer)
    return {'status': 'employer saved with success', 'employer_id': employer_id}


def get_employer_most_nearest(point: valueobjects.Address):
    db.get_nearest_employer_in_coverage_area(point)
