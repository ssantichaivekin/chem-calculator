This is my to do list.
I think my productivity is very low. I should just do one thing at a time I guess.

- Move ./constants/ to ~/.chem_calculator_constants
- REFACTOR your files. Create a new folder called scraper. Put everything scraper-related inside that folder. Create a folder called matcher. Put everything that has a regex into that file. Create a new folder called filer_controller. Move everything csv-related to that folder. Now, the constants folder should only have constants. That is the way it should be. Just thinking about it makes me feel peace.

- Create `showwork()/hidework()` method. It should show what websites it obtain its datas from, or how it gets calculated.

This will most probably not get done. I don't think I will revisit this soon :

- Create lab objects like breaker. They can have properties like 'molar' and methods like pour_to().
- How about a 'react()' method?
- Rewrite README.md
- Maybe elements, compounds, etc deserves its own class.

Done

- Define a function mass mode that change each element's value to its mass.
- Define a function mass('name') which calculate the mass of such name. > mass('C6H12O6')
- Make that function support parenthesis--use recursion?
- Create MORE test cases for both functions.
- Create a new matcher class.
- The function `m()` should support `Na2B4O7.10 H2O` maybe also `Na2B4O7+10H2O`.
- Create a list of constants that should be defined like plank constant, the ideal gas constant, or moles.
- Integrate it to the terminal for it to run well. (I did it by adding alias ichem='ipython -i ~/location/chem-calculator/chem_calculator.py in my .zshrc)
- Enable the mass command to scrape the web for mass information.
- Grab thermodynamic datas from wikipedia.
