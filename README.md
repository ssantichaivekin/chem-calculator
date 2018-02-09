# chemcalculator

This is a Python helper function designed to be used with interactive python. It takes advantage of Python's `global()` to set element and constant to the global scope (for example, we would set variable `H` to the value `1.008`. We can then use such constants for easy calculations.

The app should support something like `mass('C6H12O6')`. The function `info()` should look up last things search in `In` global variable and tell the user about the information. One cool thing is that wikipedia redirects `CuSO4` to its name `Copper(II) Sulfate`.

I am also looking towards to take advantage of Mac's `automation` and Python's `ipythonrc`. To help initialize the script.

I am also thinking about using Python's magic method for something pretty cool. Let's see how it goes. (Say `~'C6H12O6'` outputs `180.16`.)

I will also add web scraping to the ipython code to scrape chemistry properties from wikipedia. I feel like the program also deserve its own version of `whos`.
