# Дан прямоугольник размером n×m. Напишите программу, вычисляющую, сколько квадратов
# со стороной m от него получится отрезать.

# На вход программе подается строка формата nxm (x - латинская буква икс).
# Пример входных данных: 12x6
# Если данные вводятся в неверном формате, сообщить об этом и запросить ввод заново.

while True:
    userinput = input("Введите размер прямоугольника в формате AxB: ")
    pair = userinput.split("x")
    try:
        if len(pair) !=2:
            raise ValueError
        n = int(pair[0])
        m = int(pair[1])
        if n <= 0 or m <=0:
            raise ValueError
        break
    except (IndexError, ValueError):
        print("Некорректные данные")
num_squares = n // m

print(f"Можно получить {num_squares} квадратов со стороной {m}")
