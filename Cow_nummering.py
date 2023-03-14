n= int(input("Введите сколько коров пасутся на лугу: "))
last_dig=n%10
second_last_dig=n//10%10
if last_dig == 1 and second_last_dig != 1:
    print("на лугу пасутся ",n, "корова!")
elif  last_dig in range(2,5) and second_last_dig != 1:
    print("на лугу пасутся ",n, "коровы!")
elif last_dig >= 5 or second_last_dig == 1:
    print("на лугу пасутся ",n, "коров!")