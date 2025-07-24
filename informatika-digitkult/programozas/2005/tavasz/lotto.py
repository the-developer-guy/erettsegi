
# 0. feladat
# Olvaassuk be a lottosz.dat állományt, és tároljuk el a benne lévő adatokat

lottoszamok = []
with open("lottosz.dat", "rt", encoding="utf-8") as file:
    line = file.readline()
    while line != "":
        szamok = line.split(" ")
        feldolgozott_szamok = []
        elemszam = len(szamok)
        i = 0
        while i < elemszam:
            szam = int(szamok[i])
            feldolgozott_szamok.append(szam)
            i += 1
        lottoszamok.append(feldolgozott_szamok)
        line = file.readline()


# 1. feladat
# Kérje be a felhasználótól az 52. hét megadott lottószámait!

bekert_szamok = []
i = 1
while i <= 5:
    szam = int(input(f"Kérem a(z) {i}. lottószámot: "))
    bekert_szamok.append(szam)
    i += 1


# 2. feladat
# A program rendezze a bekért lottószámokat emelkedő sorrendbe!
# A rendezett számokat írja ki a képernyőre!

n = len(bekert_szamok)
i = 0
while i < n - 1:
    minimum_index = i
    j = i + 1
    while j < n:
        if bekert_szamok[j] < bekert_szamok[minimum_index]:
            minimum_index = j
        j += 1

    csere = bekert_szamok[i]
    bekert_szamok[i] = bekert_szamok[minimum_index]
    bekert_szamok[minimum_index] = csere
    i += 1

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
i = 0
while i < 51:
    j = 0
    while j < 5:
        osszes_lottoszam.append(lottoszamok[i][j])
        j += 1
    i += 1

van_kihuzatlan_szam = False
i = 1
while i <= 90:
    szam_megtalalva = False
    j = 0
    while j < len(osszes_lottoszam):
        if i == osszes_lottoszam[j]:
            szam_megtalalva = True
            break
        j += 1
    if szam_megtalalva == False:
        van_kihuzatlan_szam = True
        break
    i += 1

if van_kihuzatlan_szam:
    print("Volt olyan szám, amit egyszer sem húztak ki az első 51 héten")
else:
    print("Minden számot kihúztak az első 51 héten")


# 6. feladat
# A lottosz.dat állományban lévő adatok alapján állapítsa meg,
# hogy hányszor volt páratlan szám a kihúzott lottószámok között!
# Az eredményt a képernyőre írja ki!

paratlan_szamlalo = 0
n = len(lottoszamok)
i = 0
while i < n:
    j = 0
    while j < 5:
        if lottoszamok[i][j] % 2 == 1:
            paratlan_szamlalo += 1
        j += 1
    i += 1

print(f"{paratlan_szamlalo} db. páratlan szám volt az első 51 héten.")


# 7. feladat
# Fűzze hozzá a lottosz.dat állományból beolvasott lottószámok után
# a felhasználótól bekért, és rendezett 52. hét lottószámait,
# majd írja ki az összes lottószámot a lotto52.ki szöveges fájlba!
# A fájlban egy sorba egy hét lottószámai kerüljenek,
# szóközzel elválasztva egymástól!

lottoszamok.append(bekert_szamok)

with open("lotto52.ki", "wt", encoding="utf-8") as file:
    n = len(lottoszamok)
    i = 0
    while i < n:
        file.write(f"{lottoszamok[i][0]} "
                   f"{lottoszamok[i][1]} "
                   f"{lottoszamok[i][2]} "
                   f"{lottoszamok[i][3]} "
                   f"{lottoszamok[i][4]}\n")
        i += 1


# 8. feladat
# Határozza meg a lotto52.ki állomány adatai alapján,
# hogy az egyes számokat hányszor húzták ki 2003-ban.
# Az eredményt írja ki a képernyőre a következő formában:
# az első sor első eleme az a szám legyen ahányszor az egyest kihúzták!
# Az első sor második eleme az az érték legyen,
# ahányszor a kettes számot kihúzták stb.!
# (Annyit biztosan tudunk az értékekről, hogy mindegyikük egyjegyű.)

kihuzasok_szama = []
i = 0
while i < 90:
    kihuzasok_szama.append(0)
    i += 1

with open("lotto52.ki", "rt", encoding="utf-8") as file:
    line = file.readline()
    while line != "":
        szamok = line.split(" ")
        n = len(szamok)
        i = 0
        while i < n:
            konvertalt_szam = int(szamok[i])
            kihuzasok_szama[konvertalt_szam - 1] += 1
            i += 1
        line = file.readline()

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
n = len(primek)
i = 0
while i < n:
    prim = primek[i]
    if kihuzasok_szama[prim-1] == 0:
        print(prim)
    i += 1
