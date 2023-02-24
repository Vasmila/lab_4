cvet1 = input("Введите 1 цвет : ")
cvet2 = input("Введите 2 цвет : ")
if (cvet1 == "красный" and cvet2 == "синий") or (cvet2 == "красный" and cvet1 == "синий"):
    print("фиолетовый")
elif (cvet1 == "красный" and cvet2 == "желтый") or (cvet2 == "красный" and cvet1 == "желтый"):
    print("оранжевый")
elif (cvet1 == "синий" and cvet2 == "желтый") or (cvet2 == "синий" and cvet1 == "желтый"):
    print("зеленый")
else:
    print("Ошибка")
