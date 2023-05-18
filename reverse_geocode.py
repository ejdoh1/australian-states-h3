# load states.csv into a dictionary

import csv
from h3 import latlng_to_cell

lookup = {}
with open("states.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        lookup[row["cellId"]] = row["state"]

# Melbourne CBD lat/lng
lat = -37.814
lng = 144.96332

# convert lat/lng to H3 cell
cell = latlng_to_cell(lat, lng, 6)

# look up state
state = lookup[cell]

print(f"Melbourne CBD is in {state}")
