from typing import List
import geojson
from pydantic import (
    BaseModel,
    validator
)


class MultiPolygon(BaseModel):
    type = "MultiPolygon"
    coordinates: List[
        List[List[List[float]]]
    ]

    @validator('coordinates')
    def check_multi_polygon(cls, v):
        validate_multi_polygon(v)
        return v


class Point(BaseModel):
    type = "Point"
    coordinates: List[float]

    @validator('coordinates')
    def check_longitude(cls, v):
        validate_point(v)
        return v


def validate_latitude(latitude):
    return latitude >= -90 and latitude <= 90


def validate_longitude(longitude):
    return longitude >= -180 and longitude <= 180


def validate_point(point: List[float]):
    """according: https://en.wikipedia.org/wiki/GeoJSON"""
    point = geojson.Point(point)

    if not point.is_valid:
        raise ValueError('Point is not valid')

    latitude, longitude = point.coordinates
    latitude_valid = validate_latitude(latitude)
    longitude_valid = validate_longitude(longitude)

    if not latitude_valid or not longitude_valid:
        raise ValueError('coordinates is not valid')


def validate_multi_polygon(multipolygon_coordinates: List[List[List[float]]]):
    """according: https://en.wikipedia.org/wiki/GeoJSON"""
    multipolygon = geojson.MultiPolygon(multipolygon_coordinates)

    if not multipolygon.is_valid:
        raise ValueError('MultiPolygon is not valid')

    for level_01 in multipolygon.coordinates:
        for level_02 in level_01:
            for level_03 in level_02:
                latitude_valid = validate_latitude(level_03[0])
                longitude_valid = validate_longitude(level_03[1])
                if not latitude_valid or not longitude_valid:
                    raise ValueError('coordinates is not valid')
