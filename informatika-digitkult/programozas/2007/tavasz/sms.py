# 1. feladat
# Kérjen be a felhasználótól egy betűt,
# és adja meg, hogy milyen kód (szám) tartozik hozzá!
# Az eredményt írassa a képernyőre!

letter = input("Adjon meg egy (kis)betűt: ")

code_table = {
    "a": 2, "b": 2, "c": 2,
    "d": 3, "e": 3, "f": 3,
    "g": 4, "h": 4, "i": 4,
    "j": 5, "k": 5, "l": 5,
    "m": 6, "n": 6, "o": 6,
    "p": 7, "q": 7, "r": 7, "s": 7,
    "t": 8, "u": 8, "v": 8,
    "w": 9, "x": 9, "y": 9, "z": 9
}

print(f"A(z) {letter} betű kódja: {code_table[letter]}")


# 2. feladat
# Kérjen be a felhasználótól egy szót, és határozza meg,
# hogy milyen számsorral lehet ezt a telefonba bevinni!
# Az eredményt írassa a képernyőre!

def t9_encoder(word):
    code_table = {
    "a": "2", "b": "2", "c": "2",
    "d": "3", "e": "3", "f": "3",
    "g": "4", "h": "4", "i": "4",
    "j": "5", "k": "5", "l": "5",
    "m": "6", "n": "6", "o": "6",
    "p": "7", "q": "7", "r": "7", "s": "7",
    "t": "8", "u": "8", "v": "8",
    "w": "9", "x": "9", "y": "9", "z": "9"
    }
    result = ""
    for letter in word:
        result += code_table[letter]
    
    return result

word = input("Adjon meg egy szót: ")
print(f"A(z) \"{word}\" szót a {t9_encoder(word)} kóddal lehet a telefonba bevinni.")


# 3. feladat
# Olvassa be a szavak.txt fájlból a szavakat,
# és a továbbiakban azokkal dolgozzon!

words = []
code_count = {}
with open("szavak.txt", "rt", encoding="utf-8") as file:
    for line in file:
        word = line.strip()
        lenght = len(word)
        code = t9_encoder(word)
        w = {
            "word": word,
            "length": lenght,
            "code": code
        }
        words.append(w)

        if code not in code_count:
            code_count[code] = 0
        code_count[code] += 1


# 4. feladat
# Határozza meg és írassa a képernyőre, hogy melyik a leghosszabb tárolt szó!
# Amennyiben több azonos hosszúságú van, elegendő csak az egyiket megjeleníteni.
# Adja meg ennek a szónak a hosszát is!

longest_word = words[0]
for word in words:
    if word["length"] > longest_word["length"]:
        longest_word = word

print(f"A leghosszabb szó: \"{longest_word["word"]}\", "
      f"{longest_word["length"]} karakter hosszú.")


# 5. feladat
# Határozza meg és írassa a képernyőre, hogy hány rövid szó található a fájlban!
# Rövid szónak tekintjük a legfeljebb 5 karakterből álló szavakat.

short_word_count = 0
for word in words:
    if word["length"] <= 5:
        short_word_count += 1

print(f"A fáljban {short_word_count} db. rövid szó található.")


# 6. feladat
# Írassa a kodok.txt állományba a szavak.txt fájlban található szavaknak
# megfelelő számkódokat!
# Minden szónak feleljen meg egy számkód,
# és minden számkód külön sorba kerüljön!

with open("kodok.txt", "wt", encoding="utf-8") as file:
    for word in words:
        file.write(f"{word["code"]}\n")


# 7. feladat
# Kérjen be a felhasználótól egy számsort, és határozza meg,
# hogy melyik szó tartozhat hozzá!
# Amennyiben több szó is megfelelő, akkor mindegyiket írassa ki!

requested_code = input("Adjon meg egy számsort: ")
print(f"A {requested_code} számkódhoz az alábbi szavak tartoznak:")
for word in words:
    if word["code"] == requested_code:
        print(f"- {word["word"]}")


# 8. feladat
# Határozza meg, hogy a szógyűjteményben mely kódokhoz tartozik több szó is!
# Írassa ki a képernyőre ezeket a szavakat a kódjukkal együtt egymás mellé...

multiword_codes = []
for code in code_count:
    if code_count[code] > 1:
        multiword_codes.append(code)

print("Az alábbi kódokhoz tartozik több szó is:")
for word in words:
    if word["code"] in multiword_codes:
        print(f"{word["word"]} : {word["code"]}; ", end="")


# 9. feladat
# Határozza meg, hogy melyik kódnak megfelelő szóból van a legtöbb!
# Írassa ki a képernyőre a kódot, és a kódhoz tartozó összes tárolt szót!

most_frequent_code_count = 0
most_frequent_code = None
for code in code_count:
    if code_count[code] > most_frequent_code_count:
        most_frequent_code_count = code_count[code]
        most_frequent_code = code

print(f"A leggyakoribb számsor: {most_frequent_code}. A hozzá tartozó szavak:")
for word in words:
    if word["code"] == most_frequent_code:
        print(f"- {word["word"]}")
