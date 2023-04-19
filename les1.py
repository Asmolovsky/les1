n = int(input('Введите число 1-99 '))
if 1<n<=4 or 21<n<=24 or 31<n<=34 or 41<n<=44 or 51<n<=54 or 61<n<=64 or 71<n<=74 or 81<n<=84 or 91<n<=94:
    print("мне", n, "года")
elif 4<n<21 or 24<n<31 or 34<n<41 or 44<n<51 or 54<n<61 or 64<n<71 or 74<n<81 or 84<n<91 or 94<n<100:
    print("мне", n, "лет")
elif n > 99 or n < 1:
        print('Выход за возрастное ограничение!')
else:
    print("мне", n, "год")