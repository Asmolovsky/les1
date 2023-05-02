try:
    Year1 = int(input("Введите год1: "))
    Month1 = int(input("Введите месяц1: "))
    Day1 = int(input("Введите день1: "))
    Year2 = int(input("Введите год2: "))
    Month2 = int(input("Введите месяц2: "))
    Day2 = int(input("Введите день2: "))
    if Year1>Year2:
        print("Второй человек старше")
    elif Year2>Year1:
        print("Первый человек старше")
    elif Year1==Year2:
        if Month1>Month2:
            print("Второй человек старше")
        elif Month2>Month1:
            print("Первый человек старше")
        elif Month1==Month2:
            if Day1>Day2:
                print("Второй человек старше")
            elif Day2>Day1:
                print("Первый человек старше")
except ValueError:
    print("Вы ввели не число!")












