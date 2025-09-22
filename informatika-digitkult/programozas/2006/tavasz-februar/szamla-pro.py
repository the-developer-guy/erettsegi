import math

def idobol_idobelyeg(ora, perc, masodperc):
    idobelyeg = int(ora) * 60 * 60 + int(perc) * 60 + int(masodperc)

    return idobelyeg


def bekert_idobol_idobelyeg(hivas_idopont):
    hivas_reszek = hivas_idopont.split(":")
    ora = hivas_reszek[0]
    perc = hivas_reszek[1]
    masodperc = hivas_reszek[2]
    idobelyeg = idobol_idobelyeg(ora, perc, masodperc)

    return idobelyeg


def mobilszam(telefonszam):
    mobil_szamok = [39, 41, 71]
    korzetszam = int(telefonszam[:2])

    return korzetszam in mobil_szamok


def megkezdett_perc(kezdet_idobelyeg, vege_idobelyeg):
    hossz = vege_idobelyeg - kezdet_idobelyeg

    return math.ceil(hossz / 60)


def percdij(szam, csucsido):
    if mobilszam(szam):
        if csucsido:
            return 69.175
        else:
            return 46.675
    else:
        if csucsido:
            return 30
        else:
            return 15


# 1. feladat
bekert_telefonszam = input("Adjon meg egy telefonszámot: ")

if mobilszam(bekert_telefonszam):
    print("A megadott telefonszám mobil")
else:
    print("A megadott telefonszám vezetékes szám")


# 2. feladat
hivas_kezdete = input("Adja meg egy hívás kezdetének időpontját (ó:p:m): ")
hivas_vege = input("Adja meg egy hívás végének időpontját (ó:p:m): ")

hivas_kezdet_idobelyeg = bekert_idobol_idobelyeg(hivas_kezdete)
hivas_vege_idobelyeg = bekert_idobol_idobelyeg(hivas_vege)
percek_szama = megkezdett_perc(hivas_kezdet_idobelyeg, hivas_vege_idobelyeg)
print(f"A megadott időtartam {percek_szama} percnek számít")


hivasok = []
with open("HIVASOK.TXT", "rt", encoding="utf-8") as file:
    for i, line in enumerate(file):
        if i & 1 == 0:
            hivas = {}
            hivas_reszek = line.split(" ")

            hivas_kezdete_ora = int(hivas_reszek[0])
            hivas["csucsido"] = 7 <= hivas_kezdete_ora < 18

            hivas_kezdet_idobelyeg = idobol_idobelyeg(hivas_reszek[0],
                                                      hivas_reszek[1],
                                                      hivas_reszek[2])
            hivas_vege_idobelyeg = idobol_idobelyeg(hivas_reszek[3],
                                                    hivas_reszek[4],
                                                    hivas_reszek[5])
            hivas["hossz"] = megkezdett_perc(hivas_kezdet_idobelyeg, hivas_vege_idobelyeg)
        else:
            szam = line.strip()
            hivas["telefonszam"] = szam

            hivas["mobilszam"] = mobilszam(szam)
            
            hivas["dij"] = hivas["hossz"] * percdij(szam, hivas["csucsido"])

            hivasok.append(hivas)


# 3. feladat
with open("percek.txt", "wt", encoding="utf-8") as file:
    for hivas in hivasok:
        file.write(f"{hivas["hossz"]} {hivas["telefonszam"]}\n")


# 4. feladat
csucsidos_hivasok_szama = 0
csucsidon_kivuli_hivasok_szama = 0
for hivas in hivasok:
    if hivas["csucsido"]:
        csucsidos_hivasok_szama += 1
    else:
        csucsidon_kivuli_hivasok_szama += 1

print(f"{csucsidos_hivasok_szama} hívás volt csúcsidőben és "
      f"{csucsidon_kivuli_hivasok_szama} hívás volt csúcsidőn kívül.")


# 5. feladat 
mobil_hivasok = [hivas["hossz"] for hivas in hivasok if hivas["mobilszam"]]
vezetekes_hivasok = [hivas["hossz"] for hivas in hivasok if not hivas["mobilszam"]]

print(f"A felhasználó {sum(mobil_hivasok)} percet beszélt mobil számmal és "
      f"{sum(vezetekes_hivasok)} percet beszélt vezetékes számmal.")


# 6. feladat
csucsidos_dijak = [hivas["dij"] for hivas in hivasok if hivas["csucsido"]]

print(f"A felhasználónak {sum(csucsidos_dijak):.2f} Forintot kell fizetnie a "
      "csúcsidős hívásokért.")
