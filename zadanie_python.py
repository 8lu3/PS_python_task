# -*- coding: utf-8 -*-
"""
Created on Fri May 24 13:37:26 2019

@author: Ania

"""

class ZadaniePython(object):
    
    def __init__(self):
        data =[]
        with open("matura.csv") as file:
#            print("Name of the file:",file.name)
#            print("Mode of the file:",file.mode)
#            print("Mode of the file:",file.encoding)
            raw_data = file.readlines()
            file.close()
            
        data = self.obrobka_danych(raw_data)
        self.data = data
        wojewodztwa, lata = self.listy_pomocnicze()
        self.wojewodztwa = wojewodztwa
        self.lata = lata
    # metoda dzieląca dane i podmieniająca typy dla konkretnych kolumn w surowych danych   
    def obrobka_danych(self,raw_data):
        data =[]
        for line in raw_data:
            subl = []
            for item in line.split(';'):
                if '\n' not in item:
                    subl.append(item)
                else:
                    subl.append(item[:-1])
            data.append(subl)
            
        for lines in data[1:]:
            if 'przystąpiło' in lines[1]:
                lines[1] = False
            else:
                lines[1]=True
            lines[3] = int(lines[3])
            lines[4] = int(lines[4])
        return data
    # metoda pomocnicza tworząca listy województw i lat występujących w danych
    def listy_pomocnicze(self):
        wojewodztwa = []
        lata = []
        for lines in self.data[1:]:
            if lines[0]!='Polska':
                if lines[0] not in wojewodztwa:
                    wojewodztwa.append(lines[0])
                if lines[3] not in lata:
                    lata.append(lines[3])
        return wojewodztwa, lata
    # metoda wyliczająca średnią liczbę osób przystępujących do egzaminu maturalnego w danym województwie na przestrzeni lat
    def avg_przyst(self,wojewodztwo,rok,plec=3):
        suma = 0
        i = 0
        if plec == 1:
            for lines in self.data:
                if wojewodztwo in lines[0] and not lines[1] and lines[3]<=rok and lines[2]=='kobiety':
                    suma+= lines[4]
                    i+=1
        elif plec == 2:
            for lines in self.data:
                if wojewodztwo in lines[0] and not lines[1] and lines[3]<=rok and lines[2]=='mężczyźni':
                    suma+= lines[4]
                    i+=1
        elif plec == 3:
            for lines in self.data:
                if wojewodztwo in lines[0] and not lines[1] and lines[3]<=rok:
                    suma+= lines[4]
                    i+=1
        return suma/i
    # metoda wyliczająca średnią procentową zdawalność egzaminu w danym wojewodztwie na przestrzeni lat
    def srednia_procentowa_zdawalnosc(self,wojewodztwo,do_roku,od_roku=2010,plec=3):
        suma_przystapilo = 0
        suma_zdalo = 0
        i = 0
        if plec == 1:
            for lines in self.data:
                if wojewodztwo in lines[0] and lines[3]>=od_roku and lines[3]<=do_roku and lines[2]=='kobiety':
                    if not lines[1]:
                        suma_przystapilo += lines[4]
                    else:
                        suma_zdalo += lines[4]
                    i+=1
        elif plec == 2:
            for lines in self.data:
                if wojewodztwo in lines[0] and lines[3]>=od_roku and lines[3]<=do_roku and lines[2]=='mężczyźni':
                    if not lines[1]:
                        suma_przystapilo += lines[4]
                    else:
                        suma_zdalo += lines[4]
                    i+=1 
        elif plec == 3:
            for lines in self.data:
                if wojewodztwo in lines[0] and lines[3]>=od_roku and lines[3]<=do_roku:
                    if not lines[1]:
                        suma_przystapilo += lines[4]
                    else:
                        suma_zdalo += lines[4]
                    i+=1
        return suma_zdalo/suma_przystapilo
    # metoda wyliczająca najlepszą zdawalność oraz województwo z najlepszą zdawalnością  w danym roku
    def najlepsza_zdawalosc_w_danym_roku(self,rok,plec=3):
        zdawalnosci = []
        for wojewodztwo in self.wojewodztwa:
            zdawalnosci.append(self.srednia_procentowa_zdawalnosc(wojewodztwo,rok,rok,plec))
        
        najlepsza_zdawalnosc = 0
        i=0
        wojewodztwo_z_najlepsza_zdawalnoscia = []
        for item in zdawalnosci:
            if item>najlepsza_zdawalnosc:
                najlepsza_zdawalnosc = item
                wojewodztwo_z_najlepsza_zdawalnoscia = self.wojewodztwa[i]
            i+=1
        return najlepsza_zdawalnosc, wojewodztwo_z_najlepsza_zdawalnoscia
    # metoda wyliczająca czy w podanym województwie i roku wystąpił regres
    def czy_regres(self,wojewodztwo,rok,plec=3):
        odpowiedz = False
        teraz = self.srednia_procentowa_zdawalnosc(wojewodztwo,rok,od_roku=rok,plec=plec)
        wczesniej = self.srednia_procentowa_zdawalnosc(wojewodztwo,rok-1,od_roku=rok-1,plec=plec)
        if wczesniej > teraz:
            odpowiedz = True
        return wojewodztwo, rok-1, rok, odpowiedz
    # metoda wyliczająca regres dla całego zbioru danych
    def sprawdz_regres(self,plec=3):
        sprawdz_regres = []
        for rok in self.lata[1:]:
            for woj in self.wojewodztwa:
                sprawdz_regres.append(self.czy_regres(woj,rok,plec=plec))
        regres = []
        for line in sprawdz_regres:
            if line[3]==True:
                regres.append(line)
        return regres
    # metoda porównująca zdawalność w dwóch podanych województwach
    def porownanie_wojewodztw(self,wojewodztwo1,wojewodztwo2, plec=3):
        woj1 = []
        woj2 = []
        odpowiedz = []
        for rok in self.lata:
            woj1.append(self.srednia_procentowa_zdawalnosc(wojewodztwo1,rok,plec=plec))
            woj2.append(self.srednia_procentowa_zdawalnosc(wojewodztwo2,rok,plec=plec))
        for item in range(len(woj1)):
            if woj1[item]>woj2[item]:
                odpowiedz.append([self.lata[item], wojewodztwo1])
            else:
                odpowiedz.append([self.lata[item], wojewodztwo2])
        return odpowiedz  
    # pomocnicza metoda do wydrukowania list wyboru
    def printowanie_list(self,co,czy_regres=0):
        print("Do wyboru:")
        if co == 1:
            print(self.wojewodztwa)
            print(self.lata[czy_regres:])
        elif co == 2:
            print(self.wojewodztwa)
        elif co == 3:
            print(self.lata[czy_regres:])
    # metoda pomocnicza do wyboru argumentów do zadań        
    def wybor_argumentow(self,co):
        wybor_wojewodztwa=''
        wybor_rok = ''
        wybor_wojewodztwa2 = ''
        if co == 1:
            while wybor_wojewodztwa not in self.wojewodztwa:
                wybor_wojewodztwa = input('Podaj wojewodztwo: ')
                wybor_wojewodztwa = wybor_wojewodztwa.title()
            while wybor_rok not in self.lata:
                wybor_rok = int(input('Podaj rok: '))
        if co == 2:
            while wybor_rok not in self.lata:
                wybor_rok = int(input('Podaj rok: '))
        if co == 3:
            while wybor_wojewodztwa not in self.wojewodztwa:
                wybor_wojewodztwa = input('Podaj wojewodztwo pierwsze: ')
                wybor_wojewodztwa = wybor_wojewodztwa.title()
            while wybor_wojewodztwa2 not in self.wojewodztwa:
                wybor_wojewodztwa2 = input('Podaj wojewodztwo drugie: ')
                wybor_wojewodztwa2 = wybor_wojewodztwa2.title()
        return wybor_wojewodztwa,wybor_rok,wybor_wojewodztwa2
    
    def wybranie_zadania(self):
        wybor_zadania = ''
        while wybor_zadania not in {"1","2","3","4","5","6","q"}:
            print("\nWybierz z listy\n")
            wybor_zadania=input("Podaj:\n 1 - obliczenie średniej liczby osób, które przystąpiły do egzaminu dla danego województwa na przestrzeni lat, do podanego roku włącznie,\n"+
              "2 - obliczenie procentowej zdawalności dla danego województwa na przestrzeni lat, \n"+
              "3 - podanie województwa o najlepszej zdawalności w konkretnym roku, \n"+
              "4 - wykrycie województw, które zanotowały regresję, \n"+
              "5 - porównanie dwóch województw, \n"+
              "6 - podanie czy województwo w danym roku zanotowało regres. \n"+
              "q - wyjście \n")
        print("Wybrałeś: " + wybor_zadania)
        return wybor_zadania
            
    def wybranie_plci(self):
        wybor_plci=int(input("Podaj dla jakiego zbioru wykonać obliczenia:\n"+
                         "1 - kobiety,\n"+
                         "2 - mężczyźni \n"+
                         "3 - bez rozróżnienia (tryb domyślny) \n"))
        if wybor_plci not in {1,2,3}:
            wybor_plci = 3
        print("Wybrałeś: " + str(wybor_plci))
        return wybor_plci
    
