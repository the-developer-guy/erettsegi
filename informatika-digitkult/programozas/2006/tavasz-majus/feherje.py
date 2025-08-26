def get_aminoacid(acids, code):
    for acid in acids:
        if acid["letter"] == code:
            return acid
    return None


# 1. feladat
# Töltse be az aminosav.txt fájlból az aminosavak adatait!
# A fájlban minden adat külön sorban található,
# a fájl az aminosavak nevét nem tartalmazza.

acids = []

with open("aminosav.txt", "rt", encoding="utf-8") as file:
    name = file.readline()
    while name != "":
        letter = file.readline()
        c = file.readline()
        h = file.readline()
        o = file.readline()
        n = file.readline()
        s = file.readline()

        acid = {
            "name": name.strip(),
            "letter": letter.strip(),
            "c": int(c),
            "h": int(h),
            "o": int(o),
            "n": int(n),
            "s": int(s),
        }
        acids.append(acid)
        name = file.readline()


# 2. feladat
# Határozza meg az aminosavak relatív molekulatömegét, ha
# a szén atomtömege 12,
# a hidrogéné 1,
# az oxigéné 16,
# a nitrogéné 14 és
# a kén atomtömege 32!

for acid in acids:
    weight = acid["c"] * 12 \
        + acid["h"] * 1 \
        + acid["o"] * 16 \
        + acid["n"] * 14 \
        + acid["s"] * 32
    acid["weight"] = weight


output = open("eredmeny.txt", "wt", encoding="utf-8")


# 3. feladat
# Rendezze növekvő sorrendbe az aminosavakat a relatív molekulatömeg szerint!
# Írja ki a képernyőre és az eredmeny.txt fájlba
# az aminosavak hárombetűs azonosítóját és a molekulatömeget!
# Az azonosítót és hozzátartozó molekulatömeget
# egy sorba, szóközzel elválasztva írja ki!

n = len(acids)
for i in range(n-1):
    minimum_index = i
    for j in range(i+1, n):
        if acids[j]["weight"] < acids[minimum_index]["weight"]:
            minimum_index = j

    if i != minimum_index:
        csere = acids[i]
        acids[i] = acids[minimum_index]
        acids[minimum_index] = csere

acid_message = ""
for acid in acids:
    acid_message += f"{acid["name"]} {acid["weight"]}\n"
print(acid_message, end="")
output.write(acid_message)


# 4. feladat
# A bsa.txt a BSA nevű fehérje aminosav sorrendjét tartalmazza
# egybetűs jelöléssel.
# Határozza meg a fehérje összegképletét (azaz a C, H, O, N és S számát)!
# A meghatározásánál vegye figyelembe, hogy az
# aminosavak összekapcsolódása során
# minden kapcsolat létrejöttekor egy vízmolekula (H2O) lép ki!
# Amennyiben a bsa.txt beolvasása sikertelen,
# helyette tárolja a G,A,R,F,C betűjeleket tízszer egymás után
# és a feladatokat erre a „láncra” oldja meg!

bsa = "GARFCGARFCGARFCGARFCGARFCGARFCGARFCGARFCGARFCGARFC" 

bsa = ""
with open("bsa.txt", "rt", encoding="utf-8") as file:
    for line in file:
        acid = line.strip()
        bsa += acid

c = 0
h = 0
o = 0
n = 0
s = 0
for acid in bsa:
    current_acid = get_aminoacid(acids, acid)
    c += current_acid["c"]
    h += current_acid["h"]
    o += current_acid["o"]
    n += current_acid["n"]
    s += current_acid["s"]

h -= (len(bsa) - 1) * 2
o -= len(bsa) - 1

formula = f"C {c} H {h} O {o} N {n} S {s}\n"
print(formula, end="")
output.write(formula)


# 5. feladat
# Határozza meg, és írja ki képernyőre a Kimotripszin enzimmel széthasított
# BSA lánc leghosszabb darabjának hosszát
# és az eredeti láncban elfoglalt helyét
# (első és utolsó aminosavának sorszámát)!
# A kiíráskor nevezze meg a kiírt adatot, például: „kezdet helye:”!

chains = []
current_chain = {"start": 0, "chain": ""}
for i, acid in enumerate(bsa):
    current_chain["chain"] += acid
    if acid == "Y" or acid == "W" or acid == "F":
        chains.append(current_chain)
        current_chain = {"start": i+1, "chain": ""}
chains.append(current_chain)

max_i = 0
max_len = 0
for i, chain in enumerate(chains):
    length = len(chain["chain"])
    if length > max_len:
        max_len = length
        max_i = i

longest_chain = chains[max_i]
longest_chain_length = len(longest_chain["chain"])
longest_chain_start = longest_chain["start"]+1
longest_chain_end = longest_chain_start + longest_chain_length
chain_message = f"leghosszabb lánc hossza: {longest_chain_length}, " \
    f"első aminosavának sorszáma: {longest_chain_start}, " \
    f"utolsó aminosavának sorszáma: {longest_chain_end}\n"

print(chain_message, end="")
output.write(chain_message)


# 6. feladat
# Egy másik enzim (a Factor XI) az Arginin (R) után hasít,
# de csak akkor, ha Alinin (A) vagy Valin (V) követi.
# Határozza meg, hogy a hasítás során keletkező első fehérjelánc részletben
# hány Cisztein (C) található!

# Kétszer bejárva

count_index = len(bsa)
for i in range(len(bsa)-1):
    slice = bsa[i:i+2]
    if slice == "RA" or slice == "RV":
        count_index = i
        break

c_count = 0
for i in range(count_index):
    if bsa[i] == "C":
        c_count += 1

c_count_message = f"A Factor XI-s hasítás után az első láncban {c_count} " \
     "Cisztein található.\n"
print(c_count_message, end="")
output.write(c_count_message)

# Egybegyúrva

c_count = 0
last_acid_r = False
for acid in bsa:

    if last_acid_r == True:
        if acid == "A" or acid == "V":
            break

    if acid == "R":
        last_acid_r = True
    else:
        last_acid_r = False

    if acid == "C":
        c_count += 1

c_count_message = f"A Factor XI-s hasítás után az első láncban {c_count} " \
     "Cisztein található.\n"
print(c_count_message, end="")
output.write(c_count_message)


# Kötelező fájlbezárás

output.flush()
output.close()
