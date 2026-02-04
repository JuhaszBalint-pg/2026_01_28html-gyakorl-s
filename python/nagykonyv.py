konyvek = []
darabszam = 0
with open('python\konyvek.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        darabszam += 1
        adatok = sor.strip().split(';')
        nev = adatok[0]
        szul_ev = int(adatok[1])
        hal_ev = int(adatok[2]) if adatok[2] !='' else 2005
        nemzetiseg = adatok[3]
        cim = adatok[4]
        helyezes = int(adatok[5])
        konyv = {'nev': nev, 'születési_év': int(szul_ev), 'halálozási_év': hal_ev, 'nemzetiség': nemzetiseg, 'cím' : cim, 'helyezés' : helyezes}
        konyvek.append(konyv)

print(f'{konyvek=}')

print('\n1. feladat')
print(f' Az állományban {darabszam} db könyv adatai szerepelnek.')

magyar_konyvek = []
print("2. feladat")
for konyv in konyvek:
    if konyv['nemzetiség'] == 'magyar':
        magyar_konyvek.append(konyv)

legjobb_konyv = magyar_konyvek[0]
print(len(magyar_konyvek))
for konyv in magyar_konyvek:
    if konyv['helyezés'] < legjobb_konyv['helyezés']:
        legjobb_konyv = konyv

print(f'a legjobb magyar könyv a {legjobb_konyv['cím']}, helyezése: {legjobb_konyv['helyezés']}')

print('3. feladat')

nemet_irok = []
for i in konyvek:
    if i['nemzetiség'] == 'német':
        nemet_irok.append(konyv['nev'])

if len(nemet_irok) > 0:
    print('szerepel német író könyve')
else:
    print('Nincsen német író')

print('4. feladat')
idos_irok = set()
eletkor = 90
for konyv in konyvek:
    if ((konyv['halálozási_év'] - konyv['születési_év']) >= 90):
        idos_irok.add(konyv['nev'])

print(idos_irok)