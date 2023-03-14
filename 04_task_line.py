number = int(input("Введите четырехзначное число: "))
n1 = number // 1000
n2 = number // 100 % 10
n3 = number // 10 % 10
n4 = number % 10
print("Первое число", n1)
print("Второе число", n2)
print("Третье число", n3)
print("Четвертое число", n4)
