balance = int(input("Введите сумму больше 0: "))
price = int(input("Введите стоимость больше 0: "))
change = balance - price
if balance >= price:
    print("Ваш остаток после покупки", change, "рублей")
else:
    print(" у вас недостаточно денег для покупки")
