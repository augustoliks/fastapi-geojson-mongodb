from mock import patch
import pytest


@pytest.fixture()
def employer_rio_grande_do_sul():
    yield {
        "id": 0,
        "tradingName": "string",
        "ownerName": "Carlos",
        "document": "string",
        "address": {
            "coordinate": {
                "longitude": 0,
                "latitude": 0
            },
            "type": "Point"
        },
        "coverageArea": {
            "coordinates": [
                [
                    [
                        -57.6123046875,
                        -30.145127183376115
                    ],
                    [
                        -53.12988281249999,
                        -32.842673631954305
                    ],
                    [
                        -49.3505859375,
                        -28.613459424004414
                    ],
                    [
                        -53.96484375,
                        -27.019984007982554
                    ],
                    [
                        -57.6123046875,
                        -30.145127183376115
                    ]
                ]
            ]
        }
    }

from infra.database import db
@patch('infra.database.db', None)
def test_employer(employer_rio_grande_do_sul):
    from domain.entities import Employer
    print('carlos')
    employer = Employer(**employer_rio_grande_do_sul)
