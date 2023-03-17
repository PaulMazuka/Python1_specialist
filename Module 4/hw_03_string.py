# Посчитайте количество согласных букв в данной строке.

text = "Антон Борис Алексей Федор Боря"

consonants = 0

for letter in text.lower():
    if letter.isalpha():
        if letter in "б в г д ж з й к л м н п р с т ф х ц ч ш щ":
            consonants +=1
print(consonants)