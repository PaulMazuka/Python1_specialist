f = open("numbers.txt", "r", encoding="utf-8")
sum_numbers = 0
count = 0
for line in f:
    sum_numbers += int(line)
    count += 1
average = sum_numbers / count
print(sum_numbers)
print(f'{average:.2f}')

f.close()
