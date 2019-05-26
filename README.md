# PS_python_task
Zadanie back-end, staż, Profil Software

## Before you start:
- download the `zadanie_python.py` file and data file (save it as `matura.csv`) to one directory.

## Running the program:
- Go to `zadanie_python.py` file location in `Anaconda Prompt`/`Command Prompt`
- write `python zadanie_python.py`
- use the program with the showed commands

## Using the program:
- Choose the task with the following numbers `1`,`2`,`3`,`4`,`5`,`6` or letter `q`

Where:

    1 - average number of people who took the exam
    2 - percentage pass rate
    3 - the best province in the chosen year (the best pass rate)
    4 - provinces with regression
    5 - comparison of two provinces
    6 - whether regression happened for chosen district in the chosen year
    q - exit
- Choose the filter with the following numbers `1`,`2` oraz `3`

Where:

    1 - women
    2 - men
    3 - both (default)
- Depending on the chosen task the following options will be available:
+ Province (one or two from the list):

`['Dolnośląskie', 'Kujawsko-pomorskie', 'Lubelskie', 'Lubuskie', 'Łódzkie', 'Małopolskie', 'Mazowieckie', 'Opolskie', 'Podkarpackie', 'Podlaskie', 'Pomorskie', 'Śląskie', 'Świętokrzyskie', 'Warmińsko-Mazurskie', 'Wielkopolskie', 'Zachodniopomorskie']`
+ year: 

`[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]`
- Program loops until the `q` task is chosen
- At the end program loads the external file and prints the first five rows on the screen (using pandas - has to be installed first)

## Tests with pytest:
- go to `zadanie_python.py` file location and type:
- `pytest -s zadanie_python.py`
- type `q` ( or 'test' the program yourself)
