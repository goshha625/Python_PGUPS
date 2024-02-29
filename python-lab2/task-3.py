rocks = int(input("Сколько камней в куче?: "))

while rocks != 0:
    step = int(input("Ваш ход. Сколько камней хотите взять? (1-3): "))
    while step > rocks or step < 1 or step > 3:
        print(f"Недопустимый ход: {step}")
        step = int(input("Сколько камней хотите взять? (1-3): "))
    rocks -= step
    print(f"Вы взяли камней: {step} Осталось в куче: {rocks}")
    if rocks == 0:
        print("Вы выиграли")
        break
    else:
        if rocks == 3:
            step = 3
        elif rocks == 2:
            step = 2
        else:
            step = 1
    rocks -= step
    print(f"ИИ взял камней: {step} Осталось в куче: {rocks}")
    if rocks == 0:
        print("ИИ выиграл")
        break