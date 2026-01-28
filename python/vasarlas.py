'''
1. feladat: Vásárlás	8 pont
Írjon programot vasarlas.py néven, ami billentyűzetről bekéri egy termék árát forintban,
az euro árfolyamát és egy euro összeget, majd kiírja a minta szerint, hogy a beírt euroért meg tudjuk-e vásárolni a terméket. 
Minta:
Kérem a termék árát forintban: 10000
Kérem az euro árfolyamát: 380.56
Mennyi euróval rendelkezel: 50
A terméket meg tudod vásárolni!

Kérem a termék árát forintban: 10000
Kérem az euro árfolyamát: 380.56
Mennyi euróval rendelkezel: 5.15
Nincs elég euród a termék megvásárlására!
'''

termekar = float(input('Adja meg a termék árát Ft-ban\n'))
eurarfolyam = float(input('Adja meg az euró árfolyamát\n'))
eurvasarlo = float(input('Adja meg a rendelkezésre álló eurót\n'))

if termekar/eurarfolyam <= eurvasarlo:
    print('A terméket meg tudja vásárolni')
else:
    print('Nincs elég euródd a termék megvásárlására!')