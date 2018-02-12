'''
The 'mass' function, abbreviated 'm', calculates the mass of a compound
by its components. We will also be implementing a scraping option to
scrape information from the web instead of calculating it from its
components. (This is sometimes useful where very small mass-energy
relations starts to matter.)
'''

import re

def is_formula(string) :
    '''
    Check whether a string is a chemical formula.
    '''
    chemical_formula_regex_check = r'^(?:(?:[A-Z][a-z]?[0-9]*)|\(.*\))*$'
    r = re.compile(chemical_formula_regex_check)
    result = r.match(string)
    return bool(result)

def fmass(formula) :
    return


def m(name) :
    '''
    Return the mass of the chemical formula or chemical name.
    '''
    # We differentiate chemical formula and chemical name
    # by using regex.
    if is_formula(name) :
        return fmass(name)
    

