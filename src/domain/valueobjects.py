from pydantic import BaseModel
from typing import List


class Coordinate(BaseModel):
    longitude: float
    latitude: float


class Region(BaseModel):
    type = "MultiPolygon"
    coverageArea: List[List[Coordinate]]


class Address(BaseModel):
    type = "Point"
    coordinate: Coordinate
