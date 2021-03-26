from domain import valueobjects
from validate_docbr import CNPJ
from typing import Optional
from pydantic import (
    BaseModel,
    validator,
    Field
)


class Employer(BaseModel):
    """
    {
      "id": 1,
      "tradingName": "Adega da Cerveja - Pinheiros",
      "ownerName": "Zé da Silva",
      "document": "1432132123891/0001",
      "coverageArea": {
        "type": "MultiPolygon",
        "coordinates": [
          [[[30, 20], [45, 40], [10, 40], [30, 20]]],
          [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]]
        ]
      },
      "address": {
        "type": "Point",
        "coordinates": [-46.57421, -21.785741]
      }
    }
    """
    id: str
    tradingName: str
    ownerName: str
    document: str
    address: valueobjects.Point
    coverageArea: valueobjects.MultiPolygon

    @validator('document')
    def check_document(cls, v):
        if validate_document(v):
            return v.title()
        else:
            raise ValueError('cnpj is not valid')

    @validator('ownerName')
    def check_owner_name(cls, v):
        if validate_names(v):
            return v.title()
        else:
            raise ValueError('Owner Name is not valid, should one or more words')

    @validator('tradingName')
    def check_trading_name(cls, v):
        if validate_names(v):
            return v.title()
        else:
            raise ValueError('Owner Name is not valid, should one or more words')


def validate_document(document: str) -> bool:
    cnpj = CNPJ()
    if not cnpj.validate(document):
        return True
    else:
        return False


def validate_names(owner_name: str) -> bool:
    if len(owner_name.split(' ')) >= 2:
        return True
    else:
        return False
