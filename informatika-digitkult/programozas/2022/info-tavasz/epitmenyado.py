# 4. feladat
# Készítsen függvényt ado néven, amely meghatározza egy adott építmény után 
# fizetendő adót! A függvény paraméterlistájában szerepeljen az adósáv és az
# alapterület, visszaadott értéke pedig legyen a fizetendő adó! A következő
# feladatokban ezt a függvényt is felhasználhatja.

def ado(tax_bracket, area):
    base_tax = tax_brackets[tax_bracket]
    tax_amount = base_tax * area
    if tax_amount < 10_000:
        return 0
    return tax_amount


# 1. feladat
# Olvassa be és tárolja el az utca.txt állományban talált adatokat, és annak
# felhasználásával oldja meg a következő feladatokat!

properties = {}
tax_brackets = {}
with open("utca.txt", "rt", encoding="utf-8") as file:
    taxes = file.readline().split(" ")
    tax_brackets["A"] = int(taxes[0])
    tax_brackets["B"] = int(taxes[1])
    tax_brackets["C"] = int(taxes[2])

    for line in file:
        parts = line.strip().split(" ")
        tax_number = parts[0]
        bracket = parts[3]
        size = int(parts[4])
        real_estate = {
            "street": parts[1],
            "number": parts[2],
            "bracket": bracket,
            "size": size,
            "tax": ado(bracket, size)
        }

        if tax_number not in properties:
            properties[tax_number] = []
        properties[tax_number].append(real_estate)


# 2. feladat
# Hány telek adatai találhatók az állományban? Az eredményt írassa ki a mintának
# megfelelően a képernyőre!

property_count = 0
for tax_number in properties:
    property_count += len(properties[tax_number])

print(f"A mintában {property_count} telek szerepel.")


# 3. feladat
# Kérje be egy tulajdonos adószámát, és írassa ki a mintához hasonlóan,
# hogy melyik utcában, milyen házszám alatt van építménye!
# Ha a megadott azonosító nem szerepel az adatállományban, akkor írassa ki a
# „Nem szerepel az adatállományban.” hibaüzenetet!

requested_tax_number = input("Adjon meg egy adószámot: ")
if requested_tax_number not in properties:
    print("Nem szerepel az adatállományban.")
else:
    for real_estate in properties[requested_tax_number]:
        print(f"{real_estate["street"]} {real_estate["number"]}")




# 5. feladat
# Határozza meg, hogy hány építmény esik az egyes adósávokba,
# és mennyi az adó összege adósávonként!
# Az eredményt a mintának megfelelően írassa ki a képernyőre!

properties_by_bracket = {
    "A": [],
    "B": [],
    "C": []
}
for tax_number in properties:
    for real_estate in properties[tax_number]:
        tax_bracket = real_estate["bracket"]
        tax_amount = real_estate["tax"]
        properties_by_bracket[tax_bracket].append(tax_amount)

for bracket in properties_by_bracket:
    tax_sum = 0
    for tax_amount in properties_by_bracket[bracket]:
        tax_sum += tax_amount
    print(f"{bracket} sávba {len(properties_by_bracket[bracket])} telek esik, "
          f"az adó {tax_sum} Ft.")


# 6. feladat
# Bár az utcák többé-kevésbé párhuzamosak a tó partjával, az egyes porták
# távolsága a parttól az utcában nem feltétlenül ugyanannyi. Emiatt néhány
# utcában – az ottani tulajdonosok felháborodására – egyes telkek eltérő sávba
# esnek. Listázza ki a képernyőre, hogy melyek azok az utcák, ahol a telkek 
# sávokba sorolását emiatt felül kell vizsgálni! Feltételezheti, hogy minden
# utcában van legalább két telek.

streets = {}
streets_to_check = []
for tax_number in properties:
    for real_estate in properties[tax_number]:
        street = real_estate["street"]
        if street not in streets:
            streets[street] = []
        streets[street].append(real_estate)

for street in streets:
    initial_tax_bracket = streets[street][0]["bracket"]
    for real_estate in streets[street]:
        if real_estate["bracket"] != initial_tax_bracket:
            streets_to_check.append(street)
            break

print("A több sávba sorolt utcák:")
for street in streets_to_check:
    print(street)


# 7. feladat
# Határozza meg a fizetendő adót tulajdonosonként! A tulajdonos adószámát
# és a fizetendő összeget írassa ki a mintának megfelelően a fizetendo.txt
# állományba! A fájlban minden tulajdonos adatai új sorban szerepeljenek,
# a tulajdonos adószámát egy szóközzel elválasztva kövesse az általa fizetendő
# adó teljes összege.

with open("fizetendo.txt", "wt", encoding="utf-8") as file:
    for tax_number in properties:
        sum_tax = 0
        for real_estate in properties[tax_number]:
            sum_tax += real_estate["tax"]
        file.write(f"{tax_number} {sum_tax}\n")
