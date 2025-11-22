# 1. feladat
# Olvassa be az ip.txt állományban talált adatokat, s annak felhasználásával
# oldja meg a következő feladatokat!

addresses = []
with open("ip.txt", "rt", encoding="utf-8") as file:
    for line in file:
        address = line.strip()
        addresses.append(address)


# 2. feladat
# Határozza meg és írja a képernyőre, hogy hány adatsor van az állományban!

print(f"Az állományban {len(addresses)} darab adatsor van.")


# 3. feladat
# Írja a képernyőre az állományban található legalacsonyabb IP-címet! A
# megoldásában felhasználhatja, hogy a betűk ASCII-kódjai a számok ASCII-kódjai
# után találhatók a kódtáblában.

lowest_address = addresses[0]
for address in addresses:
    if address < lowest_address:
        lowest_address = address
print(f"A legalacsonyabb tárolt IP-cím:\n{lowest_address}")


# 4. feladat
# Határozza meg, hogy az állományban hány darab IP-cím van az egyes fajtákból!
# Az eredményt jelenítse meg a képernyőn a mintának megfelelően!

ADDRESS_TYPE_DOC = "2001:0db8"
ADDRESS_TYPE_GLOBAL = "2001:0e"
ADDRESS_TYPE_LOCAL_FC = "fc"
ADDRESS_TYPE_LOCAL_FD = "fd"

doc_address_count = 0
global_address_count = 0
local_address_count = 0

for address in addresses:
    if address.startswith(ADDRESS_TYPE_DOC):
        doc_address_count += 1
    elif address.startswith(ADDRESS_TYPE_GLOBAL):
        global_address_count += 1
    elif address.startswith(ADDRESS_TYPE_LOCAL_FC) or \
        address.startswith(ADDRESS_TYPE_LOCAL_FD):
        local_address_count += 1

print(f"Dokumentációs cím: {doc_address_count} darab")
print(f"Globális egyedi cím: {global_address_count} darab")
print(f"Helyi egyedi cím: {local_address_count} darab")


# 5. feladat
# Gyűjtse ki a sok.txt állományba azokat az IP-címeket, melyek legalább 18
# nullát tartalmaznak! A fájlban minden sor elején szerepeljen az eredeti
# állományból a cím sorszáma! Ezt kövesse egy szóközzel elválasztva a cím az
# ip.txt állományban szereplő alakjával!

with open("sok.txt", "wt", encoding="utf-8") as destination_file:
    for i in range(len(addresses)):
        zero_count = addresses[i].count("0")
        if zero_count >= 18:
            destination_file.write(f"{i+1} {addresses[i]}\n")


# 6. feladat
# Kérjen be a felhasználótól egy sorszámot! Az állományban a megadott sorszámon
# található IP-címet rövidítse a csoportokon belüli bevezető nullák
# elhagyásával! Az állományban található alakot és a rövidített változatot írja
# a képernyőre egymás alá!

num = int(input("Kérek egy sorszámot: "))
address = addresses[num-1]
print(address)

blocks = address.split(":")
short_blocks = []
for block in blocks:
    block_value = int(block, 16)
    short_blocks.append(f"{block_value:x}")

shorter_address = ""
for i in range(7):
    shorter_address += f"{short_blocks[i]}:"
shorter_address += short_blocks[7]

print(shorter_address)


# 7. feladat
# Az előző feladatban használt IP-címet rövidítse tovább az egymást követő
# nullás csoportok rövidítésére vonatkozó szabályoknak megfelelően! Az eredményt
# jelenítse meg a képernyőn! Amennyiben nem rövidíthető, írja ki:
# Nem rövidíthető tovább.

shorter_blocks = shorter_address.split(":")
zero_block_lenght = 0
zero_block_end_index = 0

longest_zero_block_length = 0
longest_zero_block_end_index = 0
for i in range(8):
    if short_blocks[i] != "0":
        if zero_block_lenght > longest_zero_block_length:
            longest_zero_block_length = zero_block_lenght
            longest_zero_block_end_index = zero_block_end_index
        zero_block_lenght = 0
    else:
        zero_block_lenght += 1
        zero_block_end_index = i

if zero_block_lenght > longest_zero_block_length:
    longest_zero_block_length = zero_block_lenght
    longest_zero_block_end_index = zero_block_end_index

if longest_zero_block_length > 1:
    i = 0
    shortest_address = ""
    while i < 7:
        if i == (longest_zero_block_end_index - longest_zero_block_length + 1):
            i = longest_zero_block_end_index + 1
            shortest_address += ":"
        else:
            shortest_address += f"{shorter_blocks[i]}:"
            i += 1

    shortest_address += shorter_blocks[7]

    print(shortest_address)
else:
    print("Nem rövidíthető tovább.")
