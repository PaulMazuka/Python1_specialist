# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    if ticket_number < 100_000 or ticket_number > 999_999:
        raise ValueError("Номер должен быть 6ти значным")
    sum1 = 0
    sum2 = 0
    for i, n in enumerate(str(ticket_number)):
        if i < 3:
            sum1 += int(n)
        else:
            sum2 += int(n)
    return sum1 == sum2


# Тестируем функцию
ticket = int(input("Номер билета: "))
try:
    if lucky_ticket(ticket):
        print("Номер счастливый")
    else:
        print("номер не счастливый")
except ValueError as e:
    print(e)

# print(lucky_ticket(123006))
# print(lucky_ticket(12321))
# print(lucky_ticket(436751))
# print(lucky_ticket(1100200))
