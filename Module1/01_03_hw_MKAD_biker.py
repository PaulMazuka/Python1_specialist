print("Длина Московской кольцевой автомобильной дороги — 109 километров./n"
      " Байкер стартует с нулевого километра МКАД и едет со скоростью v километров в час. /n"
      "На какой отметке он остановится через t часов?")
MKAD_LEN = 109  # Большими буквами потому что переменная константа
speed = int(input("Введите скорость байкера(км/ч): "))
time = int(input("Введите время через которое байкер остановится(в часах)"))
position = (speed * time) % MKAD_LEN
print("Через ", time, "часов. Байкер остановится на отметке- ", position, "-й километр")
# И походу работает с отрицательными числами корректно. Проверял на 107км и 200км