b = ZadaniePython()
pomocnicze_wojewodztwa,pomocnicze_lata = b.listy_pomocnicze()
wybor_zadania=''
# pętla do interfejsu użytkownika
while wybor_zadania!='q':
    wybor_zadania = b.wybranie_zadania()
    if wybor_zadania=='q':
            break
    else:    
        wybor_plci = b.wybranie_plci()
        wybor_wojewodztwa = ''
        wybor_wojewodztwa2 = ''
        wybor_rok = 0
        if wybor_zadania == '1': # średnia osób, które przystąpiły
            b.printowanie_list(1)
            wybor_wojewodztwa, wybor_rok,wybor_wojewodztwa2 = b.wybor_argumentow(1)
            print("\nOdpowiedź:")
            print(b.avg_przyst(wybor_wojewodztwa,wybor_rok,wybor_plci))
        elif wybor_zadania == '2': # średnia procentowa zdawalność   
            b.printowanie_list(1)
            wybor_wojewodztwa, wybor_rok,wybor_wojewodztwa2 = b.wybor_argumentow(1)
            print("\nOdpowiedź:")
            print(b.srednia_procentowa_zdawalnosc(wybor_wojewodztwa,wybor_rok,plec=wybor_plci))
        elif wybor_zadania == '3': # najlepsza zdawalność
            b.printowanie_list(3)
            wybor_wojewodztwa, wybor_rok,wybor_wojewodztwa2 = b.wybor_argumentow(2)
            print("\nOdpowiedź:")
            print(b.najlepsza_zdawalosc_w_danym_roku(wybor_rok,plec=wybor_plci))
        elif wybor_zadania == '4': # regres ogólny
            regres_do_printowania = []
            regres_do_printowania = b.sprawdz_regres(plec=wybor_plci)
            print("\nOdpowiedź:")
            for line in regres_do_printowania:
                print(line[0],str(line[1])+'-->'+str(line[2]))
        elif wybor_zadania == '5': # porównanie województw
            b.printowanie_list(2)
            wybor_wojewodztwa, wybor_rok, wybor_wojewodztwa2 = b.wybor_argumentow(3)
            print("\nOdpowiedź:")
            print(b.porownanie_wojewodztw(wybor_wojewodztwa,wybor_wojewodztwa2,plec=wybor_plci))
        else: # regres w danym miejscu i roku
            b.printowanie_list(1,1)
            wybor_wojewodztwa, wybor_rok,wybor_wojewodztwa2 = b.wybor_argumentow(1)
            if wybor_rok==2010:
                print("Regres niemożliwy do wyliczenia (nie ma poprzedniej wartości), podstawiam rok 2011")
                wybor_rok=2011
            print("\nOdpowiedź:")
            print(b.czy_regres(wybor_wojewodztwa,wybor_rok,plec=wybor_plci))
            
    
