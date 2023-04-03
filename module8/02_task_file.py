# Задаем путь к файлу:
path = "limericks.txt"  # вместо dir подставь название папки с файлом.
# Или удалите dir, если limericks.txt в той же папке, что и питоновский файл

# Открываем файл на чтение
f = open(path, "r", encoding="utf-8")
new_file = open("limericks_clean.txt", "w", encoding="utf-8")
# В переменную line считываем строку за стройкой из файла(f)
for line in f:
    line = line.replace(".", "")
    new_file.write(line)
f.close()
new_file.close()
