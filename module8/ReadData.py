f = open("data.txt", "r", encoding="utf-8")

for line in f:
    line = line.rstrip()  # удаление пробелов слева
    print(line)

f.close()  # закрытие файла после его использования

# Пробельные символы:
# " " пробел
# "/n"   перенос
# "/t"   табуляция
