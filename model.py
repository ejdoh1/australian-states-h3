from __future__ import annotations

from typing import List, Union

from pydantic import BaseModel


class Properties(BaseModel):
    STATE_CODE: str
    STATE_NAME: str


class Geometry(BaseModel):
    type: str
    coordinates: List[List[List[Union[float, List[float]]]]]


class Feature(BaseModel):
    type: str
    id: int
    properties: Properties
    geometry: Geometry


class Model(BaseModel):
    type: str
    features: List[Feature]
