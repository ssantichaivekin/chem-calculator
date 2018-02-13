'''
Test formula matcher.
'''

from formula_matcher import *

assert formulaParse('C6H12O6')['element name'] == 'C'
assert formulaParse('NaCl')['element name'] == 'Na'
assert formulaParse('CH3COOH')['element name'] == 'C'
assert formulaParse('MgSo4')['element name'] == 'Mg'
