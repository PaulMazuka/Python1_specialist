# x = input("Введите число для таблицы умножения от 1 до 9: ")
# for a in range(1, int(x) + 1):
#     print(f'{a:4}', end="")
# print("")
# for w in range(1, int(x) + 1):
#     print(f'{w}', end="")
#     for y in range(1, int(x) + 1):
#         print(f'{y * w:3}', end=" ")
#     print("")
digit = int(input("Введите число для таблицы умножения от 1 до 9: "))
count_row= 1

while count_row <= digit:
    count = 1
    while count <= digit:
        print(count*count_row, end=" ")
        count += 1
    print("")
    count_row += 1


