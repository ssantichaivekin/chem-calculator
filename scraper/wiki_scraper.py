'''
This file defines a wikipedia .
'''

import requests
import re
from bs4 import BeautifulSoup
from read_write.file_writer import write_dict


def wikisearch(query) :
    '''
    Return a beautiful soap object of the 'query' wikipedia page.
    '''
    params = {'search': query}
    r = requests.get('https://en.wikipedia.org/w/index.php', params=params)
    return BeautifulSoup(r.text, 'lxml'), r.url

def soupsite(siteurl) :
    '''
    Return a beautiful soup object of siteurl.
    '''
    r = requests.get(siteurl)
    return BeautifulSoup(r.text, 'lxml')

def wikiscrape() :
    return

pattern_float = r'(?:−|-)?[0-9]+\.[0-9]+'
float_regex = re.compile('(%s)' % (pattern_float))

pattern_int = r'(?:−|-)?[0-9]+'
int_regex = re.compile('(%s)' % (pattern_int))

pattern_float_or_int = '(?:%s)|(?:%s)' % (pattern_float, pattern_int)

def parse_float(info) :
    '''
    Find the first floating point value in the string. (Floating point values
    are defined by the decimal point.)
    Becareful! The minus (-) sign in wikipedia is not the same as in keyboard!
    I don't know why this is the case. I will ask people later.
    '''
    matchobj = float_regex.search(info)
    if matchobj :
        num = matchobj.group(1).replace('−', '-')
        res = float(num)
        return res


def parse_int(info) :
    '''
    Find the first integer in a string. But you return a float.
    Quite counter intuitive. Maybe I should change how this works.
    # TODO: Change how this works?
    '''
    matchobj = int_regex.search(info)
    if matchobj :
        num = matchobj.group(1).replace('−', '-')
        res = float(num)
        return res


def parse_float_or_int(info) :
    '''
    Parse float. If there's no float, parse int.
    '''
    x = parse_float(info)
    if x :
        return x
    return parse_int(info)

# def get_unit_pattern(units) :
#     units_pattern = '(?:'
#     units_pattern += re.escape(units[0])
#     for unit in units[1:] :
#         units_pattern += '|' + re.escape(unit)
#     units_pattern += ')'
#     return units_pattern

def parse_num_with_units(info, units) :
    '''
    Parse the number that comes just before any unit in
    units.
    # TODO : This may be buggy if the units have symbols like '-'
    '''
    for unit in units :
        pattern_unit = re.escape(unit)
        # print(info)
        # print(pattern_unit, unit)
        pattern_parse = r'(%s)(?:\s*)(?:%s)' % (pattern_float_or_int, pattern_unit)
        parse_regex = re.compile(pattern_parse)
        matchobj = parse_regex.search(info)
        if matchobj :
            numstr = matchobj.group(1)
            return parse_float_or_int(numstr), unit


def scrape_all_elements() :
    '''
    Scrape elements from wikipedia.
    Return a list containing element names and its symbol
    return {'name' : 'symbol'}
    '''
    link = 'https://en.wikipedia.org/wiki/List_of_chemical_elements'
    soup = soupsite(link)

    elements = []

    tables = soup.find_all('table')
    has_hydrogen = lambda x: 'Hydrogen' in x.prettify()
    element_table = list(filter(has_hydrogen, tables))[0]
    # print(element_table)

    rows = element_table.find_all('tr')
    is_element = lambda x: 'Notes' not in x.prettify()
    element_rows = list(filter(is_element, rows))
    
    for element in element_rows :
        info_array = [val.text for val in element.find_all('td')]
        if info_array :
            elem_no = info_array[0]
            symbol = info_array[1]
            name = info_array[2]
            mass_info = info_array[6]
            mass = parse_float_or_int(mass_info)

            # print('elem_no = ', elem_no)
            # print('symbol = ', symbol)
            # print('name = ', name)
            # print('mass = ', mass)

            element = {'elem_no': elem_no, 'symbol': symbol, 'name':name, 'mass': mass}
            elements += [element]
        # print()
    return elements

def write_mass_constants() :
    '''
    Write mass constand to a file in constants folder.
    '''
    elements = scrape_all_elements()
    order = ['symbol', 'mass', 'name', 'elem_no']
    write_dict('./constants/element_masses.csv', elements, order)

conversions = {'MJ/mol': ('kJ/mol', 1000),
               'MJ mol−1' : ('kJ/mol', 1000)}

def unit_convert(value, unit) :
    '''
    For now, just convert MJ to kJ.
    '''
    if unit in conversions :
        newunit = conversions[unit][0]
        newvalue = conversions[unit][1] * value
        return newvalue, newunit
    return value, unit


def wiki_value_from_key(name, key, units) :
    '''
    Scrape table rows in that 'name' wikipedia page for the 'key' string.
    In that row, find a floating point value and return it.
    '''
    soup, url = wikisearch(name)
    trs = soup.find_all('tr')
    res_raw = False
    for tr in trs :
        if key in tr.text :
            res_raw = tr.text
            break
    if res_raw :
        # Parse float or int that precedes a unit.
        res_val, unit = parse_num_with_units(res_raw, units)
        converted_val, converted_unit = unit_convert(res_val, unit)
        print('According to %s, the %s of %s is %.2f %s' % (url, key, name, res_val, unit))
        if unit != converted_unit :
            print('This is converted to %.2f %s' % (converted_val, converted_unit))
            return converted_val
    else :
        res_val = 0.0
        print('We cannot find the %s value of %s (assume = 0.0).' % (key, name))
    return res_val

def entropy(name) :
    '''
    Return the standard molar entropy of 'name'
    '''
    return wiki_value_from_key(name, 'So298', ['J·(K·mol)−1'])

def enthalpy_formation(name) :
    '''
    Return the standard enthalpy of formation of 'name'
    '''
    return wiki_value_from_key(name, 'ΔfHo298', ['kJ/mol', 'kJ mol−1', 'MJ/mol', 'MJ mol−1'])

def enthalpy_combustion(name) :
    '''
    Return the standard enthalpy of combustion of 'name'
    '''
    return wiki_value_from_key(name, 'ΔcHo298', ['kJ/mol', 'kJ mol−1', 'MJ/mol', 'MJ mol−1'])

def wiki_mass(name) :
    '''
    Return the mass of 'name'
    '''
    return wiki_value_from_key(name, 'Molar mass', ['g·mol−1'])

