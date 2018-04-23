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
        self and add its corresponding value to the value. Modify self.
        '''

    # Maybe not?
    # def use_matrix(self) :
    #     '''
    #     Use matrix system for units. Convert any non-matrix units to matrix.
    #     '''


