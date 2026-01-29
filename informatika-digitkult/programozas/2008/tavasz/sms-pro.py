def binning(data: list, *limits):
    if len(limits) < 3:
        raise TypeError("binning() requires at least 3 limit values, "
                        f"got {len(limits)}")
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
        return self.__length < other.__length

    def __len__(self):
        return self.__length


class Inbox:

    def __init__(self):
        self.messages = {}
        pass

    def new_message(self, hour: str, minute: str, sender: str, content: str):
        message = Message(hour, minute, sender, content)
        self.add_message(message)

    def add_message(self, message: Message):
        if message.sender not in self.messages:
            self.messages[message.sender] = []
        self.messages[message.sender].append(message)

    def get_messages_by_sender(self, phone):
        return self.messages[phone]


# 1. feladat
messages = []
with open("sms.txt", "rt", encoding="utf-8") as file:
    count = int(file.readline())
    for message_index in range(count):
        message_data = file.readline()
        message_content = file.readline()

        data_parts = message_data.split(" ")

        message = Message(data_parts[0], data_parts[1], data_parts[2],
                          message_content)
        messages.append(message)


# 2. feladat
print("2. feladat:")
if len(messages) < 10:
    last_message = messages[-1]
else:
    last_message = messages[9]

print(f"A telefonban a következő üzenet a legfrissebb:\n{last_message}")


# 3. feladat
print("3. feladat:")
longest_message = max(messages)
shortest_message = min(messages)

print("A legrövidebb üzenet: "
      f"{shortest_message.hour}, {shortest_message.minute}, "
      f"{shortest_message.sender}, {shortest_message}")
print("A leghosszabb üzenet: "
      f"{longest_message.hour}, {longest_message.minute}, "
      f"{longest_message.sender}, {longest_message}")


# 4. feladat
print("4. feladat:")
stat = [0, 0, 0, 0, 0]
for message in messages:
    message_lenght = len(message)
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
print("5. feladat:")
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
print("6. feladat:")
girlfriend_messages = []
for message in messages:
    if message.sender == 123456789:
        girlfriend_messages.append(message)

if len(girlfriend_messages) < 2:
    print("nincs elegendő üzenet")
else:
    max_message_difference = 0
    for i in range(1, len(girlfriend_messages)):
        difference = messages[i].timestamp - messages[i-1].timestamp
        if difference > max_message_difference:
            max_message_difference = difference

    max_difference_hour = max_message_difference // 60
    max_difference_minute = max_message_difference % 60
    print("A leghosszabb idő ami Ernő barátnőjének két üzenete közt telt el: "
          f"{max_difference_hour} {max_difference_minute}")


# 7. feladat
print("7. feladat:")
hour = input("Adja meg az üzenet óráját: ")
minute = input("Adja meg az üzenet percét: ")
sender = input("Adja meg az üzenet küldőjének telefonszámát: ")
content = input("Adja meg az üzenet tartalmát: ")
late_message = Message(hour, minute, sender, content)
messages.append(late_message)

# 8. feladat

inbox = Inbox()
for message in messages:
    inbox.add_message(message)

sorted_phone_numbers = sorted(inbox.messages)

with open("smski.txt", "wt", encoding="utf-8") as file:
    for sender in sorted_phone_numbers:
        messages = inbox.get_messages_by_sender(sender)
        file.write(f"{sender}\n")
        for message in messages:
            file.write(f"{message.hour} {message.minute} {message}\n")
