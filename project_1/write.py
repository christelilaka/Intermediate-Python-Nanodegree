import csv
import json
from helpers import cd_to_datetime, datetime_to_str

def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')
    
    with open(filename, 'w') as output_csv:
        writer = csv.writer(output_csv)
        writer.writerow(fieldnames)
        for approach in results:
            row = [approach.time, approach.distance, approach.velocity, approach.designation, approach.neo.name, approach.neo.diameter, approach.neo.hazardous]
            writer.writerow(row)


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    json_row = []
    for data in results:
        approach = {
            'datetime_utc': datetime_to_str(data.time),
            'distance_au': data.distance,
            'velocity_km_s': data.velocity,
            'neo': {
                'designation': data.neo.designation,
                'name': data.neo.name,
                'diameter_km': data.neo.diameter,
                'potentially_hazardous': data.neo.hazardous
            }
        }
        json_row.append(approach)

    with open(filename, "w") as outfile:
        json.dump(json_row, outfile, indent=2)