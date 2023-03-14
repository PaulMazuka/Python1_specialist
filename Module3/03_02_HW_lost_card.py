# "Потерянная карточка"
# Задание
# Для настольной игры используются карточки с номерами от 1 до n. Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
#
# Вводится число n - количество карточек, затем n−1 чисел: номера оставшихся карточек (различные числа от 1 до n).
# Программа должна вывести номер потерянной карточки.
#
# Формат входных данных
# Дано целое число n - количество карточек
# И еще n-1 целых чисел: номера оставшихся карточек.
#
# Формат выходных данных.
# Выведите номер потерянной карточки.
quantity = int(input("Количество карточек: "))
# Цикл, который выполнится n-1 раз
counter_all_card = 1
counter_without_lost_card = 1
summary_all_card = 0
summary_without_lost_card = 0
while counter_without_lost_card < quantity:
    card_number = int(input("Номер карточки: "))
    summary_without_lost_card += card_number
    counter_without_lost_card += 1
while counter_all_card <= quantity:
    summary_all_card += counter_all_card
    counter_all_card += 1


print("Номер потерянной карточки:", summary_all_card - summary_without_lost_card)
