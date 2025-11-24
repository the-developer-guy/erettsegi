# 1. feladat
# Olvassa be és tárolja el az ajto.txt fájl tartalmát!

DIRECTION_IN = True
DIRECTION_OUT = False

events = []
with open("ajto.txt", "rt", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split(" ")
        event = {
            "hour": int(parts[0]),
            "minute": int(parts[1]),
            "id": int(parts[2])
        }
        event["timestamp"] = event["hour"] * 60 + event["minute"]
        if parts[3] == "be":
            event["direction"] = DIRECTION_IN
        else:
            event["direction"] = DIRECTION_OUT
        
        events.append(event)


# 2. feladat
# Írja a képernyőre annak a személynek az azonosítóját, aki a vizsgált időszakon
# belül először lépett be az ajtón, és azét, aki utoljára távozott a
# megfigyelési időszakban!

first_in = events[0]
i = len(events) - 1
while i >= 0:
    if events[i]["direction"] == DIRECTION_OUT:
        last_out = events[i]
        break

print(f"Az első belépő: {first_in["id"]}")
print(f"Az utolsó kilépő: {last_out["id"]}")


# 3. feladat
# Határozza meg a fájlban szereplő személyek közül, ki hányszor haladt át a
# társalgó ajtaján! A meghatározott értékeket azonosító szerint növekvő
# sorrendben írja az athaladas.txt fájlba! Soronként egy személy azonosítója,
# és tőle egy szóközzel elválasztva az áthaladások száma szerepeljen!

pass_count = {}
ids = set()
for event in events:
    if event["id"] not in pass_count:
        pass_count[event["id"]] = 1
    else:
        pass_count[event["id"]] += 1

sorted_ids = []
for id in ids:
    sorted_ids.append(id)
sorted_ids.sort()

with open("athaladas.txt", "wt", encoding="utf-8") as file:
    for id in sorted_ids:
        file.print(f"{id} {pass_count[id]}\n")


# 4. feladat
# Írja a képernyőre azon személyek azonosítóját, akik a vizsgált időszak végén
# a társalgóban tartózkodtak!

status = []
for event in events:
    if event["direction"] == DIRECTION_IN:
        status.append(event["id"])
    else:
        status.remove(event["id"])

print("4. feladat")
print("A végén a társalgóban voltak: ", end="")
for id in status:
    print(id, end=" ")
print()


# 5. feladat
# Hányan voltak legtöbben egyszerre a társalgóban? Írjon a képernyőre egy olyan
# időpontot (óra:perc), amikor a legtöbben voltak bent!

max_people_count = 0
current_people_count = 0

for event in events:
    if event["direction"] == DIRECTION_IN:
        current_people_count += 1
        if current_people_count > max_people_count:
            max_hour = event["hour"]
            max_minute = event["minute"]
    else:
        current_people_count -= 1

print("5. feladat")
print(f"Például {max_hour:02d}:{max_minute:02d}-kor voltak a legtöbben a társalgóban.")


# 6. feladat
# Kérje be a felhasználótól egy személy azonosítóját! A további feladatok
# megoldásánál ezt használja fel!

print("6. feladat")
requested_id = int(input("Adja meg a személy azonosítóját! "))


# 7. feladat
# Írja a képernyőre, hogy a beolvasott azonosítóhoz tartozó személy mettől
# meddig tartózkodott a társalgóban!

print("7. feladat")
for event in events:
    if event["id"] == requested_id:
        if event["direction"] == DIRECTION_IN:
            print(f"{event["hour"]:02d}:{event["minute"]:02d}-", end="")
        else:
            print(f"{event["hour"]:02d}:{event["minute"]:02d}")


# 8. feladat
# Határozza meg, hogy a megfigyelt időszakban a beolvasott azonosítójú személy
# összesen hány percet töltött a társalgóban! Az előző feladatban példaként
# szereplő 22-es személy 5 alkalommal járt bent, a megfigyelés végén még bent
# volt. Róla azt tudjuk, hogy 18 percet töltött bent a megfigyelés végéig.
# A 39-es személy 6 alkalommal járt bent, a vizsgált időszak végén nem
# tartózkodott a helyiségben. Róla azt tudjuk, hogy 39 percet töltött ott.
# Írja ki, hogy a beolvasott azonosítójú személy mennyi időt volt a társalgóban,
# és a megfigyelési időszak végén bent volt-e még!

stay_minutes = 0
for event in events:
    if event["id"] == requested_id:
        if event["direction"] == DIRECTION_IN:
            inside = True
            step_in_timestamp = event["timestamp"]
        else:
            inside = False
            stay_minutes += event["timestamp"] - step_in_timestamp

if inside:
    stay_minutes += (15 * 60) - step_in_timestamp
    print(f"A(z) {requested_id}. személy összesen {stay_minutes} percet "
          "volt bent, a megfigyelés végén a társalgóban volt.")
else:
    print(f"A(z) {requested_id}. személy összesen {stay_minutes} percet "
          "volt bent, a megfigyelés végén nem volt a társalgóban.")
