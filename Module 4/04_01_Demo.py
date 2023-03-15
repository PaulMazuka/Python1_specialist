numbers = [2, 45, 0, -34, 23, -5, 0, 5, -45]
# посчитать сколько положительных чисел в списке
num_positive = 0
for number in numbers:
    if number > 0:
        num_positive += 1
print(num_positive)
