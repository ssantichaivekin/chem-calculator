'''
Implements a regex matcher for formulas.
The matchers generally return the following: {
    'isgroup' : (bool) 1 if to be called recursively.
    'group' : (str) the chemical group to be called recursively
    'group count' : (int) 1 by default
    'element name' : (str) if it is just an element
    'element count' : (int) the count of the element
    'left group' : (str) another group to be called recursively
}
'''
import re

# element name, (oxidation number), element count
element_pattern = r'([A-Z][a-z]?)(?:\(V?I+V?\))?([0-9]*)'
element_des = ['element name', 'element count']
element_types = [str, int]
element_regex = re.compile(element_pattern)

# inside group, count group
paren_group_pattern = r'\((.*)\)([0-9]*)'
paren_group_des = ['group', 'group count']
paren_group_types = [str, int]
paren_group_regex = re.compile(paren_group_pattern)

# (dot/plus) inside group, (up to the end or a sep).
out_group_pattern = r'(?:\.|\+| )([0-9]*)([^\.\+]*)'
out_group_des = ['group count', 'group']
out_group_types = [int, str]
out_group_regex = re.compile(out_group_pattern)

# (dot/plus) group count, inside group
quantifier_pattern = r'(?:\.|\+| |·|.{0})([0-9]+)([^\.\+]*)'
quantifier_des = ['group count', 'group']
quantifier_types = [int, str]
quantifier_regex = re.compile(quantifier_pattern)

# full pattern regex checker
full_pattern = '^(:?(?:%s)|(?:%s)|(?:%s)|(?:%s))+$' % (
    quantifier_pattern, 
    element_pattern, 
    paren_group_pattern,
    out_group_pattern)
formula_regex = re.compile(full_pattern)

# Dictionary containing all the regex checkers
checkers = {
    'element' : {
        're' : element_regex, 
        'des' : element_des,
        'types' : element_types
        },
    'paren_group' : {
        're' : paren_group_regex, 
        'des' : paren_group_des,
        'types' : paren_group_types
        },
    'out_group' : {
        're' : out_group_regex, 
        'des' : out_group_des,
        'types' : out_group_types
        },
    'quantifier' : {
        're' : quantifier_regex, 
        'des' : quantifier_des,
        'types' : quantifier_types
        }
}

def isChemicalFormula(string) :
    '''
    Check whether a string is a chemical formula
    '''
    return bool(formula_regex.match(string))

def formulaParse(string) :
    '''
    Returns the following: {
    'group' : (str) the chemical group to be called recursively
    'group count' : (int) 1 by default
    'element name' : (str) if it is just an element
    'element count' : (int) the count of the element
    'left group' : (str) another group to be called recursively
    }
    '''
    result = {}
    for name in checkers :
        checktype = checkers[name]
        res = checktype['re'].match(string)
        if res :
            # res is a re.match object
            # des is sth like ['group', 'group count']
            # typ is the array of types
            # print(name)
            des = checktype['des']
            typ = checktype['types']
            for i in range(len(des)) :
                info_name = des[i]
                info_type = typ[i]
                if info_type == int and res.group(i+1) == '' :
                    info_val = 1
                else :
                    info_val = info_type(res.group(i+1))

                result[info_name] = info_val
            left = string[res.end():]
            if left :
                result['left group'] = left
            return result
    return {}

if __name__ == '__main__' :
    assert isChemicalFormula('Santi') == False
    assert isChemicalFormula('haha') == False
    assert isChemicalFormula('True') == False
    assert isChemicalFormula('KAl(SO4)2·12H2O')
    assert formulaParse('C6H12O6')['element name'] == 'C'
    assert formulaParse('NaCl')['element name'] == 'Na'
    assert formulaParse('CH3COOH')['element name'] == 'C'
    assert formulaParse('MgSo4')['element name'] == 'Mg'
    print('C6H12O6', formulaParse('C6H12O6'))
    print('Cu(II)SO4', formulaParse('Cu(II)SO4'))
    print('12H2O', formulaParse('12H2O'))


