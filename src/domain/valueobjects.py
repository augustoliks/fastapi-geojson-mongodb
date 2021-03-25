from typing import List
import geojson
from pydantic import (
    BaseModel,
    validator
)


class Region(BaseModel):
    type = "MultiPolygon"
    coverageArea: List[
        List[
            List[float, float]
        ]
    ]

    @validator('coverageArea')
    def check_longitude(cls, v):
        if validate_multi_polygon(v):
            return v.title()
        else:
            raise ValueError('longitude value is not valid, accept value in range -180..180')


class Address(BaseModel):
    type = "Point"
    coordinates: List[float, float]


def validate_multi_polygon(multipolygon_coordinates: List[List[List[float, float]]]):
    """according: https://en.wikipedia.org/wiki/GeoJSON"""
    multipolygon = geojson.MultiPolygon(multipolygon_coordinates)

    if not multipolygon.is_valid:
        raise ValueError('Multipolygon não válido')

    for level_01 in multipolygon.coordinates:
        for level_02 in level_01:
            latitude_valid = level_02[0] in range(-90, 90)
            longitude_valid = level_02[1] in range(-180, 180)
            if not latitude_valid or not longitude_valid:
                raise ValueError('coordenadas nao validas')
