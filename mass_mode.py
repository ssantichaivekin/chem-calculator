'''
The mass mode function sets the element variables to be its mass.
For example, H = 1, He = 4, Li = 3.
We now have an inaccurate mass mode. We will implement a wikipedia
web-scrape mass mode later.
'''
import csv

def read_mass_from_file( filepath='' ) :
    '''
    Read mass information from file path or 'element_mass.csv'
    and return the name and the mass info as a dictionary.
    '''
    # TODO: how to I set up the file path correctly so that
    # I can call this function from anywhere?
    # Do I config this file path in pip?
    filepath = filepath or 'element_mass.csv'
    element_dict = {}
    f = open(filepath)
    reader = csv.reader(f)
    for row in reader :
        element_name = row[0]
        element_mass = row[1]
        element_dict[element_name] = element_mass
    return element_dict
    
def web_scrape_mass() :
    return

'''
The mass mode is now here.
Add element names and masses to the global variables.
'''
element_dict = read_mass_from_file()
globals().update(element_dict)