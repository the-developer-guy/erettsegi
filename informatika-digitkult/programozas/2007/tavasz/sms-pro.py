def t9_encoder(text: str):
    result = ""

    for letter in text:
        l = letter.lower()
        match l:
            case "a" | "b" | "c":
                result += "2"
            case "d" | "e" | "f":
                result += "3"
            case "g" | "h" | "i":
                result += "4"
            case "j" | "k" | "l":
                result += "5"
            case "m" | "n" | "o":
                result += "6"
            case "p" | "q" | "r" | "s":
                result += "7"
            case "t" | "u" | "v":
                result += "8"
            case "w" | "x" | "y" | "z":
                result += "9"
            case " " | "." | "," | "?" | "!":
                result += "0"
            case _:
                pass
    
    return result

class T9_Word:

    def __init__(self, word: str):
        self.word = word.strip()
        self.code = t9_encoder(word)

    def __len__(self):
        return len(self.word)
    
    def __str__(self):
        return self.word


# 1. feladat
letter = input("Adjon meg egy (kis)betűt: ")
print(f"A(z) {letter} betű kódja: {t9_encoder(letter)}")


# 2. feladat
# Kérjen be a felhasználótól egy szót, és határozza meg,
# hogy milyen számsorral lehet ezt a telefonba bevinni!
# Az eredményt írassa a képernyőre!

word = input("Adjon meg egy szót: ")
print(f"A(z) \"{word}\" szót a {t9_encoder(word)} kóddal lehet a telefonba bevinni.")


# 3. feladat
# Olvassa be a szavak.txt fájlból a szavakat,
# és a továbbiakban azokkal dolgozzon!

words = []
code_count = {}
with open("szavak.txt", "rt", encoding="utf-8") as file:
    for line in file:
        w = T9_Word(line)
        words.append(w)

        code_count[w.code] = code_count.get(w.code, 0) + 1


# 4. feladat
# Határozza meg és írassa a képernyőre, hogy melyik a leghosszabb tárolt szó!
# Amennyiben több azonos hosszúságú van, elegendő csak az egyiket megjeleníteni.
# Adja meg ennek a szónak a hosszát is!

longest_word = words[0]
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(f"A leghosszabb szó: \"{longest_word}\", "
      f"{len(longest_word)} karakter hosszú.")


# 5. feladat
# Határozza meg és írassa a képernyőre, hogy hány rövid szó található a fájlban!
# Rövid szónak tekintjük a legfeljebb 5 karakterből álló szavakat.

short_word_count = 0
for word in words:
    if len(word) <= 5:
        short_word_count += 1

print(f"A fáljban {short_word_count} db. rövid szó található.")


# 6. feladat
# Írassa a kodok.txt állományba a szavak.txt fájlban található szavaknak
# megfelelő számkódokat!
# Minden szónak feleljen meg egy számkód,
# és minden számkód külön sorba kerüljön!

with open("kodok.txt", "wt", encoding="utf-8") as file:
    for word in words:
        file.write(f"{word.code}\n")


# 7. feladat
# Kérjen be a felhasználótól egy számsort, és határozza meg,
# hogy melyik szó tartozhat hozzá!
# Amennyiben több szó is megfelelő, akkor mindegyiket írassa ki!

requested_code = input("Adjon meg egy számsort: ")
specific_words = [str(word) for word in words if word.code == requested_code]
if len(specific_words) == 0:
    print(f"Nem tartozik szó a(z) {requested_code} kódhoz.")
else:
    print(f"A {requested_code} számkódhoz az alábbi szavak tartoznak:")
    print(*specific_words, sep=", ")


# 8. feladat
# Határozza meg, hogy a szógyűjteményben mely kódokhoz tartozik több szó is!
# Írassa ki a képernyőre ezeket a szavakat a kódjukkal együtt egymás mellé...

multiword_codes = [code for code in code_count if code_count[code] > 1]
print("Az alábbi kódokhoz tartozik több szó is:")
print_items = []
for word in words:
    if word.code in multiword_codes:
        print_items.append(f"{word} : {word.code}")
print(*print_items, sep="; ")


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
    if word.code == most_frequent_code:
        print(f"- {word}")
