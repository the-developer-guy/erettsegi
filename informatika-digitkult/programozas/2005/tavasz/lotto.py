
# 0. feladat
# Olvaassuk be a lottosz.dat állományt, és tároljuk el a benne lévő adatokat

lottoszamok = []
with open("lottosz.dat", "rt", encoding="utf-8") as file:
    for line in file:
        szamok = line.split(" ")
        feldolgozott_szamok = []
        for szam in szamok:
            feldolgozott_szamok.append(int(szam))
        lottoszamok.append(feldolgozott_szamok)


# 1. feladat
# Kérje be a felhasználótól az 52. hét megadott lottószámait!

bekert_szamok = []
for i in range(5):
    szam = int(input(f"Kérem a(z) {i + 1}. lottószámot: "))
    bekert_szamok.append(szam)


# 2. feladat
# A program rendezze a bekért lottószámokat emelkedő sorrendbe!
# A rendezett számokat írja ki a képernyőre!

n = len(bekert_szamok)
for i in range(n - 1):
    minimum_index = i
    for j in range(i + 1, n):
        if bekert_szamok[j] < bekert_szamok[minimum_index]:
            minimum_index = j

    csere = bekert_szamok[i]
    bekert_szamok[i] = bekert_szamok[minimum_index]
    bekert_szamok[minimum_index] = csere

print("A rendezett lottószámok: "
      f"{bekert_szamok[0]}, "
      f"{bekert_szamok[1]}, "
      f"{bekert_szamok[2]}, "
      f"{bekert_szamok[3]}, "
      f"{bekert_szamok[4]}")


# 3. feladat
# Kérjen be a felhasználótól egy egész számot 1-51 között!
# A bekért adatot nem kell ellenőrizni!

bekert_het = int(input("Kérem adja meg a hét számát (1-51): "))


# 4. feladat
# Írja ki a képernyőre a bekért számnak megfelelő sorszámú hét lottószámait
# a lottosz.dat állományban lévő adatok alapján!

print(f"A(z) {bekert_het}. hét lottószámai: "
      f"{lottoszamok[bekert_het - 1][0]}, "
      f"{lottoszamok[bekert_het - 1][1]}, "
      f"{lottoszamok[bekert_het - 1][2]}, "
      f"{lottoszamok[bekert_het - 1][3]}, "
      f"{lottoszamok[bekert_het - 1][4]}")


# 5. feladat
# A lottosz.dat állományból beolvasott adatok alapján döntse el,
# hogy volt-e olyan szám, amit egyszer sem húztak ki az 51 hét alatt!
# A döntés eredményét (Van/Nincs) írja ki a képernyőre!

osszes_lottoszam = []
for heti_lottoszamok in lottoszamok:
    for szam in heti_lottoszamok:
        osszes_lottoszam.append(szam)

van_kihuzatlan_szam = False
for keresett_szam in range(1, 91):
    szam_megtalalva = False
    for lottoszam in osszes_lottoszam:
        if lottoszam == keresett_szam:
            szam_megtalalva = True
            break
    if szam_megtalalva == False:
        van_kihuzatlan_szam = True
        break

if van_kihuzatlan_szam:
    print("Volt olyan szám, amit egyszer sem húztak ki az első 51 héten")
else:
    print("Minden számot kihúztak az első 51 héten")


# 6. feladat
# A lottosz.dat állományban lévő adatok alapján állapítsa meg,
# hogy hányszor volt páratlan szám a kihúzott lottószámok között!
# Az eredményt a képernyőre írja ki!

paratlan_szamlalo = 0
for heti_lottoszamok in lottoszamok:
    for szam in heti_lottoszamok:
        if szam % 2 == 1:
            paratlan_szamlalo += 1

print(f"{paratlan_szamlalo} db. páratlan szám volt az első 51 héten.")


# 7. feladat
# Fűzze hozzá a lottosz.dat állományból beolvasott lottószámok után
# a felhasználótól bekért, és rendezett 52. hét lottószámait,
# majd írja ki az összes lottószámot a lotto52.ki szöveges fájlba!
# A fájlban egy sorba egy hét lottószámai kerüljenek,
# szóközzel elválasztva egymástól!

lottoszamok.append(bekert_szamok)

with open("lotto52.ki", "wt", encoding="utf-8") as file:
    for heti_lottoszamok in lottoszamok:
        file.write(f"{heti_lottoszamok[0]} "
                   f"{heti_lottoszamok[1]} "
                   f"{heti_lottoszamok[2]} "
                   f"{heti_lottoszamok[3]} "
                   f"{heti_lottoszamok[4]}\n")


# 8. feladat
# Határozza meg a lotto52.ki állomány adatai alapján,
# hogy az egyes számokat hányszor húzták ki 2003-ban.
# Az eredményt írja ki a képernyőre a következő formában:
# az első sor első eleme az a szám legyen ahányszor az egyest kihúzták!
# Az első sor második eleme az az érték legyen,
# ahányszor a kettes számot kihúzták stb.!
# (Annyit biztosan tudunk az értékekről, hogy mindegyikük egyjegyű.)

kihuzasok_szama = []
for i in range(90):
    kihuzasok_szama.append(0)

with open("lotto52.ki", "rt", encoding="utf-8") as file:
    for line in file:
        szamok = line.split(" ")
        for szam in szamok:
            konvertalt_szam = int(szam)
            kihuzasok_szama[konvertalt_szam - 1] += 1

for szam in kihuzasok_szama:
    print(f"{szam} ", end="")
print()

# 9. feladat
# Adja meg, hogy az 1-90 közötti prímszámokból
# melyiket nem húzták ki egyszer sem az elmúlt évben.
# A feladat megoldása során az itt megadott prímszámokat
# felhasználhatja vagy előállíthatja!

primek = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
          31, 37, 41, 43, 47, 53, 59, 61, 67,
          71, 73, 79, 83, 89]

print("A következő prímeket egyszer sem húzták ki:")
for prim in primek:
    if kihuzasok_szama[prim-1] == 0:
        print(prim)
