# 1. feladat
# Olvassa be a szavazatok.txt fájl adatait, majd ezek felhasználásával oldja meg
# a következő feladatokat! Az adatfájlban legfeljebb 100 képviselőjelölt
# adatai szerepelnek.
print("1. feladat")
votes = []
with open("szavazatok.txt", "rt", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split(" ")
        vote = {
            "district": int(parts[0]),
            "vote_count": int(parts[1]),
            "name": f"{parts[2]} {parts[3]}",
            "party": parts[4]
        }


# 2. feladat
# Hány képviselőjelölt indult a helyhatósági választáson? A kérdésre egész
# mondatban válaszoljon az alábbi mintához hasonlóan:
# A helyhatósági választáson 92 képviselőjelölt indult.
print("2. feladat")
print(f"A helyhatósági választáson {len(votes)} képviselőjelölt indult.")


# 3. feladat
# Kérje be egy képviselőjelölt vezetéknevét és utónevét, majd írja ki a
# képernyőre, hogy az illető hány szavazatot kapott! Ha a beolvasott név nem
# szerepel a nyilvántartásban, úgy jelenjen meg a képernyőn az
# „Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!”
# figyelmeztetés! A feladat megoldása során feltételezheti, hogy
# nem indult két azonos nevű képviselőjelölt a választáson.
print("3. feladat")
candidate_name = input("Adja meg egy képviselőjelölt nevét: ").strip()
candidate_found = False
for vote in votes:
    if vote["name"] == candidate_name:
        candidate_found = True
        print(f"{candidate_name} {vote["vote_count"]} szavazatot kapott.")
        break
if not candidate_found:
    print("Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!")


# 4. feladat
# Határozza meg, hányan adták le szavazatukat, és mennyi volt a részvételi
# arány! (A részvételi arány azt adja meg, hogy a jogosultak hány százaléka vett
# részt a szavazáson.) A részvételi arányt két tizedesjegy pontossággal,
# százalékos formában írja ki a képernyőre! Például:
# A választáson 5001 állampolgár, a jogosultak 40,51%-a vett részt.
print("4. feladat")
vote_sum = 0
for vote in votes:
    vote_sum += vote["vote_count"]

print(f"A választáson {vote_sum} állampolgár, a jogosultak "
      f"{vote_sum/12345:.2%}-a vett részt.")


# 5. feladat
# Határozza meg és írassa ki a képernyőre az egyes pártokra leadott szavazatok
# arányát az összes leadott szavazathoz képest két tizedesjegy pontossággal! 
# A független jelölteket együtt, „Független jelöltek” néven szerepeltesse!
# Például:
# Zöldségevők Pártja= 12,34%
# Független jelöltek= 23,40%
print("5. feladat")
votes_by_party = {
    "GYEP": 0,
    "HEP": 0,
    "TISZ": 0,
    "ZEP": 0,
    "-": 0,
}

for vote in votes:
    votes_by_party[vote["party"]] += vote["vote_count"]

print(f"Gyümölcsevők Pártja= {votes_by_party["GYEP"]/vote_sum:.2%}")
print(f"Húsevők Pártja= {votes_by_party["HEP"]/vote_sum:.2%}")
print(f"Tejivók Szövetsége= {votes_by_party["TISZ"]/vote_sum:.2%}")
print(f"Zöldségevők Pártja= {votes_by_party["ZEP"]/vote_sum:.2%}")
print(f"Független jelöltek= {votes_by_party["-"]/vote_sum:.2%}")


# 6. feladat
# Melyik jelölt kapta a legtöbb szavazatot? Jelenítse meg a képernyőn a
# képviselő vezeték- és utónevét, valamint az őt támogató párt rövidítését, vagy
# azt, hogy független! Ha több ilyen képviselő is van,
# akkor mindegyik adatai jelenjenek meg!
print("6. feladat")
high_score = 0
highest_voted = []
for vote in votes:
    if vote["vote_count"] > high_score:
        high_score = vote["vote_count"]
        highest_voted = [vote]
    elif vote["vote_count"] == high_score:
        highest_voted.append(vote)

for vote in highest_voted:
    if vote["party"] == "-":
        print(f"{vote["name"]} független")
    else:
        print(f"{vote["name"]} {vote["party"]}")


# 7. feladat
# Határozza meg, hogy az egyes választókerületekben kik lettek a képviselők!
# Írja ki a választókerület sorszámát, a győztes vezeték- és utónevét, valamint
# az őt támogató párt rövidítését, vagy azt, hogy független egy-egy szóközzel
# elválasztva a kepviselok.txt nevű szöveges fájlba! Az adatok a
# választókerületek száma szerinti sorrendben jelenjenek meg!
# Minden sorba egy képviselő adatai kerüljenek!
print("7. feladat")
districts = {}
for vote in votes:
    if vote["district"] not in districts:
        districts[vote["district"]] = []
    vote["district"].append(vote)

with open("kepviselok.txt", "wt", encoding="utf-8") as file:
    for i in range(1, 9):
        current_votes = districts[i]
        winner = current_votes[0]
        for vote in current_votes:
            if vote["vote_count"] > winner["vote_count"]:
                winner = vote
        party = winner["party"]
        if party == "-":
            party = "független"
        file.write(f"{i} {winner["name"]} {party}\n")
