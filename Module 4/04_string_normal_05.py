text = "В теории, теория и практика неразделимы." \
       " На практике это не так."

count = 0
summ = 0
text_lower=text.lower()
while count <= len(text.lower()):

    if "а" in text.lower() or "е" in text.lower() or "ё" in text.lower() or "и" in text.lower() \
            or "о" in text.lower() or "у" in text.lower() or "э" in text.lower() or \
            "ю" in text.lower() or "я" in text.lower():
        summ += 1
    count += 1

print(summ)
