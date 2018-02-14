'''
The mass mode function sets the element variables to be its mass.
For example, H = 1, He = 4, Li = 3.
We now have an inaccurate mass mode. We will implement a wikipedia
web-scrape mass mode later.

You will have to call this with a %run -i and call mass_mode()
in order for it to initialize all the global variables.
'''

from scraper.file_readers import read_mass_from_file


def mass_mode() :
    '''
    The mass mode is now back here.
    Add element names and masses to the global variables.
    '''
    element_dict = read_mass_from_file()
    globals().update(element_dict)

# With this new mass mode call line!
if __name__ == '__main__' :
    mass_mode()
    assert H < He < Li < C < O < Cl
    assert 12 <= C < 12.5 # 12.0107

