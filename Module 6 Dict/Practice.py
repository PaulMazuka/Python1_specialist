def my_abs(a):
    b = 0 - a
    return b


# print(my_abs(-5))
# print(my_abs(5))


def max2(n1, n2):
    if n1 > n2:
        return n1
    return n2


# print(max2(15, 15))
# print(max2(5, 6))
# print(max2(-10, -12))
# print(max2(2.5, 2.6))
# print(max2(-2.5, 0))
# print(max2(0, -2.5))
#

# def even(a):
#     if a % 2 == 0:
#         return True
#     return False
# Вот так короче
def even(a):
    return a % 2 == 0



n = 99999
if even(n):
    print("Число четное")
else:
    print("Число не четное")
