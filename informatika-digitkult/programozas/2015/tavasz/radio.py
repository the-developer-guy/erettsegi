# 1. feladat
# Olvassa be és tárolja a veetel.txt fájl tartalmát!

messages = []
daily_messages = []
for i in range(11):
    daily_messages.append( [] )

with open("veetel.txt", "rt", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split(" ")
        message_stub = file.readline().strip()
        day = int(parts[0])

        message = {
            "day": day,
            "ham": parts[1],
            "stub": message_stub
        }

        daily_messages[day].append(message_stub)


# 2. feladat
# Írja a képernyőre, hogy melyik rádióamatőr rögzítette az állományban szereplő
# első és melyik az utolsó üzenetet!

print(f"Az első üzenet rögzítője: {messages[0]["ham"]}")
print(f"Az utolsó üzenet rögzítője: {messages[-1]["ham"]}")


# 3. feladat
# Adja meg az összes olyan feljegyzés napját és a rádióamatőr sorszámát,
# amelynek szövegében a „farkas” karaktersorozat szerepel!

for message in messages:
    if "farkas" in message["stub"]:
        print(f"{message["day"]}. nap {message["ham"]}. rádióamatőr")


# 4. feladat
# Készítsen statisztikát, amely megadja, hogy melyik napon hány rádióamatőr
# készített feljegyzést. Azok a napok 0 értékkel szerepeljenek, amikor nem
# született feljegyzés! Az eredmény a képernyőn jelenjen meg a napok sorszáma
# szerint növekvően! A megjelenítést a feladat végén látható minta szerint
# alakítsa ki!

ham_statistics = []
for i in range(11):
    ham_statistics.append(0)

for message in messages:
    day = message["day"]
    ham_statistics[day-1] += 1

for day in range(11):
    print(f"{day+1}. nap: {ham_statistics[day]} rádióamatőr")


# 5. feladat
# A rögzített üzenetek alapján kísérelje meg helyreállítani az expedíció által
# küldött üzenetet! Készítse el az adaas.txt fájlt, amely napok szerinti
# sorrendben tartalmazza a küldött üzeneteket! Ha egy időpontban senkinél nem
# volt vétel, akkor azon a ponton a # jel szerepeljen! (Feltételezheti, hogy az
# azonos üzenethez tartozó feljegyzések között nincs ellentmondás.)
# Az alábbi minta az első napról tartalmaz három üzenetet:
#    1 13
#    #abor# #e#tun###agy#szel#2# #o##h#d#g ##rkasn#o#oka# #a#tunk
#    e####a#akn##$#$#$##$$$$$$####
#    1 19
#    ta###t##ertunk ##gy #zel#####ok hide##f#r##sn#omo#at ##ttu##
#    e#y patak#al$#$$$$$###$$$$$$$
#    1 9
#    ta#o#t#v##tu#k nag# #zel#20 fok#hi##g fa#k#snyo#okat la#tun#
#    #e#y#pat##na#$$###$$#$#$$$$$$$
# A helyreállított üzenet:
#    tabort vertunk nagy szel#20 fok hideg farkasnyomokat lattunk
#    e#y pataknal$$$$$$$$$$$$$$$$$

recovered_messages = []
for day in range(11):
    recovered_message = daily_messages[day][0]
    for message in daily_messages[day]:
        stub = ""
        for i in range(len(message)):
            if recovered_message[i] == "#":
                stub += message[i]
            else:
                stub += recovered_message[i]
        recovered_message = stub

    recovered_messages.append(recovered_message)

with open("adaas.txt", "wt", encoding="utf-8") as file:
      for message in recovered_messages:
          file.write(f"{message}\n")


# 6. feladat
# Készítsen függvényt szame néven az alábbi algoritmus alapján! A függvény egy
# karaktersorozathoz hozzárendeli az igaz vagy a hamis értéket. A függvény
# elkészítésekor az algoritmusban megadott változóneveket használja! Az
# elkészített függvényt a következő feladat megoldásánál felhasználhatja.
# 
# Függvény szame(szo:karaktersorozat): logikai
#   valasz:=igaz
#   Ciklus i:=1-től hossz(szo)-ig
#       ha szo[i]<'0' vagy szo[i]>'9' akkor valasz:=hamis
#   Ciklus vége
#   szame:=valasz
# Függvény vége

def szame(szo):
    valasz = True
    for i in range(len(szo)):
        if szo[i] < "0" or szo[i] > "9":
            valasz = False
    
    return valasz


# 7. feladat
# Olvassa be egy nap és egy rádióamatőr sorszámát, majd írja a képernyőre a
# megfigyelt egyedek számát (a kifejlett és kölyök egyedek számának összegét)!
# Ha nem volt ilyen feljegyzés, a „Nincs ilyen feljegyzés” szöveget jelenítse
# meg! Ha nem volt megfigyelt egyed vagy számuk nem állapítható meg, a
# „Nincs információ” szöveget jelenítse meg! Amennyiben egy számot
# közvetlenül # jel követ, akkor a számot tekintse nem megállapíthatónak!

requested_day = int(input("Adja meg a nap sorszámát! "))
requested_ham = input("Adja meg a rádióamatőr sorszámát! ")

requested_message = None
for message in messages:
    if message["day"] == requested_day and message["ham"] == requested_ham:
        requested_message = message
        break

if requested_message is None:
    print("Nincs ilyen feljegyzés")
else:
    parts = requested_message["stub"].split(" ")
    numbers = parts[0].split("/")
    if len(numbers) != 2:
        print("Nincs információ")
    elif not szame(numbers[0]) or not szame(numbers[1]):
        print("Nincs információ")
    else:
        wolf_count = int(numbers[0]) + int(numbers[1])
        print(f"A megfigyelt egyedek száma: {wolf_count}")
