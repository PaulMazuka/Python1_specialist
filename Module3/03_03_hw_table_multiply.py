# x = input("Введите число для таблицы умножения от 1 до 9: ")
# for a in range(1, int(x) + 1):
#     print(f'{a:4}', end="")
# print("")
# for w in range(1, int(x) + 1):
#     print(f'{w}', end="")
#     for y in range(1, int(x) + 1):
#         print(f'{y * w:3}', end=" ")
#     print("")

# мое решение
# digit = int(input("Введите число для таблицы умножения от 1 до 9: "))
# count_row= 1
#
# while count_row <= digit:
#     count = 1
#     while count <= digit:
#         print(count*count_row, end=" ")
#         count += 1
#     print("")
#     count_row += 1
#
# решение препода

n =int(input("Размер таблицы умножения: "))  # размер таблицы
k =0  # номер строки
while k < n:
    line=""
    i=0
    k += 1
    while i<n:
        i += 1
        line += str(i*k)+ " "

    print(line)


