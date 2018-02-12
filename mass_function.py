'''
The 'mass' function, abbreviated 'm', calculates the mass of a compound
by its components. We will also be implementing a scraping option to
scrape information from the web instead of calculating it from its
components. (This is sometimes useful where very small mass-energy
relations starts to matter.)
'''

import re
from mass_mode import *

masses = read_mass_from_file()
element_pattern = r'(?:([A-Z][a-z]?)(\(I+\))?([0-9]*))|(?:\((.*)\)([0-9]*)?)'


def is_formula(string) :
    '''
    Check whether a string is a chemical formula.
    '''
    # A chemical formula is a repetition of element pattern.
    chemical_formula_pattern = '^(?:%s)+$' % element_pattern
    chemical_formula_regex = re.compile(chemical_formula_pattern)
    result = chemical_formula_regex.match(string)
    return bool(result)

# def is_oxidation(string) :
#     '''
#     Check whether the string contains '(I)' '(II)'
#     '(III)' and so on.
#     '''
#     oxidation_pattern = r'^\(I+\)$'
#     oxidation_regex = re.complie(oxidation_pattern)
#     result = oxidation_regex.match(string)
#     return bool(result)

def is_one_element(matchobj) :
    '''
    Check whether the matchobj is an element (say 'C')
    rather than a group of elements covered by parenthesis.
    '''
    return bool(matchobj.group(1))

def fmass(formula) :
    '''
    Compute the total mass of the chemical formula.
    Note that we should carefully escape the oxidation numbers of
    metals such as Cu(II)SO4.
    '''
    total_mass = 0
    # Group 1 : element name
    # Group 2 : oxidation number for metals
    # Group 3 : element count
    # Group 4 : (group) string
    # Group 5 : (group) count
    element_regex = re.compile(element_pattern)

    while formula :
        element_group = element_regex.match(formula)
        if is_one_element(element_group) :
            element_name = element_group.group(1)
            # if no element count is specified, use 1.
            # For example, O in H20 does not have a count.
            element_count = float(element_group.group(3) or 1)
            total_mass += masses[element_name] * element_count
        else :
            inside_group = element_group.group(4)
            # if no group count is specified, use 1.
            group_count = float(element_group.group(5) or 1)
            total_mass += fmass(inside_group) * group_count
        end_group = element_group.end()
        formula = formula[end_group:]
    return total_mass

def wiki_mass(name) :
    '''
    Scrape Wikipedia!
    '''
    return "We haven't implemented web scraping yet."


def mass(name) :
    '''
    Return the mass of the chemical formula or chemical name.
    '''
    # We differentiate chemical formula and chemical name
    # by using regex.
    if is_formula(name) :
        return fmass(name)
    else :
        return wiki_mass(name)
    

def m(name) :
    '''
    m is the shorthand for mass.
    '''
    return mass(name)
