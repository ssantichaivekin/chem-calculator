'''
The 'mass' function, abbreviated 'm', calculates the mass of a compound
by its components. We will also be implementing a scraping option to
scrape information from the web instead of calculating it from its
components. (This is sometimes useful where very small mass-energy
relations starts to matter.)
'''

from mass_mode import *
from formula_matcher import isChemicalFormula, formulaParse
from wiki_scraper import wikiscrape

masses = read_mass_from_file()

def fmass(formula) :
    '''
    Compute the total mass of the chemical formula.
    Note that we should carefully escape the oxidation numbers of
    metals such as Cu(II)SO4.
    '''
    # elements counts each element as {'name': count}
    elements = {}
    while formula :
        # 'group' : (str) the chemical group to be called recursively
        # 'group count' : (int) 1 by default
        # 'element name' : (str) if it is just an element
        # 'element count' : (int) the count of the element
        # 'left group' : (str) another group to be called recursively
        parsedict = formulaParse(formula)
        
        if 'element name' in parsedict :
            # it is an element
            element_name = parsedict['element name']
            element_mass = masses[element_name]
            element_count = parsedict['element count']
            if element_name not in elements :
                elements[element_name] = 0
            elements[element_name] += element_count
            formula = parsedict['left group']

        if ''

    return elements

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
