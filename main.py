import random
pierwszy_raz = {}
drugi_raz = {}
trzeci_raz = {}

def calculate(liczba_osob, prawdopodobienstwo_przenocowania_w_hotelu, liczba_hoteli, liczba_dni):
    print(liczba_osob + " " + prawdopodobienstwo_przenocowania_w_hotelu + " " + liczba_hoteli + " " + liczba_dni);
    for dzien in liczba_dni:
        for osoba in liczba_osob:
            if random.randint(0, 9) == 0:
                pierwszy_raz[osoba] = True;
            else:
                pierwszy_raz[osoba] = False



