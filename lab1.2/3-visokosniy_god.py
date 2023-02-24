god = int(input("Введите год: "))
if god % 4 == 0:
    if god % 100 != 0:
        print("Високосный")
    else:
        if god % 400 == 0:
            print("Високосный")
        else:
            print("Невисокосный")
else:
    print("Невисокосный")
