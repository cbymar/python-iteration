#!/usr/bin/env python

import os
import ijson
import itertools
import pprint


def get_filename():
    path_to_file = 'airports/airports.json'
    module_path = os.path.dirname(os.path.realpath(__file__))
    project_path = os.path.dirname(module_path)
    return os.path.join(project_path, path_to_file)


def get_airports(filename):
    json_file = open(filename, 'rb')
    for airport in ijson.items(json_file, 'item'):
        yield airport


def filter_airport(airport):
    iso_countries = set([
        "US",
        "CA"
    ])

    sizes = set([
        "small"
    ])

    if airport['iso'] not in iso_countries:
        return False

    if airport['size'] not in sizes:
        return False

    return True


def get_filtered_airports():
    filename = get_filename()
    airport_codes = {}
    for airport in itertools.ifilter(filter_airport, get_airports(filename)):
        code = airport['iata']
        airport_codes[code] = airport
    pprint.pprint(airport_codes)

if __name__ == '__main__':
    get_filtered_airports()
