from math import sin, cos, sqrt, atan2, radians
import json

def distance(origin, destination):
    """
    Calculate the Haversine distance.

    Parameters
    ----------
    origin : tuple of float
        (lat, long)
    destination : tuple of float
        (lat, long)

    Returns
    -------
    distance_in_km : float

    Examples
    --------
    # >>> origin = (48.1372, 11.5756)  # Munich
    # >>> destination = (52.5186, 13.4083)  # Berlin
    # >>> round(distance(origin, destination), 1)
    504.2
    """
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371  # km

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = (sin(dlat / 2) * sin(dlat / 2) +
         cos(radians(lat1)) * cos(radians(lat2)) *
         sin(dlon / 2) * sin(dlon / 2))
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    d = radius * c

    return d

def percentage(of, in_):
    """
        Calculate percentage based by count of location closer than 10km per shopper

        Returns
        -------
        percentage of locations covered by given shopper
        """
    return round(in_.count(of) * 100 / len(in_))

def findCoveredZones(json_dictionary_shopers,json_dictionary_locations):
    """
    Find covered locations by enabled shopper.

    Parameters
    ----------
    json_dictionary_shopers : array
    json_dictionary_location : array

    Returns
    -------
    dictionary of enabled shopers with locations  less than 10km: dictionary
    """
    for key_shopers in json_dictionary_shopers:
        final.update({'shopper_id': key_shopers['id']})
        for key_locations in json_dictionary_locations:
            distanceCalc = round(
                distance((key_shopers['lat'], key_shopers['lng']), (key_locations['lat'], key_locations['lng'])), 1)
            if distanceCalc < 10:
                # print(distanceCalc)
                # myDict.setdefault(final['shopper_id'], []).append(key_locations['zip_code'])
                myDict.setdefault(final['shopper_id'], []).append(1)
            else:
                myDict.setdefault(final['shopper_id'], []).append(0)
    return myDict

#presume that location "id" is unique, in other way we can use "zip_code" as unique identifier
locations = [
    	  {'id': 1000, 'zip_code': '37069', 'lat': 45.35, 'lng': 10.84},
    	  {'id': 1001, 'zip_code': '37121', 'lat': 45.44, 'lng': 10.99},
    	  {'id': 1001, 'zip_code': '37129', 'lat': 45.44, 'lng': 11.00},
          {'id': 1001, 'zip_code': '37133', 'lat': 45.43, 'lng': 11.02}
    	]

shoppers = [
    {'id': 'S1', 'lat': 45.46, 'lng': 11.03, 'enabled': 'true'},
    {'id': 'S2', 'lat': 45.46, 'lng': 10.12, 'enabled': 'true'},
    {'id': 'S3', 'lat': 45.34, 'lng': 10.81, 'enabled': 'true'},
    {'id': 'S4', 'lat': 45.76, 'lng': 10.57, 'enabled': 'true'},
    {'id': 'S5', 'lat': 45.34, 'lng': 10.63, 'enabled': 'true'},
    {'id': 'S6', 'lat': 45.42, 'lng': 10.81, 'enabled': 'true'},
    {'id': 'S7', 'lat': 45.34, 'lng': 10.94, 'enabled': 'true'}
]

json_dictionary_shopers = json.loads(json.dumps(shoppers))
json_dictionary_locations = json.loads(json.dumps(locations))
finalArray = []
final = {}
myDict = dict()

findCoveredZones(json_dictionary_shopers, json_dictionary_locations)

#generate array of shopers with their coverage
for key, values in myDict.items():
    finalArray.append({"shopers_id": key ,"coverage": percentage(1, values)})

#sort desc by "coverage" value
sorted = sorted(finalArray, key=lambda k: k['coverage'], reverse=True)
print(sorted)
