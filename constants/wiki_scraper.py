'''
This file defines a wikipedia .
'''

import requests
import re
from bs4 import BeautifulSoup
from constants.file_writer import write_dict

def wikisearch(query) :
    params = {'search': query}
    r = requests.get('https://en.wikipedia.org/w/index.php', params=params)
    return BeautifulSoup(r.text, 'lxml')

def soupsite(query) :
    r = requests.get(query)
    return BeautifulSoup(r.text, 'lxml')

def parse_float(info) :
    '''
    Becareful! The minus (-) sign in wikipedia is not the same as in keyboard!
    I don't know why this is the case. I will ask people later.
    '''
    pattern = r'(−?[0-9]+\.[0-9]+)'
    decimal_regex = re.compile(pattern)
    matchobj = decimal_regex.search(info)
    if matchobj :
        num = matchobj.group(1).replace('−', '-')
        res = float(num)
        return res

def parse_int(info) :
    pattern = r'(−?[0-9]+)'
    int_regex = re.compile(pattern)
    matchobj = int_regex.search(info)
    if matchobj :
        num = matchobj.group(1).replace('−', '-')
        res = float(num)
        return res


def parse_float_or_int(info) :
    # if it has a !, read the number behind the !
    # either inside or outside of the box.
    x = parse_float(info)
    if x :
        return x
    return parse_int(info)
    


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
    elements = scrape_all_elements()
    order = ['symbol', 'mass', 'name', 'elem_no']
    write_dict('./constants/element_masses.csv', elements, order)


def wikiscrape(const_name) :
    return

def wiki_value_from_key(name, key) :
    '''
    Scrape table rows in that 'name' wikipedia page for the 'key' string.
    In that row, find a floating point value and return it.
    '''
    soup = wikisearch(name)
    trs = soup.find_all('tr')
    res_raw = False
    for tr in trs :
        if key in tr.text :
            res_raw = tr.text
            break
    if res_raw :
        res_val = parse_float(res_raw)
    else :
        res_val = 0.0
        print('We cannot find the %s value of %s (assume = 0.0).' % (key, name))
    return res_val

def entropy(name) :
    return wiki_value_from_key(name, 'So298')

def enthalpy_formation(name) :
    return wiki_value_from_key(name, 'ΔfHo298')

def enthalpy_combustion(name) :
    return wiki_value_from_key(name, 'ΔcHo298')


