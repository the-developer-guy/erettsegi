# 1. feladat
# Kérjen be a felhasználótól egy betűt,
# és adja meg, hogy milyen kód (szám) tartozik hozzá!
# Az eredményt írassa a képernyőre!

letter = input("Adjon meg egy (kis)betűt: ")

code = {
    "a": 2, "b": 2, "c": 2,
    "d": 3, "e": 3, "f": 3,
    "g": 4, "h": 4, "i": 4,
    "j": 5, "k": 5, "l": 5,
    "m": 6, "n": 6, "o": 6,
    "p": 7, "q": 7, "r": 7, "s": 7,
    "t": 8, "u": 8, "v": 8,
    "w": 9, "x": 9, "y": 9, "z": 9
}

print(f"A(z) {letter} betű kódja: {code[letter]}")

