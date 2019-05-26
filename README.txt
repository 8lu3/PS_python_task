Wersja angielska pod polsk¹

Przed rozpoczêciem nale¿y pobraæ plik 'zadanie_python.py' oraz plik z danymi (zapisaæ go jako 'matura.csv') do jednego folderu.

W³¹czenie programu:
- W 'Anaconda Prompt'/'Command Prompt' przejœæ do katalogu z plikiem zadanie_python.py
- wpisaæ 'python zadanie_python.py'
- U¿ytkowaæ program wg poleceñ podanych na ekranie

U¿ytkowanie programu:
- Wybór zadania do wykonania za pomoc¹ cyfr '1','2','3','4','5','6' oraz literki 'q'
Gdzie:
    1 - œrednia liczba osób, które przyst¹pi³y do egzaminu
    2 - procentowa zdawalnoœæ
    3 - województwo o najlepszej zdawalnoœci w konkretnym roku
    4 - województwa, które zanotowa³y regresjê
    5 - porównanie dwóch województw
    6 - podanie czy województwo w danym roku zanotowa³o regres
    q - wyjœcie
- Wybór filtra za pomoc¹ cyfr '1','2' oraz '3'
Gdzie
    1 - kobiety
    2 - mê¿czyŸni
    3 - bez rozró¿nienia (tryb domyœlny)
- W zale¿noœci od wybranego zadania wyst¹pi mo¿liwoœæ wyboru nastêpuj¹cych opcji:
+ wybór województwa (jedno lub dwa z): ['Dolnoœl¹skie', 'Kujawsko-pomorskie', 'Lubelskie', 'Lubuskie', '£ódzkie', 'Ma³opolskie', 'Mazowieckie', 'Opolskie', 'Podkarpackie', 'Podlaskie', 'Pomorskie', 'Œl¹skie', 'Œwiêtokrzyskie', 'Warmiñsko-Mazurskie', 'Wielkopolskie', 'Zachodniopomorskie']
+ wybór roku (jedno z): [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
- Program zapêtla siê do czasu wyboru zadania 'q'
- Na koniec nastêpuje wczytywanie pliku z zewnêtrznego serwera i wydrukowanie na ekranie pierwszych piêciu rzêdów pobranego pliku

Testy z u¿yciem pytest:
- Nale¿y przejœæ do katalogu z plikiem zadanie_python.py i wpisaæ:
- pytest -s zadanie_python.py
- wpisaæ 'q' (ewentualnie 'potestowaæ' program samemu)
----------------------------------------------------------

Before you start:
- download the 'zadanie_python.py' file and data file (save it as 'matura.csv') to one directory.

Running the program:
- Go to 'zadanie_python.py' file location in 'Anaconda Prompt'/'Command Prompt'
- write 'python zadanie_python.py'
- use the program with the showed commands

Using the program:
- Choose the task with the following numbers '1','2','3','4','5','6' or letter 'q'
Where:
    1 - average number of people who took the exam
    2 - percentage pass rate
    3 - the best province in the chosen year (the best pass rate)
    4 - provinces with regression
    5 - comparison of two provinces
    6 - whether regression happened for chosen district in the chosen year
    q - exit
- Choose the filter with the following numbers '1','2' oraz '3'
Where:
    1 - women
    2 - men
    3 - both (default)
- Depending on the chosen task the following options will be available:
+ Province (one or two from the list): ['Dolnoœl¹skie', 'Kujawsko-pomorskie', 'Lubelskie', 'Lubuskie', '£ódzkie', 'Ma³opolskie', 'Mazowieckie', 'Opolskie', 'Podkarpackie', 'Podlaskie', 'Pomorskie', 'Œl¹skie', 'Œwiêtokrzyskie', 'Warmiñsko-Mazurskie', 'Wielkopolskie', 'Zachodniopomorskie']
+ year: [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
- Program loops until the 'q' task's choice
- At the end program loads the external file and prints the first five rows on the screen

Tests with pytest:
- go to 'zadanie_python.py' file location and type:
- pytest -s zadanie_python.py
- type 'q' ( or 'test' the program yourself)
