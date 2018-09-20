'''
Fish Length to Weight converter.

Supports lengths in quarter inch increments only.

Utilizes data from:
https://www.dnr.state.mn.us/fishing/regs.html
https://dnr.wi.gov/topic/fishing/questions/estfishweight.html
https://www.iowadnr.gov/Portals/idnr/uploads/fish/regs_fish.pdf
http://www.swmnhunting.com/6783-2/
https://gf.nd.gov/fishing/regulations-guide
https://www.dec.ny.gov/outdoor/9222.html

Returns JSON in the format:
{
    "Species": "Walleye",
    "Length": "23.75",
    "MN DNR Table": 5.225,
    "Catch & Release Forumlas (WI and IA DNR)": 4.962,
    "ND DNR Table": 4.95,
    "NY DEC Table": 4.531,
    "average": 4.917
}

'''
import json
import statistics
import sys


WALLEYE_LENGTH_LOWER_LIMIT = 8
WALLEYE_LENGTH_UPPER_LIMIT = 35
NORTHERN_LENGTH_LOWER_LIMIT = 12
NORTHERN_LENGTH_UPPER_LIMIT = 54
SMALLMOUTH_LENGTH_LOWER_LIMIT = 6
SMALLMOUTH_LENGTH_UPPER_LIMIT = 25

SPECIES_DETAILS = {
    'Walleye': {
        'file': 'data/walleye.json',
        'lower': WALLEYE_LENGTH_LOWER_LIMIT,
        'upper': WALLEYE_LENGTH_UPPER_LIMIT
    },
    'Northern': {
        'file': 'data/northern.json',
        'lower': NORTHERN_LENGTH_LOWER_LIMIT,
        'upper': NORTHERN_LENGTH_UPPER_LIMIT
    },
    'Smallmouth': {
        'file': 'data/smallmouth.json',
        'lower': SMALLMOUTH_LENGTH_LOWER_LIMIT,
        'upper': SMALLMOUTH_LENGTH_UPPER_LIMIT
    }
}

CONVERSION_SYSTEMS = [
    {'lookup': 'MN', 'output': 'MN DNR Table'},
    {'lookup': 'CR', 'output': 'Catch & Release Forumlas (WI and IA DNR)'},
    {'lookup': 'ND', 'output': 'ND DNR Table'},
    {'lookup': 'NY', 'output': 'NY DEC Table'},
]


def convertibleToFloat(value) -> bool:
    try:
        float(value)
        return True
    except:
        return False


def checkArgs(species, length):
    # Is the species one we handle
    if species not in SPECIES_DETAILS.keys():
        raise ValueError('Species is not one of {0}'.format(
            SPECIES_DETAILS.keys()))

    # Is the length convertible to float
    # Leave this check first for length because other checks treat as float
    if not convertibleToFloat(length):
        raise ValueError('Length argument is not a number')

    lengthAsFloat = float(length)

    # Is length within bounds we cover
    speciesDetails = SPECIES_DETAILS.get(species)
    if not (lengthAsFloat >= speciesDetails.get('lower') and
            lengthAsFloat <= speciesDetails.get('upper')):
        raise ValueError('Length argument is outside '
                         'reasonable bounds of {0} and {1}'.format(
                             speciesDetails.get('lower'),
                             speciesDetails.get('upper')))

    # Is length a whole or quarter-value
    if lengthAsFloat % .25 > 0:
        raise ValueError('Length argument is not whole or quarter value')


def lengthToWeight(species, length) -> str:
    checkArgs(species, length)

    # Strip trailing zeros (and decimal if whole number)
    # because lookup tables don't use them
    length = length.rstrip('0').rstrip('.')

    file = SPECIES_DETAILS.get(species).get('file')

    with open(file) as dataFile:
        result = {}
        result['Species'] = species
        result['Length'] = length

        data = json.load(dataFile)
        record = data.get(length)
        if not record:
            raise ValueError(
                'No results in {0} table for length "{1}"'
                .format(species, length))

        floatVals = []
        for system in CONVERSION_SYSTEMS:
            lookup = system.get('lookup')
            output = system.get('output')
            systemWeight = record.get(lookup)
            result[output] = systemWeight

            if (systemWeight):
                floatVal = float(systemWeight)
                floatVals.append(floatVal)

        average = statistics.mean(floatVals)
        result['average'] = average

        return json.dumps(result)


if __name__ == '__main__':
    sys.exit(lengthToWeight('Smallmouth', '16'))
