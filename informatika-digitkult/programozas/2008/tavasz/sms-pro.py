# E-Learning: https://elearning.tdg.hu/2008-majus/
# Teljes megoldás: https://youtu.be/CkRpaqspvWU

def binning(data: list, *limits):
    sorted_limits = sorted(limits)

    bins = []
    for i in range(len(sorted_limits)-1):
        bins.append(0)

    for item in data:
        if item < sorted_limits[0]:
            continue
        for i in range(1, len(sorted_limits)):
            if item <= sorted_limits[i]:
                bins[i-1] += 1
                break

    return bins


class Message:

    def __init__(self, hour: str, minute: str, sender: str, content: str):
        self.hour = int(hour)
        self.minute = int(minute)
        self.timestamp = self.hour*60 + self.minute
        self.sender = int(sender)
        self.content = content.strip()
        self.__length = len(self.content)

    def __str__(self):
        return self.content

    def __lt__(self, other):
        match other:
            case int():
                return self.__length < other
            case Message():
                return self.__length < other.__length
            case _:
                return self.__length < len(other)

    def __le__(self, other):
        match other:
            case int():
                return self.__length <= other
            case Message():
                return self.__length <= other.__length
            case _:
                return self.__length <= len(other)


class Inbox:

    def __init__(self):
        self.messages = {}

    def add_message(self, message: Message):
        if message.sender not in self.messages:
            self.messages[message.sender] = []
        self.messages[message.sender].append(message)

    def new_message(self, hour: str, minute: str, sender: str, content: str):
        message = Message(hour, minute, sender, content)
        self.add_message(message)

    def get_messages_by_sender(self, phone):
        return self.messages[phone]


# 1. feladat
# https://youtu.be/ij0mMWGpep8
messages = []
with open("sms.txt", "rt", encoding="utf-8") as file:
    message_count = int(file.readline())
    for message_index in range(message_count):
        message_data = file.readline()
        message_content = file.readline()

        data_parts = message_data.split(" ")

        message = Message(data_parts[0], data_parts[1], data_parts[2],
                          message_content)

        messages.append(message)


# 2. feladat
# https://youtu.be/pzO7IA2S6zA
print("2. feladat:")
if len(messages) < 10:
    last_message = messages[-1]
else:
    last_message = messages[9]

print(f"A telefonban a következő üzenet a legfrissebb:\n{last_message}")


# 3. feladat
# https://youtu.be/oXZJmM0bwnE
print("3. feladat")
longest_message = max(messages)
shortest_message = min(messages)

print("A legrövidebb üzenet: "
      f"{shortest_message.hour}, {shortest_message.minute}, "
      f"{shortest_message.sender}, {shortest_message}")
print("A leghosszabb üzenet: "
      f"{longest_message.hour}, {longest_message.minute}, "
      f"{longest_message.sender}, {longest_message}")


# 4. feladat
# https://youtu.be/GEx0rOiBfjk
print("4. feladat")
stat = binning(messages, 1, 20, 40, 60, 80, 100)

print(f"1-20: {stat[0]}\n"
      f"21-40: {stat[1]}\n"
      f"41-60: {stat[2]}\n"
      f"61-80: {stat[3]}\n"
      f"81-100: {stat[4]}")


# 5. feladat
print("5. feladat")
current_hour = messages[0].hour
hourly_message_count = 0
unread_message_count = 0
for message in messages:
    if message.hour != current_hour:
        hourly_message_count = 0
        current_hour = message.hour
    hourly_message_count += 1
    if hourly_message_count > 10:
        unread_message_count += 1

print(f"{unread_message_count} üzenethez kellene felhívni a szolgáltatót.")


# 6. feladat
# https://youtu.be/t8S7Q33kXe0
print("6. feladat")

inbox = Inbox()
for message in messages:
    inbox.add_message(message)

girlfriend_messages = inbox.get_messages_by_sender(123456789)

if len(girlfriend_messages) < 2:
    print("nincs elegendő üzenet")
else:
    max_message_difference = 0
    for i in range(1, len(girlfriend_messages)):
        difference = girlfriend_messages[i].timestamp - girlfriend_messages[i-1].timestamp
        if difference > max_message_difference:
            max_message_difference = difference

    max_difference_hour = max_message_difference // 60
    max_difference_minute = max_message_difference % 60
    print("A leghosszabb idő ami Ernő barátnőjének két üzenete közt telt el: "
          f"{max_difference_hour} {max_difference_minute}")


# 7. feladat
# https://youtu.be/ur7pmxHcCho
print("7. feladat")
hour = input("Adja meg az üzenet óráját: ")
minute = input("Adja meg az üzenet percét: ")
sender = input("Adja meg az üzenet küldőjének telefonszámát: ")
content = input("Adja meg az üzenet tartalmát: ")
inbox.new_message(hour, minute, sender, content)


# 8. feladat
# https://youtu.be/vHk41dCImrI
sorted_phone_numbers = sorted(inbox.messages)

with open("smski.txt", "wt", encoding="utf-8") as file:
    for sender in sorted_phone_numbers:
        msgs = inbox.get_messages_by_sender(sender)
        file.write(f"{sender}\n")
        for message in msgs:
            file.write(f"{message.hour} {message.minute} {message}\n")
