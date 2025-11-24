# 1. feladat
# Olvassa be és tárolja el a valaszok.txt szöveges állomány adatait!

solutions = {}
with open("valaszok.txt", "rt", encoding="utf-8") as file:
    solution_key = file.readline().strip()
    for line in file:
        parts = line.strip().split(" ")
        solutions[parts[0]] = parts[1]


# 2. feladat
# Jelenítse meg a képernyőn a mintának megfelelően, hogy hány versenyző vett
# részt a tesztversenyen!

print(f"2. feladat: A vetélkedőn {len(solutions)} versenyző indult.")


# 3. feladat
# Kérje be egy versenyző azonosítóját, és jelenítse meg a mintának megfelelően a
# hozzá eltárolt válaszokat! Feltételezheti, hogy a fájlban létező azonosítót
# adnak meg.

requested_contestant = input("3. feladat: A versenyző azonosítója = ")
print(f"{solutions[requested_contestant]}")


# 4. feladat
# Írassa ki a képernyőre a helyes megoldást! A helyes megoldás alatti sorba
# „+” jelet tegyen, ha az adott feladatot az előző feladatban kiválasztott
# versenyző eltalálta, egyébként egy szóközt! A kiírást a mintának megfelelő
# módon alakítsa ki!

print("4. feladat")
print(solution_key)
for i in range(len(solution_key)):
    selected_solution = solutions[requested_contestant]
    if solution_key[i] == selected_solution[i]:
        print("+", end="")
    else:
        print(" ", end="")
print()


# 5. feladat
# Kérje be egy feladat sorszámát, majd határozza meg, hogy hány versenyző adott
# a feladatra helyes megoldást, és ez a versenyzők hány százaléka! A százalékos
# eredményt a mintának megfelelően, két tizedesjeggyel írassa ki!

requested_question = int(input("5. feladat: A feladat sorszáma = "))
requested_question_index = requested_question - 1
correct_answer_count = 0
correct_answer = solution_key[requested_question_index]
for id in solutions:
    if solutions[id][requested_question_index] == correct_answer:
        correct_answer_count += 1

print(f"A feladatra {correct_answer_count} fő, a versenyzők " 
      f"{len(solutions)/correct_answer_count:.2%}%-a adott helyes választ.")


# 6. feladat
# A verseny feladatai nem egyenlő nehézségűek: az 1-5. feladat 3 pontot, a 6-10.
# feladat 4 pontot, a 11-13. feladat 5 pontot, míg a 14. feladat 6 pontot ér.
# Határozza meg az egyes versenyzők pontszámát, és a listát írassa ki a
# pontok.txt nevű állományba! Az állomány minden sora egy versenyző kódját,
# majd szóközzel elválasztva az általa elért pontszámot tartalmazza!

scores = {}
points = [3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 6]
for id in solutions:
    submitted_solution = solutions[id]
    score = 0
    for i in range(len(solution_key)):
        if submitted_solution[i] == solution_key[i]:
            score += points[i]
    scores[id] = score

with open("pontok.txt", "wt", encoding="utf-8") as file:
    for id in scores:
        file.write(f"{id} {scores[id]}\n")


# 7. feladat
# A versenyen a három legmagasabb pontszámot elérő összes versenyzőt díjazzák.
# Például 5 indulónál előfordulhat, hogy 3 első és 2 második díjat adnak ki.
# Így megtörténhet az is, hogy nem kerül sor mindegyik díj kiadására. Írassa ki
# a mintának megfelelően a képernyőre a díjazottak kódját és pontszámát
# pontszám szerint csökkenő sorrendben!

unique_scores = set()
for id in scores:
    unique_scores.add(scores[id])

top_scores = []
for score in unique_scores:
    top_scores.append(score)

top_scores.sort(reverse=True)

top_contestants = [[], [], []]
for id in scores:
    for i in range(3):
        if scores[id] == top_scores[i]:
            top_contestants[i].append(id)
            break

print("7. feladat: A verseny legjobbjai:")
for i in range(3):
    for contestant in top_contestants[i]:
        print(f"{i+1}. díj ({top_scores[i]}): {contestant}")
