# Дано произвольное предложение. Слова разделены пробелами. Предложение содержит знаки препинания.
# Найдите:
# 1) первое слово из строки
# 2) первые два символа каждого слова
# 3) все слова начинающиеся на гласную букву
# 4) все слова начинающиеся на согласную букву
# 5) все уникальные(без дубликатов) знаки препинания
import re

text = "Какой-то текст. В котором,есть знаки препинания"

# 1) первое слово из строки
template = r"^[А-Яа-я-]+"
result = re.findall(template, text)
print(result)

# 2) первые два символа каждого слова
template = r"\b\w{2}"
result = re.findall(template, text)
print(result)
# 3) все слова начинающиеся на гласную букву
template = r"\b[аиеёоуюя]\w*"
result = re.findall(template, text.lower())
print(result)
# 4) все слова начинающиеся на согласную букву
template = r"\b[бвгдйжзклмнпрстфхцчшщ]"
result = re.findall(template, text.lower())
print(result)
# 5) все уникальные(без дубликатов) знаки препинания
template = r"[!,.?-]"
result = re.findall(template, text)
result1 = list(set(result))

print(result1)
