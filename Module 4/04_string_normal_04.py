# password = input("Enter password: ")
# while True:
#     if "#" in password and len(password) >= 6 and password[0].isupper():
#         print("Пароль надежный")
#         break
# else:
#     print("пароль шляпа")
while True:
    password = input("Enter password: ")
    if len(password) >= 6 and password.count("#") > 0 and password[0].isupper():
        print("Password is OK")
        break
    else:
        print("Not secure password")
