vag = int(input("Введите номер вагона: "))
if vag <= 54 and vag >= 1:
    if vag <= 35 and vag % 2 == 1:
        print("Нижнее, плацкарт")
    elif (vag <= 54 and vag >= 38 and vag % 2 == 0):
        print("Верхнее, боковое")
    elif (vag <= 36 and vag % 2 == 0):
        print("Верхнее, плацкарт")
    else:
        print("Нижнее, боковое")
else:
    print("Такого места нет")
