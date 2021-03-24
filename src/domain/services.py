from infra import repository as repo
from domain import (
    exceptions,
    valueobjects,
    entities
)


def create_new_employer(employer: entities.Employer) -> entities.Employer:
    new_employer = repo.create_employer(employer)
    return new_employer


def get_employer_most_nearest(point: valueobjects.Address) -> entities.Employer:
    employer = repo.get_nearest_employer_in_coverage_area(point)
    if not employer:
        raise exceptions.AddressNotInCoverageArea
    else:
        return employer
