'''
The mass constant function sets the element variables to be its mass.
For example, c = 3e8. We will implement a wikipedia
web-scrape constant function later.

You will have to call this with a %run -i and call run_mass_constants()
in order for it to initialize all the global variables.
'''

from file_readers import read_constants_from_file


def run_val_constants() :
    '''
    Add element constant symbol and values to the global variables.
    '''
    constant_dict = read_constants_from_file()
    globals().update(constant_dict)

run_val_constants()

if __name__ == '__main__' :
    assert 3e8 * 0.9 <= c <= 3e8 * 1.1
    assert 6.626e-34 * 0.9 <= h <= 6.626e-34 * 1.1
