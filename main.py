import random
import itertools

liczbaDni = 10**2
liczbaHoteli = 10**2
liczbaOsob = 10**4
prawdSpotk = 0.1

m = {}
rowno_dwa_spotkania = set()
dwa_spotkania = set()
trzy_spotkania = set()
pary_osob_dni = 0

for dzien in range(liczbaDni):
    hs = {}
    for osoba in range(liczbaOsob):
        if random.random() < prawdSpotk:
            hotel = random.randint(0, liczbaHoteli)
            hs[hotel] = hs.get(hotel, []) + [osoba]
    for v in hs.values():
        for pair in list(itertools.combinations(v, 2)):
            m[pair] = m.get(pair, 0)+1

for k, v in m.items():
    if v >= 2:
        pary_osob_dni = pary_osob_dni + (v*(v-1)/2)
        dwa_spotkania.add(k[0])
        dwa_spotkania.add(k[1])
    if v >= 3:
        trzy_spotkania.add(k[0])
        trzy_spotkania.add(k[1])

print("Liczba dni: "+str(liczbaDni))
print("Liczba hoteli: "+str(liczbaHoteli))
print("Liczba osob: "+str(liczbaOsob))
print("Prawdopodobieństwo spotkania: "+str(prawdSpotk))
print("----------------------------------------")
print("Pary które spotkały się minimum raz: "+str(len(m)))
print("Pary które spotkały się minimum dwa razy: "+str(len(dwa_spotkania)))
print("Pary które spotkały się minimum trzy razy: "+str(len(trzy_spotkania)))
print("Liczba podejrzanych par 'osób i dni': "+str(pary_osob_dni))
