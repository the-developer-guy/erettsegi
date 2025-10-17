# E-Learning: https://elearning.tdg.hu/2006-majus/
# Teljes megoldás: https://youtu.be/1H4R57p79dI

def double_print(message, filename="eredmeny.txt"):
    with open(filename, "at", encoding="utf-8") as file:
        file.write(message)
        file.write("\n")
    print(message)


HYDROGEN_WEIGHT = 1
CARBON_WEIGHT = 12
NITROGEN_WEIGHT = 14
OXYGEN_WEIGHT = 16
SULPHUR_WEIGHT = 32


# 1. és 2. feladat
# https://youtu.be/tLY9zLfy-Ic
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

        weight = acid["c"] * CARBON_WEIGHT \
        + acid["h"] * HYDROGEN_WEIGHT \
        + acid["o"] * OXYGEN_WEIGHT \
        + acid["n"] * NITROGEN_WEIGHT \
        + acid["s"] * SULPHUR_WEIGHT
        acid["weight"] = weight

        acids.append(acid)
        name = file.readline()


# 2,5. feladat
# https://youtu.be/5_35-6L08yE


# 3. feladat
# https://youtu.be/R1e-qIsWv5s
sorted_acids = sorted(acids, key=lambda acid: acid["weight"])
acid_message = "3. feladat:\n"
for acid in sorted_acids:
    acid_message += f"{acid["name"]} {acid["weight"]} "
double_print(acid_message)


# 4. feladat
# https://youtu.be/9hVqAjh_7H0
bsa = "GARFC" * 10

bsa = ""
with open("bsa.txt", "rt", encoding="utf-8") as file:
    for line in file:
        acid = line.strip()
        bsa += acid

acid_table = {}
for acid in acids:
    acid_table[acid["letter"]] = acid

acid_table = {acid["letter"]: acid for acid in acids}

c = 0
h = 0
o = 0
n = 0
s = 0
for letter in bsa:
    current_acid = acid_table[letter]
    c += current_acid["c"]
    h += current_acid["h"]
    o += current_acid["o"]
    n += current_acid["n"]
    s += current_acid["s"]

connection_count = len(bsa) - 1
h -= connection_count * 2
o -= connection_count

double_print(f"4. feladat:\nC {c} H {h} O {o} N {n} S {s}")


# 5. feladat
chains = []
current_chain = {"start": 0, "chain": ""}
i = 0
for acid in bsa:
    current_chain["chain"] += acid
    if acid == "Y" or acid == "W" or acid == "F":
        chains.append(current_chain)
        current_chain = {"start": i+1, "chain": ""}
    i += 1
chains.append(current_chain)

max_i = 0
max_len = 0
for i in range(len(chains)):
    chain = chains[i]
    length = len(chain["chain"])
    if length > max_len:
        max_len = length
        max_i = i

longest_chain = chains[max_i]
longest_chain_length = len(longest_chain["chain"])
longest_chain_start = longest_chain["start"]+1
longest_chain_end = longest_chain_start + longest_chain_length

double_print("5. feladat\n"
    f"leghosszabb lánc hossza: {longest_chain_length}, "
    f"első aminosavának sorszáma: {longest_chain_start}, "
    f"utolsó aminosavának sorszáma: {longest_chain_end}")


# 6. feladat
# https://youtu.be/0t1zgeupui4
ra_index = bsa.find("RA")
rv_index = bsa.find("RV")

if ra_index == -1 and rv_index == -1:
    chain = bsa
elif ra_index == -1:
    chain = bsa[:rv_index]
elif rv_index == -1:
    chain = bsa[:ra_index]
else:
    chain = bsa[:min(ra_index, rv_index)]

c_count = chain.count("C")
double_print(f"A Factor XI-s hasítás után az első láncban {c_count} "
     "Cisztein található.")
