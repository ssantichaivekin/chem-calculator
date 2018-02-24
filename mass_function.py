'''
The 'mass' function, abbreviated 'm', calculates the mass of a compound
by its components. We will also be implementing a scraping option to
scrape information from the web instead of calculating it from its
components. (This is sometimes useful where very small mass-energy
relations starts to matter.)
'''

from constants.file_readers import read_mass_from_file
from constants.wiki_scraper import wikiscrape, wiki_mass
from matcher.formula_matcher import isChemicalFormula, formulaParse

masses = read_mass_from_file()

def count_elements(formula) :
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
        # print(formula, parsedict)
        
        if 'element name' in parsedict :
            # it is an element
            element_name = parsedict['element name']
            element_count = parsedict['element count']
            if element_name not in elements :
                elements[element_name] = 0
            elements[element_name] += element_count

        if 'group' in parsedict :
            # is a group
            newgroup = parsedict['group']
            group_count = parsedict['group count']
            new_elements = count_elements(newgroup)
            for element in new_elements :
                if element not in elements :
                    elements[element] = 0
                elements[element] += group_count * new_elements[element]
        
        if 'left group' in parsedict :
            formula = parsedict['left group']
        else :
            formula = ''

    return elements

def fmass(formula) :
    elements = count_elements(formula)
    total_mass = 0
    for element in elements :
        count = elements[element]
        total_mass += masses[element] * count
    return total_mass


def mass(name) :
    '''
    Return the mass of the chemical formula or chemical name.
    '''
    # We differentiate chemical formula and chemical name
    # by using regex.
    if isChemicalFormula(name) :
        return fmass(name)
    else :
        return wiki_mass(name)
    

def m(name) :
    '''
    m is the shorthand for mass.
    '''
    return mass(name)

if __name__ == '__main__' :
    assert 179 <= mass('C6H12O6') <= 182 # 180.156
    assert 179 <= m('C6H12O6') <= 182 # 180.156
    assert 155 <= m('Cu(II)SO4') <= 165 # 159.609
    assert 188 <= m('KHC4H4O6') <= 189 # 188.177
    assert 59 <= m('(CH3)2CHOH') <= 61 # ‎60.096
    assert 470 <= m('KAl(SO4)2·12H2O') <= 480 # 474.3884
