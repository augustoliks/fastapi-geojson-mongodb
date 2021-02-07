from . import valueobjects
from validate_docbr import CNPJ
from pydantic import (
    BaseModel,
    validator
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
    id: int
    tradingName: str
    ownerName: str
    document: str
    address: valueobjects.Address
    coverageArea: valueobjects.Region

    @validator('document')
    def validate_document(cls, v):
        cnpj = CNPJ()
        if not cnpj.validate(v):
            raise ValueError('cnpj is not valid')
        else:
            return v.title()
