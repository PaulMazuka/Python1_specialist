name = "Иван"
age = 32
job_title = "Бухгалтер"

"Уважаемые,  ... ...  Поздравляем вас с  ..."

message1 = "Уважаемый, " + name + " " + job_title + " ." + " Поздравляем вас c "+ str(age)
message2 = "Уважаемый, %s  %s. Поздравляем вас с %s" % (name, job_title, age)
message3="Уважаемый, {}  {}. Поздравляем вас с {}".format (name, job_title, age)
message4=f"Уважаемый, {name.upper()}  {job_title}. Поздравляем вас с {age + 1}"
print(message1)
print(message2)
print(message3)
print(message4)
