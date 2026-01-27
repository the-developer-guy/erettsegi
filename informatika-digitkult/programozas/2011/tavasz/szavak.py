def vowel_count(word):
    return 0

# 1. feladat
# Kérjen be a felhasználótól egy szót, és döntse el, hogy tartalmaz-e 
# magánhangzót! Amennyiben tartalmaz, írja ki, hogy „Van benne magánhangzó.”!
# Ha nincs, akkor írja ki, hogy „Nincs benne magánhangzó.”! A begépelendő szóról
# feltételezheti, hogy csak az angol ábécé kisbetűit tartalmazza.
# (Az angol ábécé magánhangzói: a, e, i, o, u.)

word = input("Adjon meg egy szót: ")
i = 0
while i < len(word):
    current_character = word[i]
    if current_character == "a" or \
        current_character == "e" or \
        current_character == "i" or \
        current_character == "o" or \
        current_character == "u":
        break
    i += 1

if i == len(word):
    print("Nincs benne magánhangzó.")
else:
    print("Van benne magánhangzó.")


# 2. feladat
# Írja ki a képernyőre, hogy melyik a leghosszabb szó a szoveg.txt állományban,
# és az hány karakterből áll! Ha több azonos leghosszabb hosszúságú szó is van a
# szógyűjteményben, akkor azok közül elegendő egyetlen szót kiírnia. A feladatot
# úgy oldja meg, hogy tetszőleges hosszúságú szövegállomány esetén működjön,
# azaz a teljes szöveget ne tárolja a memóriában!

with open("szoveg.txt", "rt", encoding="utf-8") as file:
    longest_word = file.readline().strip()
    for line in file:
        word = line.strip()
        if len(word) > len(longest_word):
            longest_word = word

print(f"A leghosszabb szó: \"{longest_word}\", hossza: {len(longest_word)}.")


# 3. feladat
# A magyar nyelv szavaiban általában kevesebb a magánhangzó, mint a
# mássalhangzó. Határozza meg, hogy az állomány mely szavaiban van több
# magánhangzó, mint egyéb karakter! Ezeket a szavakat írja ki a képernyőre
# egy-egy szóközzel elválasztva! A szavak felsorolása után a mintának
# megfelelően az alábbi adatokat adja meg:
# • hány szót talált;
# • hány szó van összesen az állományban;
# • a talált szavak hány százalékát teszik ki az összes szónak!
# A százalékot két tizedessel szerepeltesse! Például:
# 130/3000 : 4,33%

vowel_heavy_word_count = 0
word_count = 0
with open("szoveg.txt", "rt", encoding="utf-8") as file:
    for line in file:
        word = line.strip()
        word_count += 1
        if vowel_count(word) > len(word):
            vowel_heavy_word_count += 1

print(f"{vowel_heavy_word_count}/{word_count} : "
      f"{vowel_heavy_word_count/word_count:.2%}")


# 4. feladat
# Hozzon létre egy tömb vagy lista adatszerkezetet, és ebbe gyűjtse ki a fájlban
# található ötkarakteres szavakat! A szoveg.txt állomány legfeljebb 1000 darab
# ötkarakteres szót tartalmaz. Kérjen be a felhasználótól egy 3 karakteres
# szórészletet! Írja ki a képernyőre a szólétra építés szabályai szerint hozzá
# tartozó ötkarakteres szavakat a tárolt adathalmazból! A kiírásnál a szavakat
# egy-egy szóköz válassza el! (Teszteléshez használhatja például az „isz” vagy
# „obo” szórészleteket, mert ezekhez a megadott szövegállományban több létraszó
# is tartozik.)

ladder_words = []
with open("szoveg.txt", "rt", encoding="utf-8") as file:
    for line in file:
        word = line.strip()
        if len(word) == 5:
            ladder_words.append(word)

word_middle = input("Adjon meg egy 3 karakteres fokot: ")
print(f"A \"{word_middle}\" fokhoz tartozó szavak:")
for word in ladder_words:
    if word[1:4] == word_middle:
        print(word, end=" ")


# 5. feladat
# Az eltárolt ötkarakteres szavakból csoportosítsa azokat a szavakat, melyek
# ugyanannak a hárombetűs szórészletnek a létraszavai! Hozzon létre egy
# letra.txt állományt, amelybe ezeket a szavakat írja az alábbiak szerint:
# • minden szó külön sorba kerüljön;
# • csak olyan szó szerepeljen az állományban, aminek van legalább egy párja,
# amivel egy létrát alkotnak (azaz első és utolsó karakter nélkül megegyeznek);
# • az egy létrához tartozó szavak közvetlenül egymás után helyezkedjenek el;
# • két létra szavai között egy üres elválasztó sor legyen!

ladders = {}
for word in ladder_words:
    word_middle = word[1:4]
    if word_middle not in ladders:
        ladders[word_middle] = []
    ladders[word_middle].append(word)

with open("letra.txt", "wt", encoding="utf-8") as file:
    for ladder in ladders:
        if len(ladders[ladder]) == 1:
            continue

        for word in ladders[ladder]:
            file.write(f"{word}\n")
        file.write("\n")
