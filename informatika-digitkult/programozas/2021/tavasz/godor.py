# 1. feladat
# Olvassa be és tárolja el a melyseg.txt fájl tartalmát!
# Írja ki a képernyőre, hogy az adatforrás hány adatot tartalmaz!

depths = []
with open("melyseg.txt", "rt", encoding="utf-8") as file:
    for line in file:
        depths.append(int(line))

measurement_count = len(depths)
print(f"Az adatsorban {measurement_count} elem található.")


# 2. feladat
# Olvasson be egy távolságértéket, majd írja a képernyőre, hogy milyen mélyen
# van a gödör alja azon a helyen! Ezt a távolságértéket használja majd
# a 6. feladat megoldása során is!

selected_distance = int(input("Adjon meg egy távolságot: "))

print(f"A bekért helyen {depths[selected_distance-1]}m mély.")


# 3. feladat
# Határozza meg, hogy a felszín hány százaléka maradt érintetlen
# és jelenítse meg 2 tizedes pontossággal!

untouched_surface = 0
for depth in depths:
    if depth == 0:
        untouched_surface += 1

print(f"A felszín {untouched_surface/measurement_count:.2%}-a érintetlen.")


# 4. feladat
# Írja ki a godrok.txt fájlba a gödrök leírását, azaz azokat a számsorokat,
# amelyek egy-egy gödör méterenkénti mélységét adják meg!
# Minden gödör leírása külön sorba kerüljön! 
# Az állomány pontosan a gödrök számával egyező számú sort tartalmazzon!
# A godrok.txt fájl első két sorának tartalma:
# 2 2 2 2 4 4 3 2 2 3 3 4 4 3 2 2
# 2 2 2

pits = []
current_pit = []
pit = False

for depth in depths:
    if depth > 0:
        pit = True
        current_pit.append(depth)
    else:
        if pit:
            pit = False
            pits.append(current_pit)
            current_pit = []

with open("godrok.txt", "wt", encoding="utf-8") as file:
    for pit in pits:
        for depth in pit:
            file.write(f"{depth} ")
        file.write("\n")

# 5. feladat
# Határozza meg a gödrök számát és írja a képernyőre!

print(f"{len(pits)} gödör van.")


# 6. feladat
# Ha a 2. feladatban beolvasott helyen nincs gödör, akkor 
# „Az adott helyen nincs gödör.” üzenetet jelenítse meg

if depths[selected_distance-1] == 0:
    print("Az adott helyen nincs gödör.")

# 6. feladat a)
# ha ott gödör található, akkor határozza meg, hogy mi a gödör kezdő és
# végpontja! A meghatározott értékeket írja a képernyőre!
# (Ha nem tudja meghatározni, használja a további részfeladatoknál a 7 és 22
# értéket, mint a kezdő és a végpont helyét)

if depths[selected_distance-1] > 0:
    pit_start = selected_distance-1
    pit_end = selected_distance-1

    while depths[pit_start] > 0:
        pit_start -= 1
    while depths[pit_end] > 0:
        pit_end += 1
    
    print(f"A gödör {pit_start+1}m-től {pit_end+1}m-ig tart.")


# 6. feladat b)
# a legmélyebb pontja felé mindkét irányból folyamatosan mélyül-e! Azaz a gödör
# az egyik szélétől monoton mélyül egy pontig, és onnantól monoton emelkedik a
# másik széléig. Az eredménytől függően írja ki a képernyőre a „Nem mélyül
# folyamatosan.” vagy a „Folyamatosan mélyül.” mondatot!

if depths[selected_distance-1] > 0:
    deepening = True
    always_deepening = True
    for i in range(pit_start, pit_end):
        if deepening:
            if depths[i] < depths[i+1]:
                deepening = False
        else:
            if depths[i] > depths[i+1]:
                always_deepening = False
                break
    
    if always_deepening:
        print("Folyamatosan mélyül.")
    else:
        print("Nem mélyül folyamatosan.")


# 6. feladat c)
# mekkora a legnagyobb mélysége! A meghatározott értéket írja a képernyőre!

if depths[selected_distance-1] > 0:
    max_depth = depths[pit_start]
    for i in range(pit_start, pit_end+1):
        if depths[i] > max_depth:
            max_depth = depths[i]

    print(f"A gödör {max_depth}m mély a legmélyebb pontján.")


# 6. feladat d)
# mekkora a térfogata, ha szélessége minden helyen 10 méternyi! A meghatározott
# értéket írja a képernyőre!


if depths[selected_distance-1] > 0:
    volume = 0
    for i in range(pit_start, pit_end+1):
        depth = depths[i]
        volume += depth * 10 * 1

    print(f"A gödör térfogata {volume}m³")


# 6. feladat e)
# a félkész csatorna esőben jelentős mennyiségű vizet fogad be. Egy gödör annyi
# vizet képes befogadni anélkül, hogy egy nagyobb szélvihar hatására se öntsön
# ki, amennyi esetén a víz felszíne legalább 1 méter mélyen van a külső
# felszínhez képest. Írja a képernyőre ezt a vízmennyiséget!

if depths[selected_distance-1] > 0:
    compensation = 0
    for i in range(pit_start, pit_end+1):
        if depths[i] > 0:
            compensation += 10
    
    print(f"A gödör legfeljebb {volume-compensation}m³ vizet tud "
          "biztonságosan befogadni.")
