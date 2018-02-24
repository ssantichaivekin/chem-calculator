Python helper functions for simple chemistry calculations. I have a bit of wikipedia webscraping, a bit of chemical-formula-parsing regex, and a bit of hand-copied chemical constants to help you through your chemistry classes. I hope this can alleviate the pain you have in your chemistry class/lab. At least a bit.

## How to run? 

In your console, type:

```bash
ipython -i ~/yourdownloadlocation/chem-calculator/chem_calculator.py
```

You can add an alias to your .bash_profile or .zshrc.

```bash
alias pychem='ipython -i ~/Desktop/Code/chem-calculator/chem_calculator.py'
```

## What can you do with it?

This application is designed to do calculations related to mass.
However, it also includes thermodynamics data webscraping and other
common chmistry constants like mol, c, h, R, etc.

```python
>>> mass('C6H12O6')
-180.0
>>> mass('KAl(SO4)2·12H2O')
474.2
>>> h # plank constant
-6.626e-34
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
0.0 # return
>>> enthalpy_combustion('butane')
According to https://en.wikipedia.org/wiki/Butane, the ΔcHo298 of butane is -2.88 MJ mol−1
This is converted to -2876.90 kJ/mol
-2876.90 # return
>>> enthalpy_formation('glucose')
According to https://en.wikipedia.org/wiki/Glucose, the ΔfHo298 of glucose is -1271.00 kJ/mol
-1271.0 # return
```

## What is going on behind the scene?

Some regex parsing and Beautiful Soap webscraping.

```python
>>> from matcher.formula_matcher import *
>>> count_elements('Na2B4O7.10H2O')
{'B': 4, 'H': 20, 'Na': 2, 'O': 17}
>>> isChemicalFormula('John Cena')
False

>>> from scraper.wiki_scraper import wiki_value_from_key
# The keyword for entropy is So298
# The unit we are expecting is 'J·(K·mol)−1'
>>> wiki_value_from_key('CH4', 'So298', ['J·(K·mol)−1'])
According to https://en.wikipedia.org/wiki/CH4, the So298 of CH4 is 186.25 J·(K·mol)−1
186.25 # return
```

## Does it work well?

The webscraping part still needs a lot of improvement. It still fails to grab thermodynamic
datas of many common objects (most notably glucose). The formula parsing part works perfectly well.

<img src="https://github.com/ssantichaivekin/chem-calculator/blob/master/screenshot.png" width="600">


