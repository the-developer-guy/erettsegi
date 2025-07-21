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


# 2. feladat
# Kérjen be továbbá egy hívás kezdeti és hívás vége időpontot
# óra perc másodperc formában!
# A két időpont alapján határozza meg,
# hogy a számlázás szempontjából hány perces a beszélgetés!
# A kiszámított időtartamot írja ki a képernyőre!

hivas_kezdete = input("Adja meg egy hívás kezdetének időpontját (ó:p:m): ")
hivas_vege = input("Adja meg egy hívás végének időpontját (ó:p:m): ")

hivas_kezdet_reszek = hivas_kezdete.split(":")
hivas_kezdet_ora = int(hivas_kezdet_reszek[0])
hivas_kezdet_perc = int(hivas_kezdet_reszek[1])
hivas_kezdet_masodperc = int(hivas_kezdet_reszek[2])

hivas_vege_reszek = hivas_vege.split(":")
hivas_vege_ora = int(hivas_vege_reszek[0])
hivas_vege_perc = int(hivas_vege_reszek[1])
hivas_vege_masodperc = int(hivas_vege_reszek[2])

hivas_kezdet_idobelyeg = hivas_kezdet_ora * 60 * 60 + hivas_kezdet_perc * 60 + hivas_kezdet_masodperc
hivas_vege_idobelyeg = hivas_vege_ora * 60 * 60 + hivas_vege_perc * 60 + hivas_vege_masodperc
hivas_hossz = hivas_vege_idobelyeg - hivas_kezdet_idobelyeg

# Minden megkezdett perc egy egész percnek számít.
percek_szama = hivas_hossz // 60
if hivas_hossz % 60 != 0:
    percek_szama += 1

print(f"A megadott időtartam {percek_szama} percnek számít")


# Fájl beolvasása és adatmodellezés a további feladatokhoz

hivasok = []
with open("HIVASOK.TXT", "rt", encoding="utf-8") as file:
    telefonszam = False
    hivas = {}
    for line in file:
        if telefonszam:
            hivas["telefonszam"] = line.strip()
            hivasok.append(hivas)
            hivas = {}
            telefonszam = False
        else:
            hivas_reszek = line.split(" ")
            hivas_kezdet_ora = int(hivas_reszek[0])
            hivas_kezdet_perc = int(hivas_reszek[1])
            hivas_kezdet_masodperc = int(hivas_reszek[2])
            hivas_vege_ora = int(hivas_reszek[0])
            hivas_vege_perc = int(hivas_reszek[1])
            hivas_vege_masodperc = int(hivas_reszek[2])

            if hivas_kezdet_ora >= 7 and hivas_kezdet_ora < 18:
                hivas["csucsido"] = True
            else:
                hivas["csucsido"] = False

            hivas_kezdet_idobelyeg = hivas_kezdet_ora * 60 * 60 + hivas_kezdet_perc * 60 + hivas_kezdet_masodperc
            hivas_vege_idobelyeg = hivas_vege_ora * 60 * 60 + hivas_vege_perc * 60 + hivas_vege_masodperc
            hivas_hossz = hivas_vege_idobelyeg - hivas_kezdet_idobelyeg

            percek_szama = hivas_hossz // 60
            if hivas_hossz % 60 != 0:
                percek_szama += 1
            
            hivas["hossz"] = percek_szama
            telefonszam = True


# 3. feladat
# Állapítsa meg a hivasok.txt fájlban lévő hívások időpontja alapján,
# hogy hány számlázott percet telefonált a felhasználó hívásonként!
# A kiszámított számlázott perceket írja ki a percek.txt fájlba 
# a következő formában!
# perc telefonszám

with open("percek.txt", "wt", encoding="utf-8") as file:
    for hivas in hivasok:
        file.write(f"{hivas["hossz"]} {hivas["telefonszam"]}\n")


# 4. feladat
# Állapítsa meg a hivasok.txt fájl adatai alapján,
# hogy hány hívás volt csúcsidőben és csúcsidőn kívül!
# Az eredményt jelenítse meg a képernyőn!

csucsidos_hivasok_szama = 0
csucsidon_kivuli_hivasok_szama = 0
for hivas in hivasok:
    if hivas["csucsido"] == True:
        csucsidos_hivasok_szama += 1
    else:
        csucsidon_kivuli_hivasok_szama += 1

print(f"{csucsidos_hivasok_szama} hívás volt csúcsidőben és "
      f"{csucsidon_kivuli_hivasok_szama} hívás volt csúcsidőn kívül.")