'''
read the unit part.
examples:   'kJ/mol'        : ['kJ'], ['mol']
            'kJ mol−1'      : ['kJ'], ['mol']
            'kJ·mol−1'      : ['kJ'], ['mol']
            'MJ/mol'        : ['MJ'], ['mol']
            'MJ mol−1'      : ['MJ'], ['mol']
            'g·mol−1'       : ['g'], ['mol]
            'J·(K·mol)−1'   : ['J'], ['K', 'mol']
return (list of numerator, list of denominator).

Note that we will have something like :
[group1][connector][group2][connector][group3]-1
[group1][connector]([group2][connector][group3])-1[group4]
[group1]/[group2]
'''
# The strategy is that we will read the preceding connector (possibly empty),
# and capture a first group, and optionally read the -1 sign on the back.
# It is also possible that a group has a () enclosing it. In that case,
# We capture the whole thing and perfrom read string on it recursively.
# Note that in that case, the numerator and the denominator will be inversed.
group_pattern = r'[a-zA-Z]{1,3}'
free_connector_pattern = r'[\.\+\s·.]'
div_connector_pattern = r'/'
inv_pattern = r'−1|-1' # Note that the two - symbols are not of equal value here!

# we also have a separate parenthesis patttern for recursive call:
paren_pattern = r'\(.*\)'

# Now we compile these patterns for further use!
# If the second group or the forth group is match, then it is inverted
full_pattern = '(%s)?(%s)?(%s|%s)(%s)?' % (
    free_connector_pattern,
    div_connector_pattern,
    group_pattern,
    paren_pattern,
    inv_pattern
)

print(full_pattern)

def read_unitstring(unitstring) :
    return