seconds = int(input("Прошло секунд: "))
day = seconds // 86400
hour = seconds // 3600
if hour >= 24:
    hour = hour - 24
minutes = (seconds // 60) % 60
last_seconds = seconds % 60
print(day, " Дней ", hour, " Часов ", minutes, " минут", last_seconds, " секунд")
