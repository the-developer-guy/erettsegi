# 1. feladat
# Olvassa be és tárolja el a penztar.txt fájl tartalmát!

baskets = []
with open("penztar.txt", "rt", encoding="utf-8") as file:
    basket = {}
    for line in file:
        item = line.strip()
        if item == "F":
            baskets.append(basket)
            basket = {}
        else:
            if item not in basket:
                basket[item] = 0
            basket[item] += 1


# 2. feladat
# Határozza meg, hogy hányszor fizettek a pénztárnál!

print(f"A fizetések száma: {len(baskets)}")


# 3. feladat
# Írja a képernyőre, hogy az első vásárlónak hány darab árucikk volt a
# kosarában!

item_count = 0
for item in baskets[0]:
    item_count += baskets[0][item]
print(f"Az első vásárló {item_count} darab árucikket vásárolt.")


# 4. feladat
# Kérje be a felhasználótól egy vásárlás sorszámát, egy árucikk nevét és egy
# darabszámot! A következő három feladat megoldásánál ezeket használja fel!

basket_number = int(input("Adja meg egy vásárlás sorszámát! "))
requested_item = input("Adja meg egy árucikk nevét! ")
requested_count = int(input("Adja meg a vásárolt darabszámot! "))

# 5. feladat
# Határozza meg, hogy a bekért árucikkből
# a. melyik vásárláskor vettek először, és melyiknél utoljára!
# b. összesen hány alkalommal vásároltak!

first_purhcase = None
last_purchase = None
purchase_count = 0
for i in range(len(baskets)):
    basket = baskets[i]
    if requested_item in basket:
        if first_purhcase is None:
            first_purhcase = i
        last_purchase = i
        purchase_count += 1

print(f"Az első vásárlás sorszáma: {first_purhcase+1}")
print(f"Az utolsó vásárlás sorszáma: {last_purchase+1}")
print(f"{purchase_count} vásárlás során vettek belőle.")


# 6. feladat
# Határozza meg, hogy a bekért darabszámot vásárolva egy termékből mennyi a
# fizetendő összeg! A feladat megoldásához készítsen függvényt ertek néven,
# amely a darabszámhoz a fizetendő összeget rendeli!

def ertek(darabszam):
    if darabszam == 1:
        return 500
    elif darabszam == 2:
        return 950
    else:
        return 950 + (400 * darabszam-2)


print(f"{requested_count} darab vételekor fizetendő: {ertek(requested_count)}")


# 7. feladat
# Határozza meg, hogy a bekért sorszámú vásárláskor mely árucikkekből és milyen
# mennyiségben vásároltak! Az árucikkek nevét tetszőleges sorrendben
# megjelenítheti.

basket = baskets[basket_number-1]
for item in basket:
    print(f"{basket[item]} {item}")


# 8. feladat
# Készítse el az osszeg.txt fájlt, amelybe soronként az egy-egy vásárlás
# alkalmával fizetendő összeg kerüljön a kimeneti mintának megfelelően!

with open("osszeg.txt", "wt", encoding="utf-8") as file:
    for i in range(len(baskets)):
        basket = baskets[i]
        basket_sum = 0
        for item in basket:
            basket_sum += ertek(basket[item])
        file.write(f"{i+1}: {basket_sum}\n")
