'''
Class ChemOb define a class that have a unit.
A chemistry object is defined as follows:
    - An object has a value.
    - An object has a numerator unit.
    - An object has a denominator unit.
At this point, you might wonder about a partial unit.
Say, srqt(mol). However, I don't see that a lot. Actually,
I have never seen that before. So I will keep that aside for
now.
'''

import re

def read_unitstring(unitstring) :
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
    pattern_unit = 

class ChemOb :
    def __init__(self, value = 0, unitstring = "") :
        '''
        ChemOb has value, numerator_unit, and denominator_unit.
        '''
        self.value = value
        num, den = read_unitstring(unitstring)
        self.numerator = num
        self.denominator = den
    
    def recalculate_prefix(self) :
        '''
        remove every prefix (p - pico, u - micro, m - milli, k - kilo) from each unit in
        self. Modify self.
        '''

    # Maybe not?
    # def use_matrix(self) :
    #     '''
    #     Use matrix system for units. Convert any non-matrix units to matrix.
    #     '''


