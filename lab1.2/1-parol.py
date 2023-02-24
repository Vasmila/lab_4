par = input("Введите пароль: ")
if len(par) < 6:
    print("Пароль слишком короткий")
else:
    par1 = input("Введите повторный пароль: ")
    if par == par1:
        print("Пароль принят")
