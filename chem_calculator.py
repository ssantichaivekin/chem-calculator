# import defined mass constants H = 1, C = 12 Cl = 35.5
from read_write.run_mass_constants import *

# import defined val constants c = 3*10^8, h = 6.626e-34
from read_write.run_val_constants import * 

# import function to read mass
from mass_function import mass, fmass

# import function to read and process thermodynamic values
from scraper.wiki_scraper import entropy, enthalpy_formation, enthalpy_combustion
from scraper.wiki_scraper import wiki_mass as wikimass