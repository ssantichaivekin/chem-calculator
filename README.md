# chem-calculator

Python helper functions for simple chemistry calculations. We have a bit of wikipedia webscraping, a bit of chemical-formula-parsing regex, and a bit of hand-copied chemical constants to help you through your chemistry classes. I hope this can alleviate the pain you have in your chemistry class. At least a bit.

You can do something like :
```python
=> %run chem_calculator
=> mass('C6H12O6')
180.0
=> mass('KAl(SO4)2·12H2O')
474.2
=> h # plank constant
6.626e-34
=> Cl # mass of Cl
35.5
```

Or something like :

```python
=> from formula_matcher import *
=> count_elements('Na2B4O7.10H2O')
{'B': 4, 'H': 20, 'Na': 2, 'O': 17}
=> isChemicalFormula('John Cena')
False
```