a = int(input('Введите число 1 '))
b = int(input('Введите число 2 '))
c = int(input('Введите число 3 '))
if a+b>c and a+c>b and b+c>a:
    print('Существует')
else:
    print('Не существует')