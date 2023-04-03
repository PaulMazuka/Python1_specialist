while True:
    try:
        n = int(input("n: "))
        m = int(input("m: "))
        break
    except ValueError:
        print("некорректные данные")

try:
    res = n / m
    print("res=", res)
except ZeroDivisionError:
    print("На ноль делить нельзя")
