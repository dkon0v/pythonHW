''' Задача 2 . '''

num = input('Введите трехзначное число')
res = 0
if len(num) == 3:
    for i in num:
        res += int(i)
    print (res)
else:
    print ('Введите трехзначное число')