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

print("2. feladat:")
print(f"Az állományban {len(addresses)} darab adatsor van.")


# 3. feladat
# Írja a képernyőre az állományban található legalacsonyabb IP-címet! A
# megoldásában felhasználhatja, hogy a betűk ASCII-kódjai a számok ASCII-kódjai
# után találhatók a kódtáblában.

print("3. feladat:")
lowest_address = addresses[0]
for address in addresses:
    if address < lowest_address:
        lowest_address = address
print(f"A legalacsonyabb tárolt IP-cím:\n{lowest_address}")


# 4. feladat
# Határozza meg, hogy az állományban hány darab IP-cím van az egyes fajtákból!
# Az eredményt jelenítse meg a képernyőn a mintának megfelelően!

print("4. feladat:")
ADDRESS_TYPE_DOC = "2001:0db8"
ADDRESS_TYPE_GLOBAL = "2001:0e"
ADDRESS_TYPE_LOCAL_FC = "fc"
ADDRESS_TYPE_LOCAL_FD = "fd"

documentation_address_count = 0
global_address_count = 0
local_address_count = 0

for address in addresses:
    if address[0:9] == ADDRESS_TYPE_DOC:
        documentation_address_count += 1
    elif address[0:7] == ADDRESS_TYPE_GLOBAL:
        global_address_count += 1
    elif address[0:2] == ADDRESS_TYPE_LOCAL_FC or \
        address[0:2] == ADDRESS_TYPE_LOCAL_FD:
        local_address_count += 1

print(f"Dokumentációs cím: {documentation_address_count} darab")
print(f"Globális egyedi cím: {global_address_count} darab")
print(f"Helyi egyedi cím: {local_address_count} darab")


# 5. feladat
# Gyűjtse ki a sok.txt állományba azokat az IP-címeket, melyek legalább 18
# nullát tartalmaznak! A fájlban minden sor elején szerepeljen az eredeti
# állományból a cím sorszáma! Ezt kövesse egy szóközzel elválasztva a cím az
# ip.txt állományban szereplő alakjával!

with open("sok.txt", "wt", encoding="utf-8") as destination_file:
    for i in range(len(addresses)):
        zero_count = 0
        for c in addresses[i]:
            if c == "0":
                zero_count += 1
        if zero_count >= 18:
            destination_file.write(f"{i+1} {addresses[i]}\n")


# 6. feladat
# Kérjen be a felhasználótól egy sorszámot! Az állományban a megadott sorszámon
# található IP-címet rövidítse a csoportokon belüli bevezető nullák
# elhagyásával! Az állományban található alakot és a rövidített változatot írja
# a képernyőre egymás alá!

print("6. feladat:")
num = int(input("Kérek egy sorszámot: "))
address = addresses[num-1]
print(address)

blocks = address.split(":")
short_blocks = []
for block in blocks:
    current_block = ""
    for i in range(4):
        if block[i] == "0":
            continue
        break
    while i < 4:
        current_block += block[i]
        i += 1
    short_blocks.append(current_block)

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

print("7. feladat:")
shorter_blocks = shorter_address.split(":")
zero_block_lenght = 0
zero_block_end_index = 0

longest_zero_block_length = 0
longest_zero_block_end_index = 0
for i in range(8):
    if shorter_blocks[i] == "0":
        zero_block_lenght += 1
        zero_block_end_index = i
    else:
        if zero_block_lenght > longest_zero_block_length:
            longest_zero_block_length = zero_block_lenght
            longest_zero_block_end_index = zero_block_end_index
        zero_block_lenght = 0
    

if zero_block_lenght > longest_zero_block_length:
    longest_zero_block_length = zero_block_lenght
    longest_zero_block_end_index = zero_block_end_index

if longest_zero_block_length > 1:
    shortest_address = ""
    zero_block_start_index = longest_zero_block_end_index \
        - (longest_zero_block_length-1)

    # rövidítéssel kezdünk
    if zero_block_start_index == 0:
        shortest_address += "::"
        for i in range(longest_zero_block_end_index+1, 7):
            shortest_address += f"{shorter_blocks[i]}:"
        shortest_address += shorter_blocks[7]

    # rövidítéssel végzünk
    elif longest_zero_block_end_index == 7:
        for i in range(8-longest_zero_block_length):
            shortest_address += f"{shorter_blocks[i]}:"
        shortest_address += ":"

    # középen rövidítünk
    else:
        for i in range(zero_block_start_index):
            shortest_address += f"{shorter_blocks[i]}:"
        shortest_address += ":"
        for i in range(longest_zero_block_end_index+1, 7):
            shortest_address += f"{shorter_blocks[i]}:"
        shortest_address += shorter_blocks[7]

    print(shortest_address)
else:
    print("Nem rövidíthető tovább.")
