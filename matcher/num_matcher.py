'''
This is a module that help parse floating point numbers
and numbers in general. It is used as a helper function
to scrape things off wikipedia.
'''

import re

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