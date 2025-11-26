# 1. feladat
# Olvassa be és tárolja el az autok.txt fájl tartalmát!

DIRECTION_IN = 1
DIRECTION_OUT = 0

events = []
with open("autok.txt", "rt", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split(" ")
        event = {
            "day": int(parts[0]),
            "time": parts[1],
            "plate": parts[2],
            "worker_id": int(parts[3]),
            "km": int(parts[4]),
            "direction": int(parts[5])
        }

        events.append(event)


# 2. feladat
# Adja meg, hogy melyik autót vitték el utoljára a parkolóból!
# Az eredményt a mintának megfelelően írja a képernyőre!

i = len(events) - 1
while i >= 0:
    if events[i]["direction"] == DIRECTION_OUT:
        last_car_out = events[i]
        break
    i -= 1


# 3. feladat
# Kérjen be egy napot és írja ki a képernyőre a minta szerint, hogy mely
# autókat vitték ki és hozták vissza az adott napon!

requested_day = int(input("Óttó: "))
filtered_events = []
for event in events:
    if event["day"] == requested_day:
        filtered_events.append(event)
    if event["day"] > requested_day:
        break


# 4. feladat
# Adja meg, hogy hány autó nem volt bent a hónap végén a parkolóban!

cars = {}
for event in events:
    cars[event["plate"]] = event["direction"]

out_car_count = 0
for plate in cars:
    if cars[plate] == DIRECTION_OUT:
        out_car_count += 1

print(f"A hónap végén {out_car_count} autót nem hoztak vissza.")


# 5. feladat
# Készítsen statisztikát, és írja ki a képernyőre mind a 10 autó esetén az ebben
# a hónapban megtett távolságot kilométerben! A hónap végén még kint lévő autók
# esetén az utolsó rögzített kilométerállással számoljon! A kiírásban az autók
# sorrendje tetszőleges lehet.

odometers = {}
for event in events:
    if event["plate"] not in odometers:
        odometers[event["plate"]] = {
            "min": event["km"],
            "max": event["km"]
        }
    else:
        previous_km = odometers[event["plate"]]
        current_km = event["km"]
        if current_km > previous_km:
            odometers[event["plate"]]["max"] = current_km

for plate in odometers:
    distance = odometers[plate]["max"] - odometers[plate]["min"]
    print(f"{plate} {distance} km")


# 6. feladat
# Határozza meg, melyik személy volt az, aki az autó egy elvitele alatt a
# leghosszabb távolságot tette meg! A személy azonosítóját és a megtett
# kilométert a minta szerint írja a képernyőre!
# (Több legnagyobb érték esetén bármelyiket kiírhatja.)

max_distance = {"km": 0, "id": 0}
rentals = {}
for event in events:
    if event["plate"] not in rentals:
        rentals[event["plate"]] = event["km"]
    
    if event["direction"] == DIRECTION_IN:
        diff = event["km"] - rentals[event["plate"]]
        if diff > max_distance["km"]:
            max_distance = {
                "km": diff,
                "id": event["id"]
            }

print(f"Leghosszabb út: {max_distance["km"]} km, személy: {max_distance["id"]}")


# 7. feladat
# Az autók esetén egy havi menetlevelet kell készíteni! Kérjen be a
# felhasználótól egy rendszámot! Készítsen egy X_menetlevel.txt állományt,
# amelybe elkészíti az adott rendszámú autó menetlevelét!
# (Az X helyére az autó rendszáma kerüljön!) A fájlba soronként tabulátorral
# elválasztva a személy azonosítóját, a kivitel időpontját (nap. óra:perc),
# a kilométerszámláló állását, a visszahozatal időpontját (nap. óra:perc), és
# a kilométerszámláló állását írja a minta szerint!
# (A tabulátor karakter ASCII-kódja: 9.)

requested_plate = input("Rendszám: ")
with open(f"{requested_plate}_menetlevel.txt", "wt", encoding="utf-8") as file:
    for event in events:
        if event["plate"] == requested_plate:
            if event["direction"] == DIRECTION_OUT:
                file.write(f"{event["id"]}\t"
                           f"{event["day"]}.\t"
                           f"{event["time"]}\t"
                           f"{event["km"]} km")
            else:
                file.write(f"\t{event["day"]}.\t"
                           f"{event["time"]}\t"
                           f"{event["km"]} km\n")
