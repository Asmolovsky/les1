try:
    number=(input("Введите трехзначное число: "))
    a=int(number)//100
    c=int(number)%10
    b=int(number)//10%10
    print(a+b+c)
except ValueError:
    print("Пожалуйста вводите цифры")












