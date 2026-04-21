# A futár az egyes utakra az út hosszától függően kap fizetést az alábbi
# táblázatnak megfelelően:
# 1 – 2 km     500 Ft
# 3 – 5 km     700 Ft
# 6 – 10 km    900 Ft
# 11 – 20 km   1 400 Ft
# 21 – 30 km   2 000 Ft
def ride_price(distance):
    if 1 <= distance <= 2:
        return 500
    elif 3 <= distance <= 5:
        return 700
    elif 6 <= distance <= 10:
        return 900
    elif 11 <= distance <= 20:
        return 1400
    elif 21 <= distance <= 30:
        return 2000


# 1. feladat
# Olvassa be a tavok.txt állományban talált adatokat, s annak felhasználásával
# oldja meg a következő feladatokat!

rides = []
with open("tavok.txt", "rt", encoding="utf-8") as file:
    for line in file:
        parts = line.split()
        ride = {
            "day": int(parts[0]),
            "ride": int(parts[1]),
            "distance": int(parts[2])
        }
        ride["price"] = ride_price(ride["distance"])
        rides.append(ride)


# 2. feladat
# Írja ki a képernyőre, hogy mekkora volt a hét legelső útja kilométerben!
# Figyeljen arra, hogy olyan állomány esetén is helyes értéket adjon, amiben
# például a hét első napján a futár nem dolgozott!

print("2. feladat")
first_ride = rides[0]
for ride in rides:
    if ride["ride"] == 1 and ride["day"] <= first_ride["day"]:
        first_ride = ride

print(f"Az első út {first_ride["distance"]} km hosszú volt.")


# 3. feladat
# Írja ki a képernyőre, hogy mekkora volt a hét utolsó útja kilométerben!

print("3. feladat")
last_ride = rides[0]
for ride in rides:
    if ride["day"] > last_ride["day"]:
        last_ride = ride
    elif ride["day"] == last_ride["day"] and ride["ride"] > last_ride["ride"]:
        last_ride = ride

print(f"Az utolsó út {last_ride["distance"]} km hosszú volt.")


# 4. feladat
# Tudjuk, hogy a futár minden héten tart legalább egy szabadnapot. Írja ki a
# képernyőre, hogy a hét hányadik napjain nem dolgozott a futár!

print("4. feladat")
days_with_ride = set()
for ride in rides:
    days_with_ride.add(ride["day"])

print("A futár a következő napokon nem dolgozott:")
for i in range(1, 8):
    if i not in days_with_ride:
        print(f"- {i}. nap")


# 5. feladat
# Írja ki a képernyőre, hogy a hét melyik napján volt a legtöbb fuvar!
# Amennyiben több nap is azonos, maximális számú fuvar volt, elegendő ezek
# egyikét kiírnia.

print("5. feladat")
ride_counter = [0, 0, 0, 0, 0, 0, 0]
for ride in rides:
    i = ride["day"]-1
    ride_counter[i] += 1

max_ride_index = 0
for i in range(1, 7):
    if ride_counter[i] > ride_counter[max_ride_index]:
        max_ride_index = i

print(f"A(z) {max_ride_index+1}. napon volt a legtöbb fuvar.")


# 6. feladat
# Számítsa ki és írja a képernyőre a mintának megfelelően, hogy az egyes napokon
# hány kilométert kellett tekerni!
# 1. nap: 124 km
# 2. nap: 0 km
# 3. nap: 75 km

print("6. feladat")
ride_distances = [0, 0, 0, 0, 0, 0, 0]
for ride in rides:
    i = ride["day"]-1
    ride_distances[i] += ride["distance"]

for i in range(7):
    print(f"{i+1}. nap: {ride_distances[i]} km")


# 7. feladat
# Kérjen be a felhasználótól egy tetszőleges távolságot, és határozza meg,
# hogy mekkora díjazás jár érte! Ezt írja a képernyőre!

print("7. feladat")
distance = int(input("Adjon meg egy távolságot (egész szám 1-30): "))
print(f"{distance} km-re {ride_price(distance)} Ft-ot kapna a futár.")


# 8. feladat
# Határozza meg az összes rögzített út ellenértékét! Ezeket az értékeket írja ki
# a dijazas.txt állományba nap szerint, azon belül pedig az út sorszáma szerinti
# növekvő sorrendben az alábbi formátumban:
# 1. nap 1. út: 700 Ft
# 1. nap 2. út: 900 Ft
# 1. nap 3. út: 2000 Ft

ride_count = len(rides)
for i in range(ride_count-1):
    min_index = i
    for j in range(i+1, ride_count):
        if rides[j]["day"] < rides[min_index]["day"]:
            min_index = j
        elif rides[j]["day"] == rides[min_index]["day"] and \
            rides[j]["ride"] < rides[min_index]["ride"]:
            min_index = j
    if min_index != i:
        swap = rides[i]
        rides[i] = rides[min_index]
        rides[min_index] = swap

with open("dijazas.txt", "wt", encoding="utf-8") as file:
    for ride in rides:
        file.write(f"{ride.day}. nap {ride.ride}. út: {ride.price} Ft\n")


# 9. feladat
# Határozza meg, és írja ki a képernyőre, hogy a futár mekkora összeget kap a
# heti munkájáért!

print("9. feladat")
full_income = 0
for ride in rides:
    full_income += ride["price"]

print(f"A heti munkájáért {full_income} Ft-ot kap a futár.")
