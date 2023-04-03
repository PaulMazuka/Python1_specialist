
# Функция нахождения максимального элемента
def my_max(*args):  # функция принимается любое кол-во аргрументов
    max_value =args[0]
    for arg in args:
        if arg > max_value:
            max_value == arg
    return max_value
