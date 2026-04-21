import random

# 1. feladat
# Olvassa be az igeny.txt állományban talált adatokat,
# s azok felhasználásával oldja meg a következő feladatokat!

print("1. feladat")
requests = []
with open("igeny.txt", "rt", encoding="utf-8") as file:
    floor_count = int(file.readline())
    team_count = int(file.readline())
    request_count = int(file.readline())
    for i in range(request_count):
        line = file.readline()
        parts = line.strip().split(" ")
        request = {
            "hour": int(parts[0]),
            "minute": int(parts[1]),
            "second": int(parts[2]),
            "team": int(parts[3]),
            "start_floor": int(parts[4]),
            "target_floor": int(parts[5])
        }
        requests.append(request)


# 2. feladat
# Tudjuk, hogy a megfigyelés kezdetén a lift éppen áll.
# Kérje be a felhasználótól, hogy melyik szinten áll a lift,
# és a további részfeladatok megoldásánál ezt vegye figyelembe!

print("2. feladat")
lift_start_position = int(input("Adja meg a lift kiindulási emeletét: "))


# 3. feladat
# Határozza meg, hogy melyik szinten áll majd a lift
# az utolsó kérés teljesítését követően!

print("3. feladat")
last_request = requests[len(requests)-1]
print(f"A lift a {last_request["target_floor"]}. szinten áll "
      "az utolsó igény teljesítése után.")


# 4. feladat
# Írja a képernyőre, hogy a megfigyelés kezdete és az utolsó igény teljesítése
# között melyik volt a legalacsonyabb
# és melyik a legmagasabb sorszámú szint, amelyet a lift érintett!

print("4. feladat")
highest_floor = lift_start_position
lowest_floor = lift_start_position
for request in requests:
    if request["start_floor"] > highest_floor:
        highest_floor = request["start_floor"]
    if request["target_floor"] > highest_floor:
        highest_floor = request["target_floor"]

    if request["start_floor"] < lowest_floor:
        lowest_floor = request["start_floor"]
    if request["target_floor"] < lowest_floor:
        lowest_floor = request["target_floor"]

print(f"A legalacsonyabb szint, amit a lift érintett: {lowest_floor}")
print(f"A legmagasabb szint, amit a lift érintett: {highest_floor}")


# 5. feladat
# Határozza meg, hogy hányszor kellett a liftnek felfelé indulnia utassal
# és hányszor utas nélkül!
# Az eredményt jelenítse meg a képernyőn!

print("5. feladat")
travel_up_with_passengers_count = 0
travel_up_empty_count = 0
lift_current_position = lift_start_position
for request in requests:
    if request["start_floor"] > lift_current_position:
        travel_up_empty_count += 1
    if request["target_floor"] > request["start_floor"]:
        travel_up_with_passengers_count += 1
    lift_current_position = request["target_floor"]

print(f"A lift {travel_up_with_passengers_count} alkalommal indult felfelé "
      f"utassal és {travel_up_empty_count} alkalommal utas nélkül.")


# 6. feladat
# Határozza meg, hogy mely szerelőcsapatok nem vették igénybe a liftet
# a vizsgált intervallumban!
# A szerelőcsapatok sorszámát egymástól egy-egy szóközzel elválasztva
# írja a képernyőre!

print("6. feladat")
travelled_teams = set()
for request in requests:
    travelled_teams.add(request["team"])
if len(travelled_teams) == team_count:
    print("Minden csapat használta a liftet")
else:
    print("A következő csapatok nem vették igénybe a liftet: ", end="")
    for team_number in range(1, team_count+1):
        if team_number not in travelled_teams:
            print(team_number, end=" ")
    print()


# 7. feladat
# Előfordul, hogy egyik vagy másik szerelőcsapat áthágja a szabályokat,
# és egyik szintről gyalog megy a másikra.
# (Ezt onnan tudhatjuk, hogy más emeleten igényli a liftet, mint ahova
# korábban érkezett.)
# Generáljon véletlenszerűen egy létező csapatsorszámot!
# Határozza meg, hogy a vizsgált időszak igényei alapján lehet-e egyértelműen
# bizonyítani, hogy ez a csapat vétett a szabályok ellen!
# Ha igen, akkor adja meg, hogy melyik két szint közötti utat tették meg
# gyalog, ellenkező esetben írja ki a
# Nem bizonyítható szabálytalanság szöveget!

print("7. feladat")
generated_team_number = random.randint(1, team_count)
team_requests = []
for request in requests:
    if request["team"] == generated_team_number:
        team_requests.append(request)

violations = []
for i in range(1, len(team_requests)):
    last_floor = team_requests[i-1]["target_floor"]
    current_floor = team_requests[i]["start_floor"]
    if last_floor != current_floor:
        violations.append((last_floor, current_floor))

if len(violations) == 0:
    print("Nem bizonyítható szabálytalanság")
else:
    print("A következő szintek között szegte meg a szabályokat a "
          f"{generated_team_number}. számú csapat:")
    for violation in violations:
        print(f"- {violation[0]}. és {violation[1]}.")


# 8. feladat
# A munkák elvégzésének adminisztrálásához minden csapatnak egy blokkolókártyát
# kell használnia. A kártyára a liftben elhelyezett blokkolóóra rögzíti az
# emeletet, az időpontot. Ennek a készüléknek a segítségével kell megadni a
# munka kódszámát és az adott munkafolyamat sikerességét.
# A munka kódja 1 és 99 közötti egész szám lehet. A sikerességet
# a „befejezett” és a „befejezetlen” szavakkal lehet jelezni.
# Egy műszaki hiba folytán az előző feladatban vizsgált csapat kártyájára az
# általunk nyomon követett időszakban nem került bejegyzés. Ezért a
# csapatfőnöknek a műszak végén pótolnia kell a hiányzó adatokat. Az igeny.txt
# állomány adatait felhasználva írja a képernyőre időrendben, hogy a vizsgált
# időszakban milyen kérdéseket tett fel az óra, és kérje be az adott válaszokat
# a felhasználótól! A pótlólag feljegyzett adatokat írja a blokkol.txt
# állományba! A blokkol.txt állomány tartalmát az alábbi sorok mintájára
# alakítsa ki:
# Befejezés ideje: 9:23:11
# Sikeresség: befejezett
# -----
# Indulási emelet: 9
# Célemelet: 11
# Feladatkód: 23
# Befejezés ideje: 10:43:22
# Sikeresség: befejezetlen
# -----
# Indulási emelet: 11
# Célemelet: 6
# Feladatkód: 6

print("8. feladat")
with open("blokkol.txt", "wt", encoding="utf-8") as file:
    for request in team_requests:
        h = request["hour"]
        m = request["minute"]
        s = request["second"]
        success = input(f"Adja meg, hogy a {h}:{m:02}:{s:02}-kor befejezett "
                        "munka sikeres volt-e (i/n): ")
        job_code = int(input("Adja meg a következő munka kódját (1-99): "))

        file.write(f"Befejezés ideje: {h}:{m:02}:{s:02}\n")
        if success == "i":
            file.write("Sikeresség: befejezett\n-----\n")
        else:
            file.write("Sikeresség: befejezetlen\n-----\n")
        file.write(f"Indulási emelet: {request["start_floor"]}\n"
                   f"Célemelet: {request["target_floor"]}\n"
                   f"Feladatkód: {job_code}\n")
