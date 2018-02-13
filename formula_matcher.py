import re

# Group 1 : element name
# Group 2 : oxidation number for metals
# Group 3 : element count
# Group 4 : (group) string
# Group 5 : (group) count

quantifier_pattern = r'(?:(?:\.|\+)([0-9]+))'
# element name, oxidation number, element count
element_pattern = r'([A-Z][a-z]?)(\(I+\))?([0-9]*)'
# inside group, count group
paren_group_pattern = r'\((.*)\)([0-9]*)'
# (dot/plus) inside group, (up to the end or a sep).
out_group_pattern = r'(?:\.|\+| |.{0})([0-9]*)([^\.\+]*)'

full_pattern = '(?:%s)|(?:%s)|(?:%s)|(?:%s)' % (
    quantifier_pattern, 
    element_pattern, 
    paren_group_pattern,
    out_group_pattern)

check_pattern = '^(?:%s)+$' % full_pattern

