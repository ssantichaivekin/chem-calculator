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
    chemical_formula_pattern = r'^(?:(?:[A-Z][a-z]?[0-9]*)|\(.*\))*$'
    chemical_formula_regex = re.compile(chemical_formula_pattern)
    result = chemical_formula_regex.match(string)
    return bool(result)

def fmass(formula) :
    '''
    Compute the mass of the chemical formula.
    Note that we should carefully escape the oxidation numbers of
    metals such as Cu(II)SO4.
    '''
    first_element_pattern = r'(?:([A-Z][a-z]?)([0-9])?|\(.*\))'
    first_element_regex = re.compile(first_element_pattern)
    first_element_group = first_element_regex.match(formula)
    return first_element_group


def m(name) :
    '''
    Return the mass of the chemical formula or chemical name.
    '''
    # We differentiate chemical formula and chemical name
    # by using regex.
    if is_formula(name) :
        return fmass(name)
    

