# 1. feladat
# Olvassa be a kep.txt állomány tartalmát,
# és tárolja el a 640×360 képpont színét!

image = []
with open("kep.txt", "rt", encoding="utf-8") as file:
    for line in file:
        row_pixels = []
        parts = line.strip().split(" ")
        row_pixel_count = len(parts) // 3
        for i in range(row_pixel_count):
            red = i*3 + 0
            green = i*3 + 1
            blue = i*3 + 2
            pixel = {
                "r": red,
                "g": green,
                "b": blue,
                "lum": red + green + blue
            }
            row_pixels.append(pixel)
        image.append(row_pixels)        


# 2. feladat
# Kérje be a felhasználótól a kép egy pontjának sor- és oszlopszámát
# (a számozás mindkét esetben 1-től indul), és írja a képernyőre
# az adott képpont RGB színösszetevőit a minta szerint!

row = int(input("Adjon meg egy sorszámot: "))
column = int(input("Adjon meg egy oszlopszámot: "))

pixel = image[row-1][column-1]
print(f"A képpont színe RGB({pixel["r"]},{pixel["g"]},{pixel["b"]})")


# 3. feladat
# Világosnak tekintjük az olyan képpontot, amely RGB-értékeinek összege
# 600-nál nagyobb.
# Számolja meg és írja ki, hogy a teljes képen hány világos képpont van!

brigth_pixel_count = 0
for row in image:
    for pixel in row:
        if pixel["lum"] > 600:
            brigth_pixel_count += 1

print(f"A világos képpontok száma: {brigth_pixel_count}")


# 4. feladat
# A kép legsötétebb pontjainak azokat a pontokat tekintjük, amelyek
# RGB-értékeinek összege a legkisebb. Adja meg, hogy mennyi a legkisebb összeg,
# illetve keresse meg az ilyen RGB összegű pixeleket,
# és írja ki mindegyik színét RGB(r,g,b) formában a mintának megfelelően!

darkest_pixel = image[0][0]
darkest_pixels = []
for row in image:
    for pixel in row:
        if pixel["lum"] < darkest_pixel["lum"]:
            darkest_pixel = pixel
            darkest_pixels = [pixel]
        elif pixel["lum"] == darkest_pixel["lum"]:
            darkest_pixels.append(pixel)

print("A legsötétebb pixelek színe:")
for pixel in darkest_pixels:
    print(f"RGB({pixel["r"]},{pixel["g"]},{pixel["b"]})")


# 5. feladat
# A képen a kék ég látható közepén egy felhővel. Az ég és a felhő színe között
# jelentős különbség van, így az ég-felhő határvonal programmal is felismerhető.
# Ennek megtalálásához készítsen függvényt hatar néven, amely megadja, hogy egy
# adott sorban van-e olyan hely a képen, ahol az egymás melletti képpontok kék
# színösszetevőinek eltérése meghalad egy adott értéket! A függvény kapja meg
# paraméterként a sor számát, illetve az eltérés értékét, melyek egészek!
# A függvény visszatérési értéke egy logikai érték legyen, amely megadja, hogy
# az adott sorban volt-e az eltérést meghaladó különbség
# az egymás melletti képpontok kék színében!

def blue_change_detected(row, treshold):
    selected_row = image[row-1]
    pixel_count = len(selected_row)
    for i in range(1, pixel_count):
        change = selected_row[i-1]["b"] - selected_row[i]["b"]
        if change < 0:
            change *= -1
        if change > treshold:
            return True

    return False


# 6. feladat
# Keresse meg a képen a felhő első és utolsó sorát az előzőleg elkészített
# függvény segítségével úgy, hogy eltérésként 10-et ad meg a függvénynek
# bemenetként! Adja meg az első és az utolsó olyan sor sorszámát, ahol az
# eltérés a soron belül valahol 10-nél nagyobb!

for row in range(len(image)):
    if blue_change_detected(row, 10):
        print(f"A felhő legfelső sora: {i+1}")
        break

row = len(image)-1
while row >= 0:
    if blue_change_detected(row, 10):
        print(f"A felhő legalsó sora: {i+1}")
        break
    row -= 1
