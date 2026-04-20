import ipaddress

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
print(f"A legalacsonyabb tárolt IP-cím:\n{min(addresses)}")


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
    if address.startswith(ADDRESS_TYPE_DOC):
        documentation_address_count += 1
    elif address.startswith(ADDRESS_TYPE_GLOBAL):
        global_address_count += 1
    elif address.startswith(ADDRESS_TYPE_LOCAL_FC) or \
        address.startswith(ADDRESS_TYPE_LOCAL_FD):
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
    for i, address in enumerate(addresses, start=1):
        if address.count("0") >= 18:
            destination_file.write(f"{i} {address}\n")


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
    block_value = int(block, 16)
    short_blocks.append(f"{block_value:x}")

shorter_address = ":".join(short_blocks)
print(shorter_address)
print(*short_blocks, sep=":")


# 7. feladat
# Az előző feladatban használt IP-címet rövidítse tovább az egymást követő
# nullás csoportok rövidítésére vonatkozó szabályoknak megfelelően! Az eredményt
# jelenítse meg a képernyőn! Amennyiben nem rövidíthető, írja ki:
# Nem rövidíthető tovább.
print("7. feladat:")
addr = ipaddress.ip_address(shorter_address)
if shorter_address == str(addr):
    print("Nem rövidíthető tovább.")
else:
    print(addr)
