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
                'kJ mol−1'      : ['kJ']
                'kJ·mol−1'      :
                'MJ/mol'        :
                'MJ mol−1'      :
                'g·mol−1'       :
                'J·(K·mol)−1'   :
    return a list of numerator and denominator.
    '''
    pattern_unit = 

class ChemOb :
    def __init__(self, value = 0, unitstring = "") :
        self.value = value
        num, den = read_unitstring(unitstring)
        self.numerator = num
        self.denominator = den

