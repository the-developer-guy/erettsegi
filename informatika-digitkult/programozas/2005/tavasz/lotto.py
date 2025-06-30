
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

    bekert_szamok[i], bekert_szamok[minimum_index] = bekert_szamok[minimum_index], bekert_szamok[i]

print("A rendezett lottószámok: "
      f"{bekert_szamok[0]}, "
      f"{bekert_szamok[1]}, "
      f"{bekert_szamok[2]}, "
      f"{bekert_szamok[3]}, "
      f"{bekert_szamok[4]}")

# 3. feladat
# Kérjen be a felhasználótól egy egész számot 1-51 között! A bekért adatot nem kell ellenőrizni!

bekert_het = int(input("Kérem adja meg a hét számát (1-52): "))

# 4. feladat
# Írja ki a képernyőre a bekért számnak megfelelő sorszámú hét lottószámait a lottosz.dat állományban lévő adatok alapján!

lottoszamok.append(bekert_szamok)

print(f"A(z) {bekert_het}. hét lottószámai: "
      f"{lottoszamok[bekert_het - 1][0]}, "
      f"{lottoszamok[bekert_het - 1][1]}, "
      f"{lottoszamok[bekert_het - 1][2]}, "
      f"{lottoszamok[bekert_het - 1][3]}, "
      f"{lottoszamok[bekert_het - 1][4]}")