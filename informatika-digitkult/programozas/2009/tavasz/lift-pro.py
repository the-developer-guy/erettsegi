import random


def get_user_input_success(message: str) -> bool:
    while True:
        user_response = input(message).strip()
        if user_response == "i" or user_response == "I":
            return True
        elif user_response == "n" or user_response == "N":
            return False
        print(f"Érvénytelen válasz: {user_response}\nPróbálja újra")


def get_user_input_int(message: str) -> int:
    while True:
        user_response = input(message)
        try:
            converted_response = int(user_response)
            break
        except ValueError as e:
            print(f"Érvénytelen, nem egész szám: {user_response}")
            print(e)

    return converted_response


# 1. feladat

print("1. feladat")

class ElevatorRequest:

    def __init__(self, hour: str, minute: str, second: str,
                 team: str, start_floor: str, target_floor: str):
        self.time = f"{int(hour):2d}:{int(minute):02d}:{int(second):02d}"
        self.team = int(team)
        self.start_floor = int(start_floor)
        self.target_floor = int(target_floor)


class Requests:

    def __init__(self):
        self.requests_by_team = {}
        self.requests = []

    def add_request(self, req: ElevatorRequest):
        if req.team not in self.requests_by_team:
            self.requests_by_team[req.team] = []
        self.requests_by_team[req.team].append(req)
        self.requests.append(req)

    def get_requests(self, team_id: int):
        try:
            team_requests = self.requests_by_team[team_id]
        except KeyError:
            team_requests = []
        return team_requests

    def min_floor(self):
        first_request = self.requests[0]
        floor = min(first_request.start_floor, first_request.target_floor)
        for request in self.requests:
            current_min_floor = min(request.start_floor, request.target_floor)
            floor = min(floor, current_min_floor)
        return floor
    
    def max_floor(self):
        first_request = self.requests[0]
        floor = max(first_request.start_floor, first_request.target_floor)
        for request in self.requests:
            current_max_floor = max(request.start_floor, request.target_floor)
            floor = max(floor, current_max_floor)
        return floor

    def __getitem__(self, key):
        return self.requests[key]

    def __len__(self):
        return len(self.requests_by_team)

    def __iter__(self):
        return self.__iterate()

    def __iterate(self):
        for request in self.requests:
            yield request
        return


requests = Requests()
with open("igeny.txt", "rt", encoding="utf-8") as file:
    file.readline() # ugorjuk át a nem használt emeletszámot
    team_count = int(file.readline())
    file.readline() # ugorjuk át a hívások számát is
    for line in file:
        parts = line.strip().split(" ")
        request = ElevatorRequest(parts[0], parts[1], parts[2],
                                  parts[3], parts[4], parts[5])
        requests.add_request(request)


# 2. feladat
print("2. feladat")
lift_start_position = get_user_input_int(
    "Adja meg a lift tartózkodási emeletét: ")


# 3. feladat
print("3. feladat")
last_request = requests[-1]
print(f"A lift a {last_request.target_floor}. szinten áll "
      "az utolsó igény teljesítése után.")


# 4. feladat
print("4. feladat")
highest_floor = max(requests.max_floor(), lift_start_position)
lowest_floor = min(requests.min_floor(), lift_start_position)

print(f"A legalacsonyabb szint, amit a lift érintett: {lowest_floor}")
print(f"A legmagasabb szint, amit a lift érintett: {highest_floor}")


# 5. feladat
print("5. feladat")
travel_up_with_passengers_count = 0
travel_up_empty_count = 0
lift_current_position = lift_start_position

for request in requests:
    start_floor = request.start_floor
    target_floor = request.target_floor

    if start_floor > lift_current_position:
        travel_up_empty_count += 1
    if target_floor > start_floor:
        travel_up_with_passengers_count += 1
    lift_current_position = target_floor

print(f"A lift {travel_up_with_passengers_count} alkalommal indult felfelé "
      f"utassal és {travel_up_empty_count} alkalommal utas nélkül.")


# 6. feladat
print("6. feladat")
if len(requests) == team_count:
    print("Minden csapat használta a liftet")
else:
    print("A következő csapatok nem vették igénybe a liftet: ", end="")
    for team_number in range(1, team_count+1):
        if team_number not in requests.requests_by_team:
            print(team_number, end=" ")
    print()


# 7. feladat
print("7. feladat")
generated_team_number = random.randint(1, team_count)
team_requests = requests.get_requests(generated_team_number)

violations = []
for i in range(1, len(team_requests)):
    last_floor = team_requests[i-1].target_floor
    next_floor = team_requests[i].start_floor
    if last_floor != next_floor:
        violations.append((last_floor, next_floor))

if len(violations) == 0:
    print("Nem bizonyítható szabálytalanság")
else:
    print("A következő szintek között szegte meg a szabályokat a "
          f"{generated_team_number}. számú csapat:")
    for violation in violations:
        print(f"- {violation[0]}. és {violation[1]}.")


# 8. feladat
print("8. feladat")
with open("blokkol.txt", "wt", encoding="utf-8") as file:
    for request in team_requests:
        success = get_user_input_success(f"Adja meg, hogy a {request.time}-kor "
                        "befejezett munka sikeres volt-e (i/n): ")
        job_code = get_user_input_int(
            "Adja meg a következő munka kódját (1-99): ")

        file.write(f"Befejezés ideje: {request.time}\n")
        if success:
            file.write("Sikeresség: befejezett\n")
        else:
            file.write("Sikeresség: befejezetlen\n")
        file.write("-----\n"
                   f"Indulási emelet: {request.start_floor}\n"
                   f"Célemelet: {request.target_floor}\n"
                   f"Feladatkód: {job_code}\n")
