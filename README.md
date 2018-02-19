# chem-calculator

Python helper functions for simple chemistry calculations. We have a bit of wikipedia webscraping, a bit of chemical-formula-parsing regex, and a bit of hand-copied chemical constants to help you through your chemistry classes. I hope this can alleviate the pain you have in your chemistry class. At least a bit.

You can do something like this after running chem_calculator.py :
```python
>>> mass('C6H12O6')
180.0
>>> mass('KAl(SO4)2·12H2O')
474.2
>>> h # plank constant
6.626e-34
>>> Cl # mass of Cl
35.5
>>> entropy('methane')
186.25
>>> entropy('CH4')
186.25
>>> entropy('ozone')
238.92
>>> enthalpy_formation('butane')
-126.3
>>> enthalpy_formation('H2O2')
-187.8
>>> entropy('O2')
We cannot find the So298 value of O2 (assume = 0.0).
0.0
>>> enthalpy_combustion('butane')
According to https://en.wikipedia.org/wiki/Butane, the ΔcHo298 of butane is -2.88 MJ mol−1
This is converted to -2876.90 kJ/mol
-2876.90 # return
>>> enthalpy_formation('glucose')
According to https://en.wikipedia.org/wiki/Glucose, the ΔfHo298 of glucose is -1271.00 kJ/mol
-1271.0 # return
```

Or something like :

```python
>>> from formula_matcher import *
>>> count_elements('Na2B4O7.10H2O')
{'B': 4, 'H': 20, 'Na': 2, 'O': 17}
>>> isChemicalFormula('John Cena')
False
```