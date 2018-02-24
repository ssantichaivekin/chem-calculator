'''
The mass constant function sets the element variables to be its mass.
For example, H = 1, He = 4, Li = 3.
'''

from read_write.file_readers import read_mass_from_file


def run_mass_constants() :
    '''
    Add element names and masses to the global variables.
    '''
    element_dict = read_mass_from_file()
    globals().update(element_dict)


# The file now calls run_mass_constants directly.
run_mass_constants()

if __name__ == '__main__' :
    assert H < He < Li < C < O < Cl
    assert 12 <= C < 12.5 # 12.0107

