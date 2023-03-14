limit = int(input("limit: "))

number = 0
summary = 0
while number <= limit:
    summary += number
    number += 2
print("Сумма всех чётных чисел от 0 до ", limit, " равна", summary)
