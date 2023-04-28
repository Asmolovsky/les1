TodayYear = int(input("Введите год сегодня: "))
TodayMonth = int(input("Введите месяц сегодня: "))
TodayDay = int(input("Введите день сегодня: "))
BdayYear = int(input("Введите год рождения: "))
BdayMonth = int(input("Введите месяц рождения: "))
BdayDay = int(input("Введите день рождения: "))
YearOld = TodayYear - BdayYear
MonthAge = 12-BdayMonth+TodayMonth
DayAge = 30-BdayDay+TodayDay
if MonthAge>12 or (MonthAge+1)>12:
    print(YearOld+1)
    if DayAge>=30 and (MonthAge+1)>=12:
        print("На 1 год больше")
else:
    print(YearOld)






