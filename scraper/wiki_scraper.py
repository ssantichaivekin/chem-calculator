'''
This file defines wikipedia webscraping functionalities.
'''

import requests
import re
from bs4 import BeautifulSoup
from read_write.file_writer import write_dict
from matcher.num_matcher import parse_float_or_int, parse_num_with_units
from scraper.conversions import conversion_table as conversions

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


