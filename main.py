import random
import itertools

liczbaDni = 10**2
liczbaHoteli = 10**2
liczbaOsob = 10**4
prawdSpotk = 0.1

podejrzane_pary = {}
liczba_podejrzanych_osob = set()
jedno_spotkanie = 0
dwa_spotkania = 0
trzy_spotkania = 0
pary_osob_dni = 0

for dzien in range(liczbaDni):
    h = {}
    for osoba in range(liczbaOsob):
        if random.random() < prawdSpotk:
            hotel = random.randint(0, liczbaHoteli)
            h[hotel] = h.get(hotel, []) + [osoba]
    for v in h.values():
        for pair in list(itertools.combinations(v, 2)):
            podejrzane_pary[pair] = podejrzane_pary.get(pair, 0)+1

for k, v in podejrzane_pary.items():
    if v == 1:
        jedno_spotkanie += 1
    if v== 2:
        dwa_spotkania +=  1
    if v >= 2:
        pary_osob_dni = pary_osob_dni + (v*(v-1)/2)
        liczba_podejrzanych_osob.add(k[0])
        liczba_podejrzanych_osob.add(k[1])
    if v == 3:
        trzy_spotkania += 1

print("Liczba dni: "+str(liczbaDni))
print("Liczba hoteli: "+str(liczbaHoteli))
print("Liczba osob: "+str(liczbaOsob))
print("Prawdopodobieństwo spotkania: "+str(prawdSpotk))
print("----------------------------------------")
print("Pary które spotkały się minimum raz: "+str(len(podejrzane_pary)))
print("Pary które spotkały się raz: "+str(jedno_spotkanie))
print("Pary które spotkały się dwa razy: "+str((dwa_spotkania)))
print("Pary które spotkały się trzy razy: "+str((trzy_spotkania)))
print("Liczba podejrzanych osób: "+str(len(liczba_podejrzanych_osob)))
print("Liczba podejrzanych par 'osób i dni': "+str(int(pary_osob_dni)))
