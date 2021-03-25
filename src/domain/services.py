from infra import repository as repo
from domain import (
    exceptions,
    valueobjects,
    entities
)


def create_new_employer(employer: entities.Employer):
    repo.create_employer(employer)
    return {'message': 'objeto salvo com sucesso', 'objeto': employer.dict()}


def get_employer_most_nearest(point: valueobjects.Point) -> entities.Employer:
    employer = repo.get_nearest_employer_in_coverage_area(point)
    if not employer:
        raise exceptions.AddressNotInCoverageArea
    else:
        return employer
