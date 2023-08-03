n = int(input('Введите число: '))
f1 = 1
f2 = 2
print(f1, f2, end=" ")
for i in range(3,n+1):
    print(f1+f2, end=" ")
    b = f1
    f1 = f2
    f2 = b+f1
print ()
print ()
n = int(input('Введите число: '))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(factorial)










