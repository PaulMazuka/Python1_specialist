number_a = int(input("Введите число А: "))
number_b = int(input("Введите число Б: "))

perfect_numbers = ""
summa_perfect_numbers = 0
while number_a <= number_b:
    summ_div = 0
    div = 1
    while div < number_a:
        if number_a % div == 0:
            summ_div += div
        div += 1
    if summ_div == number_a:
        perfect_numbers += str(number_a) + str(" ")
        summa_perfect_numbers += number_a
    number_a += 1
print("Список совершенных чисел в диапазоне от А до Б ", perfect_numbers)
print("Сумма всех совершенных чисел в диапазоне от А до Б равна= ", summa_perfect_numbers)

# Задание
# Число совершенно, если оно равно сумме всех своих делителей,
# кроме самого себя. Пример: 6 = 1 + 2 + 3.
# Найдите все совершенные числа и их количество в заданном диапазоне [a, b].
#
# Формат входных данных
# Даны два целых положительных числа, границы диапазона. Гарантируется, что a < b.
#
# Формат выходных данных
# Вывести все совершенные числа, а затем их количество.
