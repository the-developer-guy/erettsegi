# 0. feladat
# A következő feladatokat oldja meg egy program segítségével!
# A programot mentse szamla néven!

# 1. feladat
# Kérjen be a felhasználótól egy telefonszámot!
# Állapítsa meg a program segítségével, hogy a telefonszám mobil-e vagy sem!
# A megállapítást írja ki a képernyőre!

bekert_telefonszam = input("Adjon meg egy telefonszámot: ")

# Minden telefonszám elején egy kétjegyű körzetszám,
# illetve mobil hívószám található.
korzetszam = bekert_telefonszam[0:2]

# A mobil hívószámok: 39, 41, 71 kezdődnek, 
if korzetszam == "39" or korzetszam == "41" or korzetszam == "71":
    print("A megadott telefonszám mobil")
# minden egyéb szám vezetékes hívószámnak felel meg.
else:
    print("A megadott telefonszám vezetékes szám")
