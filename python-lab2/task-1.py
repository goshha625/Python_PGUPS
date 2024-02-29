input("Загадайте любое целое число от 1 до 1000, \nа программа угадает это число. Для продолжения нажмите ENTER.")

start = 1
end = 1000

for _ in range(10):
    attempt = start + (end-start)//2
    print(f"Я думаю, это число {attempt}.")
    answer = input("Ответьте '>', '<' или '=': ")
    while answer != '>' and answer != '<' and answer != '=':
        answer = input("Вы ввели недопустимый символ. Ответьте '>', '<' или '=': ")
    if answer == '=':
        print("Число угадано!")
    elif answer == '>':
        start = attempt + 1
    elif answer == '<':
        end = attempt - 1
    else:
        print("Вы ввели недопустимый символ. Повторите попытку")


