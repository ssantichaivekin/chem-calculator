# chem-calculator

Python helper functions for simple chemistry calculations. We have a bit of wikipedia webscraping, a bit of chemical-formula-parsing regex, and a bit of hand-copied chemical constants to help you through your chemistry classes. I hope this can alleviate the pain you have in your chemistry class. At least a bit.

You can do something like this after running chem_calculator.py :
```python
=> mass('C6H12O6')
180.0
=> mass('KAl(SO4)2·12H2O')
474.2
=> h # plank constant
6.626e-34
=> Cl # mass of Cl
35.5
=> entropy('methane')
186.25
=> entropy('CH4')
186.25
=> entropy('ozone')
238.92
=> enthalpy_formation('butane')
-126.3
=> enthalpy_formation('H2O2')
-187.8
```

Or something like :

```python
=> from formula_matcher import *
=> count_elements('Na2B4O7.10H2O')
{'B': 4, 'H': 20, 'Na': 2, 'O': 17}
=> isChemicalFormula('John Cena')
False
```

The problem we are having right now is that our algorithm is designed to grab value with decimal point, while some values on wikipedia does not have one. For example, Glucose has the standard entropy of formation of `−1271 kJ/mol`. This won't work for our algorithm. Also, we will have to show our sources when we scrape to follow the wikipedia creative commons license. And also to show the user what might have gone wrong in a query. Also, some of the data in wikipedia have a different unit. Butane has the enthalpy of combustion of `−2.8781 MJ/mol`. We should set our webscraper to account for that...