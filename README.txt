Wersja angielska pod polską

Przed rozpoczęciem należy pobrać plik 'zadanie_python.py' oraz plik z danymi (zapisać go jako 'matura.csv') do jednego folderu.

Włączenie programu:
- W 'Anaconda Prompt'/'Command Prompt' przejść do katalogu z plikiem zadanie_python.py
- wpisać 'python zadanie_python.py'
- Użytkować program wg poleceń podanych na ekranie

Użytkowanie programu:
- Wybór zadania do wykonania za pomocą cyfr '1','2','3','4','5','6' oraz literki 'q'
Gdzie:
    1 - średnia liczba osób, które przystąpiły do egzaminu
    2 - procentowa zdawalność
    3 - województwo o najlepszej zdawalności w konkretnym roku
    4 - województwa, które zanotowały regresję
    5 - porównanie dwóch województw
    6 - podanie czy województwo w danym roku zanotowało regres
    q - wyjście
- Wybór filtra za pomocą cyfr '1','2' oraz '3'
Gdzie
    1 - kobiety
    2 - mężczyźni
    3 - bez rozróżnienia (tryb domyślny)
- W zależności od wybranego zadania wystąpi możliwość wyboru następujących opcji:
+ wybór województwa (jedno lub dwa z): ['Dolnośląskie', 'Kujawsko-pomorskie', 'Lubelskie', 'Lubuskie', 'Łódzkie', 'Małopolskie', 'Mazowieckie', 'Opolskie', 'Podkarpackie', 'Podlaskie', 'Pomorskie', 'Śląskie', 'Świętokrzyskie', 'Warmińsko-Mazurskie', 'Wielkopolskie', 'Zachodniopomorskie']
+ wybór roku (jedno z): [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
- Program zapętla się do czasu wyboru zadania 'q'
- Na koniec następuje wczytywanie pliku z zewnętrznego serwera i wydrukowanie na ekranie pierwszych pięciu rzędów pobranego pliku

Testy z użyciem pytest:
- Należy przejść do katalogu z plikiem zadanie_python.py i wpisać:
- pytest -s zadanie_python.py
- wpisać 'q' (ewentualnie 'potestować' program samemu)
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
+ Province (one or two from the list): ['Dolnośląskie', 'Kujawsko-pomorskie', 'Lubelskie', 'Lubuskie', 'Łódzkie', 'Małopolskie', 'Mazowieckie', 'Opolskie', 'Podkarpackie', 'Podlaskie', 'Pomorskie', 'Śląskie', 'Świętokrzyskie', 'Warmińsko-Mazurskie', 'Wielkopolskie', 'Zachodniopomorskie']
+ year: [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
- Program loops until the 'q' task is chosen
- At the end program loads the external file and prints the first five rows on the screen

Tests with pytest:
- go to 'zadanie_python.py' file location and type:
- pytest -s zadanie_python.py
- type 'q' ( or 'test' the program yourself)
