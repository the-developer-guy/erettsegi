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
