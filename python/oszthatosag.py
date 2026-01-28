'''
Írjon programot oszthato.py néven. A programban hozzon létre egy függvényt oszthato néven
ami egy egész számot kap paraméterként és igaz értéket ad vissza,
ha a szám 7-tel osztható, de 3-mal nem.
A függvény segítségével számolja ki azon 3 jegyű számok átlagát, amire a függvény igaz értékkel tér vissza.
Minta:
A 7-tel osztható és 3-mal nem osztható 3 jegyű számok átlaga: 551.2705882352941
'''
useri = int(input('Adjon meg egy számot!\n'))
haromjegyu = []
ertek = 0
list = []

def oszthato(szam):
    if szam % 7 == 0 and szam % 3 != 0:
        return True
    else:
        return False
    
for i in range(100, 1000):
    oszthato(useri)    
    if i % useri == 0:
        haromjegyu.append(i)

print(f'{haromjegyu}')

mennyiseg = len(haromjegyu)
ertek = sum(haromjegyu)

print('A 7-tel osztható és 3-mal nem osztható 3 jegyű számok átlaga:')
print(f'{ertek/mennyiseg:.3f}')