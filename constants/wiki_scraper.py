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

def parse_mass_info(info) :
    # if it has a !, read the number behind the !
    # either inside or outside of the box.
    pattern = r'([0-9]+\.[0-9]+)'
    decimal_regex = re.compile(pattern)
    matchobj = decimal_regex.search(info)
    if matchobj :
        return float(matchobj.group(1))
    
    pattern = r'([0-9]+)'
    int_regex = re.compile(pattern)
    matchobj = int_regex.search(info)
    if matchobj :
        return float(matchobj.group(1))


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
            mass = parse_mass_info(mass_info)

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

