"""Generate a CSV file mapping H3 cells to Australian states."""

from h3 import Polygon, polygon_to_cells

from model import Model

RES = 6


def poly_to_cells(poly, res):
    """Convert a polygon to a list of cells."""
    poly = [(lng, lat) for lat, lng in poly]
    poly = Polygon(poly)
    return polygon_to_cells(poly, res)


with open("states.geojson", "r", encoding="utf-8") as f:
    model = Model.parse_raw(f.read())

# write state,cellId to CSV file
lookup = {}
for feature in model.features:
    if feature.geometry.type == "MultiPolygon":
        for polygons in feature.geometry.coordinates:
            for polygon in polygons:
                for cell in poly_to_cells(polygon, RES):
                    lookup[cell] = feature.properties.STATE_NAME
for feature in model.features:
    if feature.geometry.type == "Polygon":
        for cell in poly_to_cells(feature.geometry.coordinates[0], RES):
            lookup[cell] = feature.properties.STATE_NAME

with open("states.csv", "w", encoding="utf-8") as f:
    f.write("state,cellId\n")
    for cell, state in lookup.items():
        f.write(f"{state},{cell}\n")
