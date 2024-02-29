password = input("Password: ")
password_check = input("Repeat Password: ")

if len(password) < 8:
    print("Короткий!")
elif '123' in password:
    print("Простой!")
elif password != password_check:
    print("Различаются.")
else:
    print("OK")
