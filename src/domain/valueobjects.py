from typing import List
from pydantic import (
    BaseModel,
    validator
)


class Coordinate(BaseModel):
    longitude: float
    latitude: float

    @validator('latitude')
    def check_latitude(self, v):
        if validate_latitude(v):
            return v.title()
        else:
            raise ValueError('latitude value is not valid, accept value in range -90..90')

    @validator('longitude')
    def check_longitude(self, v):
        if validate_longitude(v):
            return v.title()
        else:
            raise ValueError('longitude value is not valid, accept value in range -180..180')


class Region(BaseModel):
    type = "MultiPolygon"
    coverageArea: List[List[Coordinate]]

    @validator('coverageArea')
    def check_longitude(self, v):
        if validate_multi_polygon(v):
            return v.title()
        else:
            raise ValueError('longitude value is not valid, accept value in range -180..180')


class Address(BaseModel):
    type = "Point"
    coordinate: Coordinate


def validate_latitude(latitude: float):
    """according https://pt.wikipedia.org/wiki/Latitude"""
    if latitude in range(-90, 90):
        return True
    else:
        return False


def validate_longitude(longitude: float) -> bool:
    """according https://pt.wikipedia.org/wiki/ Longitude"""
    if longitude in range(-180, 180):
        return True
    else:
        return False


def validate_multi_polygon(multipolygon: List[List[Coordinate]]) -> bool:
    """according: https://en.wikipedia.org/wiki/GeoJSON"""
    if multipolygon[0] == multipolygon[:-1]:
        return True
    else:
        return False