print("Bonus pierwszy, wczytywanie pliku .csv z serwera zewnętrznego (nie plik lokalny)")

# BONUS PIERWSZY - wczytywanie pliku z serwera
import pandas as pd
dane_dane = pd.read_csv(
        "https://www.dane.gov.pl/media/resources/20190520/Liczba_os%C3%B3b_kt%C3%B3re_przystapi%C5%82y_lub_zda%C5%82y_egzamin_maturalny.csv",
        encoding='Windows-1250',sep=';')
print(dane_dane.head())

# klasa do testów pytest
class TestZadaniePython(object):
    
    def setup(self):
        self.zpc = ZadaniePython()
    
    def test_listy_pomocnicze(self):
        x = ['Dolnośląskie', 'Kujawsko-pomorskie', 'Lubelskie', 'Lubuskie', 'Łódzkie', 'Małopolskie', 'Mazowieckie', 'Opolskie', 'Podkarpackie', 'Podlaskie', 'Pomorskie', 'Śląskie', 'Świętokrzyskie', 'Warmińsko-Mazurskie', 'Wielkopolskie', 'Zachodniopomorskie'],[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
        assert x == self.zpc.listy_pomocnicze()
    
    def test_avg_przyst(self):
        x = 10689.5
        assert x == self.zpc.avg_przyst("Pomorskie",2013,plec=1)

    def test_srednia_procentowa_zdawalnosc(self):
        x = 0.7747592714335434
        assert x == self.zpc.srednia_procentowa_zdawalnosc("Mazowieckie",2014,od_roku=2010,plec=2)
        
    def test_najlepsza_zdawalosc_w_danym_roku(self):
        x = (0.8212769020369971, "Małopolskie")
        assert x == self.zpc.najlepsza_zdawalosc_w_danym_roku(2016,plec=1)

    def test_czy_regres(self):
        x = ('Warmińsko-Mazurskie', 2012, 2013, False)
        assert x == self.zpc.czy_regres("Warmińsko-Mazurskie",2013,plec=3)
       
    def test_sprawdz_regres(self):
        x = [('Dolnośląskie', 2010, 2011, True), ('Kujawsko-pomorskie', 2010, 2011, True), ('Lubelskie', 2010, 2011, True), ('Lubuskie', 2010, 2011, True), ('Łódzkie', 2010, 2011, True), ('Małopolskie', 2010, 2011, True), ('Mazowieckie', 2010, 2011, True), ('Opolskie', 2010, 2011, True), ('Podkarpackie', 2010, 2011, True), ('Podlaskie', 2010, 2011, True), ('Pomorskie', 2010, 2011, True), ('Śląskie', 2010, 2011, True), ('Świętokrzyskie', 2010, 2011, True), ('Warmińsko-Mazurskie', 2010, 2011, True), ('Wielkopolskie', 2010, 2011, True), ('Zachodniopomorskie', 2010, 2011, True), ('Dolnośląskie', 2013, 2014, True), ('Kujawsko-pomorskie', 2013, 2014, True), ('Lubelskie', 2013, 2014, True), ('Lubuskie', 2013, 2014, True), ('Łódzkie', 2013, 2014, True), ('Małopolskie', 2013, 2014, True), ('Mazowieckie', 2013, 2014, True), ('Opolskie', 2013, 2014, True), ('Podkarpackie', 2013, 2014, True), ('Podlaskie', 2013, 2014, True), ('Pomorskie', 2013, 2014, True), ('Śląskie', 2013, 2014, True), ('Świętokrzyskie', 2013, 2014, True), ('Warmińsko-Mazurskie', 2013, 2014, True), ('Wielkopolskie', 2013, 2014, True), ('Zachodniopomorskie', 2013, 2014, True), ('Dolnośląskie', 2016, 2017, True), ('Lubelskie', 2016, 2017, True), ('Lubuskie', 2016, 2017, True), ('Łódzkie', 2016, 2017, True), ('Mazowieckie', 2016, 2017, True), ('Opolskie', 2016, 2017, True), ('Podkarpackie', 2016, 2017, True), ('Podlaskie', 2016, 2017, True), ('Pomorskie', 2016, 2017, True), ('Śląskie', 2016, 2017, True), ('Świętokrzyskie', 2016, 2017, True), ('Warmińsko-Mazurskie', 2016, 2017, True), ('Wielkopolskie', 2016, 2017, True), ('Zachodniopomorskie', 2016, 2017, True), ('Kujawsko-pomorskie', 2017, 2018, True), ('Pomorskie', 2017, 2018, True)]
        assert x == self.zpc.sprawdz_regres(plec=1)

    def test_porownanie_wojewodztw(self):
        x = [[2010, 'Lubuskie'], [2011, 'Lubuskie'], [2012, 'Lubuskie'], [2013, 'Lubuskie'], [2014, 'Lubuskie'], [2015, 'Lubuskie'], [2016, 'Lubuskie'], [2017, 'Lubuskie'], [2018, 'Lubuskie']]
        assert x == self.zpc.porownanie_wojewodztw("Lubelskie","Lubuskie",plec=2)
