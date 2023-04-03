path = "sold.txt"
f = open("sold.txt", "r", encoding="utf-8")

numbers = []
for line in f:
    numbers_str = line.split()
    for num in numbers_str:
        numbers.append(float(num))

print(f'сумма:{sum(numbers):.2f}')
print(f'максимальная цена:{max(numbers):.2f}')
print(f'минимальная сумма:{min(numbers):.2f}')
