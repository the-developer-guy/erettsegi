# 1. feladat
# Olvassa be az sms.txt állományban talált adatokat,
# s annak felhasználásával oldja meg a következő feladatokat!
# Ha az állományt nem tudja beolvasni, akkor a benne található adatok közül
# az első tíz üzenet adatait jegyezze be a programba,
# s úgy oldja meg a feladatokat!


messages = []
with open("sms.txt", "rt", encoding="utf-8") as file:
    count = int(file.readline())
    for message_index in range(count):
        message_data = file.readline()
        message_content = file.readline()

        data_parts = message_data.split(" ")

        message = {
            "hour": int(message_data[0]),
            "minute": int(message_data[1]),
            "timestamp": int(message_data[0])*60 + int(message_data[1]),
            "sender": message_data[2],
            "message": message_content,
            "length": len(message_content)
        }

        messages.append(message)


# 2. feladat
# A fájlban tárolt utolsó üzenet érkezésekor melyik üzenet a legfrissebb
# a telefon memóriájában? Írja az üzenet szövegét a képernyőre!

print("2. feladat:")
if len(messages) < 10:
    i = len(messages) - 1
    last_message = messages[i]
else:
    last_message = messages[9]


# 3. feladat
# Adja meg a leghosszabb és a legrövidebb üzenetek adatait!
# Ha több azonos hosszúságú üzenet van, akkor elegendő csak egyet-egyet
# megadnia! A képernyőn 
# óra, perc, telefonszám, üzenet 
# formában jelenítse meg az adatokat!

print("3. feladat:")
longest_message = messages[0]
shortest_message = messages[0]
for message in messages:
    if message["length"] > longest_message["length"]:
        longest_message = message
    if message["length"] < shortest_message["length"]:
        shortest_message = message


# 4. feladat
# Készítsen karakterhossz szerinti statisztikát: 
# 1-20, 21-40, 41-60, 61-80, 81-100!
# Az intervallumok mellé a hozzájuk tartozó üzenetek darabszámát írja,
# mint eredményt a képernyőre!

print("4. feladat:")
stat = [0, 0, 0, 0, 0]
for message in messages:
    message_lenght = message["length"]
    if 0 < message_lenght <= 20:
        stat[0] += 1
    elif 20 < message_lenght <= 40:
        stat[1] += 1
    elif 40 < message_lenght <= 60:
        stat[2] += 1
    elif 60 < message_lenght <= 80:
        stat[3] += 1
    elif 80 < message_lenght <= 100:
        stat[4] += 1

print(f"1-20: {stat[0]}\n"
      f"21-40: {stat[1]}\n"
      f"41-60: {stat[2]}\n"
      f"61-80: {stat[3]}\n"
      f"81-100: {stat[4]}")

# 5. feladat
# Ha Ernő minden óra 0. percében elolvasná a memóriában lévő üzeneteket 
# (az éppen ekkor érkező üzeneteket nem látja), majd ki is törölné, 
# akkor hány olyan üzenet lenne, amelynek elolvasásához fel kellene hívnia 
# a szolgáltatót? Írja ezt a számot a képernyőre!
# (Az üzeneteket először 1, utoljára 24 órakor olvassa el.)

print("5. feladat:")
current_hour = messages[0]["hour"]
hourly_message_count = 0
unread_message_count = 0
for message in messages:
    if message["hour"] != current_hour:
        hourly_message_count = 0
        current_hour = message["hour"]
    hourly_message_count += 1
    if hourly_message_count > 10:
        unread_message_count += 1


# 6. feladat
# Ernő barátnője gyakran küld sms-t az 123456789-es számról. 
# Mennyi volt a leghosszabb idő, amennyi eltelt két üzenete között?
# Ha legfeljebb 1 üzenet érkezett tőle, akkor írja ki, hogy 
# „nincs elegendő üzenet”, egyébként pedig adja meg 
# a leghosszabb időtartamot óra perc alakban!

print("6. feladat:")
girlfriend_messages = []
for message in messages:
    if message["sender"] == "123456789":
        girlfriend_messages.append(message)

max_message_difference = 0
for i in range(1, len(girlfriend_messages)):
    difference = messages[i]["timestamp"] - messages[i-1]["timestamp"]
    if difference > max_message_difference:
        max_message_difference = difference


# 7. feladat
# Egy üzenet véletlenül késett.
# Olvassa be a billentyűzetről ennek az sms-nek az adatait,
# majd tárolja el a memóriában a többihez hasonlóan!

print("7. feladat:")

# 8. feladat
# Az smski.txt állományban készítsen egy listát az üzenetekről 
# telefonszám szerinti csoportosításban, telefonszám szerint növekvő sorrendben!
# Egy csoporthoz tartozó első sorban a feladó telefonszáma szerepeljen!
# Az alatta lévő sorokban a feladás ideje, 
# majd a tőle újabb szóközzel elválasztva az üzenet szövege szerepeljen!

messages_by_sender = {}
senders = []
for message in messages:
    sender = message["sender"]
    if sender not in senders:
        senders.append(sender)
        messages_by_sender[sender] = []
    
    messages_by_sender[sender].append(message)

senders.sort()

with open("smski.txt", "wt", encoding="utf-8") as file:
    for sender in senders:
        msgs = messages_by_sender[sender]
        file.write(f"{sender}\n")
        for message in msgs:
            file.write(f"{message["hour"]} {message["minute"]} "
                       f"{message["message"]}\n")
