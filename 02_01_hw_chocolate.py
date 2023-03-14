size_a = int(input("Введите количество долек по горизонтали"))
size_b = int(input("Введите количество долек по вертикали"))
parts = int(input("Введите количество долек которые хотите съесть"))
s_chocolate = size_a * size_b
if (parts % size_a == 0 or parts % size_b == 0) and parts <= s_chocolate:
    print("Да ")
print("Нет")
