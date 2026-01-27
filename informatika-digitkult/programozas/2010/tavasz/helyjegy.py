# 1. feladat
# Olvassa be az eladott.txt állományban talált adatokat, s azok felhasználásával
# oldja meg a következő feladatokat!

passengers = []
with open("eladott.txt", "rt", encoding="utf-8") as file:
    travel_info = file.readline().split(" ")
    sold_ticket_count = int(travel_info[0])
    ride_length = int(travel_info[1])
    fare = int(travel_info[2])
    ticket_id = 1
    for line in file:
        ticket_parts = line.split(" ")
        passenger = {
            "id": ticket_id,
            "seat": int(ticket_parts[0]),
            "board": int(ticket_parts[1]),
            "alight": int(ticket_parts[2]),
            "price": 0
        }
        passengers.append(passenger)
        ticket_id += 1

# 2. feladat
# Adja meg a legutolsó jegyvásárló ülésének sorszámát és az általa beutazott
# távolságot! A kívánt adatokat a képernyőn jelenítse meg!

last_passenger = passengers[-1]
print(f"Az utolsó jegyvásárló a(z) {last_passenger["seat"]}. számú ülésen "
      f"utazott, és {last_passenger["alight"]-last_passenger["board"]} "
      "kilométert tett meg.")


# 3. feladat
# Listázza ki, kik utazták végig a teljes utat!
# Az utasok sorszámát egy-egy szóközzel elválasztva írja a képernyőre!

long_traveling_passengers = []
for passenger in passengers:
    if passenger["board"] == 0 and passenger["alight"] == ride_length:
        long_traveling_passengers.append(passenger)
if len(long_traveling_passengers) == 0:
    print("Egy utas sem utazta végig az utat.")
else:
    print("A következő utasok utaztak végig:")
    for i in range(len(long_traveling_passengers)-1):
        print(f"{long_traveling_passengers[i]["id"]}", end=" ")
    print(f"{long_traveling_passengers[len(long_traveling_passengers)-1]["id"]}")


# 4. feladat
# Határozza meg, hogy a jegyekből mennyi bevétele származott a társaságnak!
# Az eredményt írja a képernyőre!

income = 0
for passenger in passengers:
    income += passenger["price"]
print(f"A társaságnak {income} Ft bevétele származott.")


# 5. feladat
# Írja a képernyőre, hogy a busz végállomást megelőző utolsó megállásánál
# hányan szálltak fel és le!

stops = set()
for passenger in passengers:
    stops.add(passenger["board"])
    stops.add(passenger["alight"])
sorted_stops = list(stops)
sorted_stops.sort()


# 6. feladat
# Adja meg, hogy hány helyen állt meg a busz a kiinduló állomás és a
# célállomás között! Az eredményt írja a képernyőre!

print(f"A busz {len(stops)-2} helyen állt meg.")


# 7. feladat
# Készítsen „utaslistát” az út egy pontjáról! A listában ülésenként tüntesse
# fel, hogy azt az adott pillanatban melyik utas foglalja el! A pontot, azaz a
# kiindulási állomástól mért távolságot, a felhasználótól kérje be! Ha a
# beolvasott helyen éppen megálló lett volna, akkor a felszálló utasokat vegye
# figyelembe, a leszállókat pedig hagyja figyelmen kívül!
# Az eredményt az ülések sorszámának sorrendjében írja a kihol.txt állományba!
# Az üres helyek esetén az „üres” szót jelenítse meg!
# Minden ülés külön sorba kerüljön!

list_distance = int(input("Adja meg az utaslistához szükséges távot: "))
occupied_seats = {}
for passenger in passengers:
    if passenger["board"] <= list_distance and \
        passenger["alight"] > list_distance:
        occupied_seats[passenger["seat"]] = passenger["id"]

with open("kihol.txt", "wt", encoding="utf-8") as file:
    for i in range(1, 49):
        if i in occupied_seats:
            file.write(f"{i}. ülés: {occupied_seats[i]}. utas\n")
        else:
            file.write(f"{i}. ülés: üres")
