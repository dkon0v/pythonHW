x = abs(int(input('Введите натуральное число X диапазоном от 1 до 1000')))
y = abs(int(input('Введите натуральное число Y диапазоном от 1 до 1000')))
if x < 1 or x > 1000 or y < 1 or y > 1000:
    print ('Вы ввели число не из заданного диапазона!')
else:
    S = x + y
    P = x * y
    stop = 0
    for i in range(1001):
        if stop != 1:
            for r in range(1001):
                if stop != 1:
                    if i * r == P and i + r == S:
                        print(i,r)
                        stop = 1
            else:
                r = 1001
        else:
            i = 1001