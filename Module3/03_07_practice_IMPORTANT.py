n = int(input("Введите количество cтрок из чисел от 1 до 9: "))
i = 1
line = ""
while i <= n:
    line = line + str(i)
    print(line)
    i += 11

#"Лесенка"
# Задание
# По данному числу n выведите лесенку из n ступенек. Кадлая i-я
# ступень состоит из чисел от 1 до i без пробелов
#
# Пример
# Для n = 4
# Нужно вывести:
# 1
# 12
# 123
# 1234
#
# Формат входных данных
# Дано целое число в диапазоне [1, 9]
#
# Формат выходных данных
# Вывести лесенку из чисел.
