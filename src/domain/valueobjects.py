from pydantic import (
    BaseModel,
    Field
)
from typing import (
    List
)


class Coordinate(BaseModel):
    longitude: float
    latitude: float


class Region(BaseModel):
    type: str = Field("MultiPolygon", const=True)
    coverageArea: List[List[Coordinate]]


class Address(BaseModel):
    type: str = Field("Point", const=True)
    coordinate: Coordinate
