Wersja angielska pod polsk�

Przed rozpocz�ciem nale�y pobra� plik 'zadanie_python.py' oraz plik z danymi (zapisa� go jako 'matura.csv') do jednego folderu.

W��czenie programu:
- W 'Anaconda Prompt'/'Command Prompt' przej�� do katalogu z plikiem zadanie_python.py
- wpisa� 'python zadanie_python.py'
- U�ytkowa� program wg polece� podanych na ekranie

U�ytkowanie programu:
- Wyb�r zadania do wykonania za pomoc� cyfr '1','2','3','4','5','6' oraz literki 'q'
Gdzie:
    1 - �rednia liczba os�b, kt�re przyst�pi�y do egzaminu
    2 - procentowa zdawalno��
    3 - wojew�dztwo o najlepszej zdawalno�ci w konkretnym roku
    4 - wojew�dztwa, kt�re zanotowa�y regresj�
    5 - por�wnanie dw�ch wojew�dztw
    6 - podanie czy wojew�dztwo w danym roku zanotowa�o regres
    q - wyj�cie
- Wyb�r filtra za pomoc� cyfr '1','2' oraz '3'
Gdzie
    1 - kobiety
    2 - m�czy�ni
    3 - bez rozr�nienia (tryb domy�lny)
- W zale�no�ci od wybranego zadania wyst�pi mo�liwo�� wyboru nast�puj�cych opcji:
+ wyb�r wojew�dztwa (jedno lub dwa z): ['Dolno�l�skie', 'Kujawsko-pomorskie', 'Lubelskie', 'Lubuskie', '��dzkie', 'Ma�opolskie', 'Mazowieckie', 'Opolskie', 'Podkarpackie', 'Podlaskie', 'Pomorskie', '�l�skie', '�wi�tokrzyskie', 'Warmi�sko-Mazurskie', 'Wielkopolskie', 'Zachodniopomorskie']
+ wyb�r roku (jedno z): [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
- Program zap�tla si� do czasu wyboru zadania 'q'
- Na koniec nast�puje wczytywanie pliku z zewn�trznego serwera i wydrukowanie na ekranie pierwszych pi�ciu rz�d�w pobranego pliku

Testy z u�yciem pytest:
- Nale�y przej�� do katalogu z plikiem zadanie_python.py i wpisa�:
- pytest -s zadanie_python.py
- wpisa� 'q' (ewentualnie 'potestowa�' program samemu)
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
+ Province (one or two from the list): ['Dolno�l�skie', 'Kujawsko-pomorskie', 'Lubelskie', 'Lubuskie', '��dzkie', 'Ma�opolskie', 'Mazowieckie', 'Opolskie', 'Podkarpackie', 'Podlaskie', 'Pomorskie', '�l�skie', '�wi�tokrzyskie', 'Warmi�sko-Mazurskie', 'Wielkopolskie', 'Zachodniopomorskie']
+ year: [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
- Program loops until the 'q' task's choice
- At the end program loads the external file and prints the first five rows on the screen

Tests with pytest:
- go to 'zadanie_python.py' file location and type:
- pytest -s zadanie_python.py
- type 'q' ( or 'test' the program yourself)
