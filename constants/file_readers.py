import csv

def read_dict_from_file(filepath) :
    '''
    Read dictionary csv information from file path
    and return the name and the value info as a dictionary.
    '''
    # TODO: how to I set up the file path correctly so that
    # I can call this function from anywhere?
    # Do I config this file path in pip?

    res = {}
    f = open(filepath)
    reader = csv.reader(f)
    for row in reader :
        key = row[0]
        val = row[1]
        res[key] = float(val)
    return res

def read_mass_from_file(filepath='./constants/element_masses.csv') :
    '''
    Read mass information from file path or 'element_mass.csv'
    and return the name and the mass info as a dictionary.
    '''
    element_masses = read_dict_from_file(filepath)
    return element_masses