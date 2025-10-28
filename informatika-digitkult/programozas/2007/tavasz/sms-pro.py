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


class T9Word:

    def __init__(self, word: str):
        self.__word = word.strip()
        self.__code = t9_encoder(self.__word)

    def get_code(self):
        return self.__code

    def __len__(self):
        return len(self.__word)

    def __str__(self):
        return self.__word


# 1. feladat
letter = input("Adjon meg egy (kis)betűt: ")
print(f"A(z) \"{letter}\" betű kódja: {t9_encoder(letter)}")


# 2. feladat
word = input("Adjon meg egy szót: ")
print(f"A(z) \"{word}\" szót a {t9_encoder(word)} kóddal lehet a telefonba bevinni.")


# 3. feladat
words = []
code_count = {}
with open("szavak.txt", "rt", encoding="utf-8") as file:
    for line in file:
        w = T9Word(line)
        words.append(w)

        code_count[w.get_code()] = code_count.get(w.get_code(), 0) + 1


# 4. feladat
longest_word = words[0]
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(f"A leghosszabb szó: \"{longest_word}\", "
      f"{len(longest_word)} karakter hosszú.")


# 5. feladat
short_word_count = 0
for word in words:
    if len(word) <= 5:
        short_word_count += 1

print(f"A fáljban {short_word_count} db. rövid szó található.")


# 6. feladat
with open("kodok.txt", "wt", encoding="utf-8") as file:
    for word in words:
        file.write(f"{word.get_code()}\n")


# 7. feladat
requested_code = input("Adjon meg egy számsort: ")
specific_words = [str(word) for word in words if word.get_code() == requested_code]
if len(specific_words) == 0:
    print(f"Nem tartozik szó a(z) {requested_code} kódhoz.")
else:
    print(f"A {requested_code} számkódhoz az alábbi szavak tartoznak:")
    print(*specific_words, sep=", ")


# 8. feladat
multiword_codes = [code for code in code_count if code_count[code] > 1]
print("Az alábbi kódokhoz tartozik több szó is:")
print_items = []
for word in words:
    if word.get_code() in multiword_codes:
        print_items.append(f"{word} : {word.get_code()}")
print(*print_items, sep="; ")


# 9. feladat
sorted_codes = sorted(code_count.items(), key=lambda item: item[1])
most_frequent_code = sorted_codes[-1][0]

print(f"A leggyakoribb számsor: {most_frequent_code}. A hozzá tartozó szavak:")
for word in words:
    if word.get_code() == most_frequent_code:
        print(f"- {word}")
