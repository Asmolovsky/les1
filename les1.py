try:
    a = int(input("Введите число: "))
    print("Введенное число: ", a)
except ValueError:
    print("Некорректное значение числа")
