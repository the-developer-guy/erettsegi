# 1. feladat
# Kérjen be a felhasználótól egy maximum 255 karakternyi, nem üres szöveget!
# A továbbiakban ez a nyílt szöveg.

szoveg = input("Adjon meg egy legfeljebb 255 karakter hosszú szöveget! ")

# 2. feladat
# Alakítsa át a nyílt szöveget,
# hogy a későbbi kódolás feltételeinek megfeleljen!
# A kódolás feltételei:
# A magyar ékezetes karakterek helyett ékezetmenteseket kell használni
#   (Például á helyett a; ő helyett o stb.)
# A nyílt szövegben az átalakítás után csak az angol ábécé betűi szerepelhetnek
# A nyílt szöveg az átalakítás után legyen csupa nagybetűs

# Példa
# Nyílt szöveg: Ez a próba szöveg, amit kódolunk!
# Szöveg átalakítása: EZAPROBASZOVEGAMITKODOLUNK

atalakitott_szoveg = ""
for karakter in szoveg:
    if karakter.isalpha():
        nagybetus_karakter = karakter.upper()
        if nagybetus_karakter == "Á":
            nagybetus_karakter = "A"
        elif nagybetus_karakter == "É":
            nagybetus_karakter = "E"
        elif nagybetus_karakter == "Í":
            nagybetus_karakter = "I"
        elif nagybetus_karakter == "Ó":
            nagybetus_karakter = "O"
        elif nagybetus_karakter == "Ö":
            nagybetus_karakter = "O"
        elif nagybetus_karakter == "Ő":
            nagybetus_karakter = "O"
        elif nagybetus_karakter == "Ú":
            nagybetus_karakter = "U"
        elif nagybetus_karakter == "Ü":
            nagybetus_karakter = "U"
        elif nagybetus_karakter == "Ű":
            nagybetus_karakter = "U"
            
        atalakitott_szoveg += nagybetus_karakter


# 3. feladat
# Írja ki a képernyőre az átalakított nyílt szöveget!

print(atalakitott_szoveg)


# 4. feladat
# Kérjen be a felhasználótól egy maximum 5 karakteres, nem üres kulcsszót!
# A kulcsszó a kódolás feltételeinek megfelelő legyen!
# (Sem átalakítás, sem ellenőrzés nem kell!)
# Alakítsa át a kulcsszót csupa nagybetűssé!

bekert_kulcsszo = input("Adjon meg egy legfeljebb 5 karakteres kulcsszót: ")
kulcsszo = bekert_kulcsszo.upper()


# 5. feladat
# A kódolás első lépéseként fűzze össze a kulcsszót egymás után annyiszor,
# hogy az így kapott karaktersorozat (továbbiakban kulcsszöveg) hossza
# legyen egyenlő a kódolandó szöveg hosszával!
# Írja ki a képernyőre az így kapott kulcsszöveget!

kulcsszoveg = ""
kulcsszo_hossz = len(kulcsszo)
for i in range(len(atalakitott_szoveg)):
    kulcsszoveg += kulcsszo[i % kulcsszo_hossz]

print(f"Kulcsszöveg: {kulcsszoveg}")


# 6. feladat
# A kódolás második lépéseként a következőket hajtsa végre!
# Vegye az átalakított nyílt szöveg első karakterét,
# és keresse meg a vtabla.dat fájlból beolvasott táblázat első oszlopában!
# Ezután vegye a kulcsszöveg első karakterét,
# és keresse meg a táblázat első sorában!
# Az így kiválasztott sor és oszlop metszéspontjában lévő karakter lesz
# a kódolt szöveg első karaktere.
# Ezt ismételje a kódolandó szöveg többi karakterével is!

kodtabla = []
with open("Vtabla.dat", "rt", encoding="utf-8") as file:
    for line in file:
        kodtabla.append(line)

kodolt_szoveg = ""
print(f"'A' kódja {ord('A')}")
for i in range(len(atalakitott_szoveg)):
    oszlop_karakter = atalakitott_szoveg[i]
    sor_karakter = kulcsszoveg[i]
    oszlop_index = ord(oszlop_karakter) - 65
    sor_index = ord(sor_karakter) - 65

    kodolt_szoveg += kodtabla[sor_index][oszlop_index]


# 7. feladat
# Írja ki a képernyőre és a kodolt.dat fájlba a kapott kódolt szöveget!

print(f"A kódolt szöveg: {kodolt_szoveg}")

with open("kodolt.dat", "wt", encoding="utf-8") as file:
    file.write(kodolt_szoveg)
